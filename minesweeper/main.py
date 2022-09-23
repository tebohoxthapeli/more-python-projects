from Board import Board
from re import split


def play(dimen_size: int = 10, num_bombs: int = 10):
    # step 1: create the board and plant the bombs
    board = Board(dimen_size, num_bombs)

    # step 2: show the user the board and ask where they want to dig
    # step 3a: if location is a bomb, show game over message
    # step 3b: if location is not a bomb, dig recursively until each square is at least next to a
    # bomb
    # step 4: repeat steps 2 and 3a/b until there are no more places to dig -> victory

    safe = True

    while len(board.dug) < board.dimen_size**2 - num_bombs:
        print(board)

        user_input = split(
            ",\\s*", input("Where would you like to dig?: Input as row, col:\n")
        )

        row, col = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= board.dimen_size or col < 0 or col >= dimen_size:
            print("Invalid location. Try again.")
            continue

        # if valid, dig
        safe = board.dig(row, col)

        if not safe:
            # set all locations to dug so that they can be revealed, including the bombs

            board.dug = {
                (r, c) for r in range(board.dimen_size) for c in range(board.dimen_size)
            }

            print(board)
            print("YOU DUG A BOMB. GAME OVER.")
            quit()

    print("YOU HAVE WON!")


def main():
    play()


if __name__ == "__main__":
    main()

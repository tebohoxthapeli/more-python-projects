from time import sleep
from TicTacToe import TicTacToe


def play(
    game: TicTacToe,
    x_player,
    o_player,
    print_game: bool = True,
) -> str | None:
    if print_game:
        game.print_board_nums()

    # starting letter
    letter = "x"

    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that, which breaks the loop)

    while game.empty_squares():
        # get move from appropriate player:
        if letter == "o":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(f"\n{letter} makes a move to square {square}")
                game.print_board()

            if game.current_winner:
                if print_game:
                    print(f"\n{letter} wins")
                return letter

            # after we made our move, we need to alternate letters
            letter = "o" if letter == "x" else "x"  # switches player

            # only sleep when human is playing
            if print_game:
                sleep(0.8)

    if print_game:
        print("\nIt's a tie")
    return None


from GeniusComputer import GeniusComputer

from NormalComputer import NormalComputer

# from Human import Human


def main():
    normal_computer = 0
    genius_computer = 0
    ties = 0
    iterations = 50

    print("\nGames in progress. Please wait...\n")

    for _ in range(iterations):
        result = play(
            game=TicTacToe(),
            x_player=NormalComputer("x"),
            o_player=GeniusComputer("o"),
            print_game=False,
        )

        if result == "o":
            genius_computer += 1
        elif result == "x":
            normal_computer += 1
        else:
            ties += 1

    print(f"After {iterations} games:")
    print(f"{ties = }:")
    print(f"{normal_computer = }:")
    print(f"{genius_computer = }:")


if __name__ == "__main__":
    main()

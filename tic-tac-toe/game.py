import time


class TicTacToe:
    def __init__(self):
        # single list to rep 3x3 board
        self.board = [" " for _ in range(9)]

        # keep track of winner
        self.current_winner = None

    @staticmethod
    def print_board_nums() -> None:
        # example: | 0 | 1 | 2 |
        # tells us what number corresponds to what box

        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]

        for row in number_board:
            print(f"| {' | '.join(row)} |")

        print()

    def print_board(self) -> None:
        # get the rows
        space_board = [self.board[i * 3 : (i + 1) * 3] for i in range(3)]

        for row in space_board:
            print(f"| {' | '.join(row)} |")

    def available_moves(self) -> list[int]:
        return [idx for idx, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self) -> bool:
        return " " in self.board

    def num_empty_squares(self) -> int:
        return self.board.count(" ")

    def winner(self, square, letter):
        # winner if 3 same letters in a row, in any direction
        # check all directions
        # check row first

        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]

        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]

        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if the square is an even number (0,2,4,6,8)
        # only even numbers fall on either of the 2 diagonals

        if square % 2 == 0:
            # left to right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]

            if all([spot == letter for spot in diagonal1]):
                return True

            # right to left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]

            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of these fail
        return False

    def make_move(self, square, letter):
        # if move is valid then make it (assign letter to square)
        # then return true
        # If move is invalid, return false

        if self.board[square] == " ":
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True

        return False


def play(game: TicTacToe, x_player, o_player, print_game=True):
    # returns winner of the game (the letter) or None for a tie
    if print_game:
        game.print_board_nums()

    # starting letter
    letter = "x"

    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)

    while game.empty_squares():
        # get move from appropriate player:
        if letter == "o":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("")  # just empty line

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins")
                return letter

            # after we made our move, we need to alternate letters
            letter = "o" if letter == "x" else "x"  # switches player

            # tiny pause
            time.sleep(0.8)

    if print_game:
        print("It's a tie")


import player


def main():
    x_player = player.Human("x")
    o_player = player.Computer("o")
    t = TicTacToe()

    play(t, x_player, o_player, print_game=True)


if __name__ == "__main__":
    main()

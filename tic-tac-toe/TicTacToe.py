class TicTacToe:
    def __init__(self):
        # single list to rep 3x3 board
        self.board = [" " for _ in range(9)]

        # keep track of winner
        self.current_winner = None

    # staticmethod because does not relate to any specific
    # object, no need to pass 'self'
    @staticmethod
    def print_board_nums() -> None:
        # example: | 0 | 1 | 2 |
        # tells us what number corresponds to what box

        board_rows = [
            [
                str(spot_index)
                for spot_index in range(row_index * 3, (row_index * 3) + 3)
            ]
            for row_index in range(3)
        ]

        for row in board_rows:
            print(f"| {' | '.join(row)} |")

    def print_board(self) -> None:
        # get the rows
        board_rows = [
            self.board[row_index * 3 : (row_index * 3) + 3] for row_index in range(3)
        ]

        for row in board_rows:
            print(f"| {' | '.join(row)} |")

    def available_moves(self) -> list[int]:
        return [index for index, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self) -> bool:
        return " " in self.board

    def num_empty_squares(self) -> int:
        return self.board.count(" ")

    def is_winner(self, square: int, letter: str):
        # winner if 3 same letters in a row, in any direction
        # check all directions
        # check row first

        row_index = square // 3
        row = self.board[row_index * 3 : (row_index * 3) + 3]

        if all([spot == letter for spot in row]):
            return True

        # check column
        col_index = square % 3
        column = [self.board[col_index + row_index * 3] for row_index in range(3)]

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

    def make_move(self, square: int, letter: str):
        # if move is valid then make it (assign letter to square) then return true
        # If move is invalid, return false

        if self.board[square] == " ":
            self.board[square] = letter

            if self.is_winner(square, letter):
                self.current_winner = letter
            return True
        return False

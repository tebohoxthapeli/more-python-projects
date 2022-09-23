from random import randint
from typing import Any

TBoard = list[list[Any]]


class Board:
    def __init__(self, dimen_size: int, num_bombs: int) -> None:
        self.dimen_size = dimen_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # initialise set to keep track of which locations have been dug
        # save (row, col) tuples into this set
        # if dug at 0,0 then self.dug = {(0,0)}

        self.dug = set()

    def get_empty_board(self) -> TBoard:
        return [[None for _ in range(self.dimen_size)] for _ in range(self.dimen_size)]

    def make_new_board(self) -> TBoard:
        board = self.get_empty_board()
        bombs_planted = 0
        total_spots = self.dimen_size**2

        while bombs_planted < self.num_bombs:
            location = randint(0, total_spots - 1)

            row = location // self.dimen_size
            col = location % self.dimen_size

            if board[row][col] == "*":
                # already planted bomb
                continue

            # no bomb here: plant it
            board[row][col] = "*"
            bombs_planted += 1

        return board

    def get_neighbour_range(self, r_or_c: int) -> range:
        # helper function to get_num_neighbouring_bombs
        # use this to access neighbours

        # TL: (row-1, col-1)
        # TM: (row-1, col)
        # TR: (row-1, col+1)
        # R: (row, col-1)
        # L: (row, col+1)
        # BL: (row+1, col-1)
        # BM: (row+1, col)
        # BR: (row+1, col+1)

        # range(a, b+1) -> +1 because the 2nd arg is exclusive
        # min and max used to avoid going out of bounds

        return range(max(0, r_or_c - 1), min(self.dimen_size - 1, r_or_c + 1) + 1)

    def get_num_neighbouring_bombs(self, row: int, col: int) -> int:
        # iterate through each neighbouring position + sum number of bombs

        num_neighbouring_bombs = 0

        for r in self.get_neighbour_range(row):
            for c in self.get_neighbour_range(col):
                if self.board[r][c] == "*":
                    num_neighbouring_bombs += 1

        return num_neighbouring_bombs

    def assign_values_to_board(self) -> None:
        # now that the bombs have been planted, assign a number (0-8) for all the empty spaces,
        # which represents number of neighbouring bombs

        iter_ds = range(self.dimen_size)

        for row in iter_ds:
            for col in iter_ds:
                if self.board[row][col] == "*":
                    # already a bomb
                    # don't calculate anything
                    # don't want to override bomb
                    continue

                self.board[row][col] = self.get_num_neighbouring_bombs(row, col)

    def dig(self, row: int, col: int) -> bool:
        # dig at (row, col)
        # return True if successful dig
        # return False if bomb dug

        # few scenarios:

        # hit a bomb -> game over
        # dig at location with neighouring bombs -> finish dig
        # dig at location with no neighbouring bombs -> recursively dig neighbours

        # keep track that already dug here
        self.dug.add((row, col))

        cur_spot = self.board[row][col]

        if cur_spot == "*":
            return False
        elif cur_spot > 0:
            return True

        for r in self.get_neighbour_range(row):
            for c in self.get_neighbour_range(col):
                if (r, c) in self.dug:
                    # don't dig where already dug
                    continue

                self.dig(r, c)

        # if we have dug everywhere and nothing is returned from the for-loop above
        # that means for sure we won't dig up a bomb
        return True

    def fmt_out(self, val) -> str:
        if val == "-":
            return str(val).center(5, "-")
        return str(val).center(5)

    def join_head(self, join_char: str) -> str:
        val_list = []

        for i in range(self.dimen_size + 1):
            if i > 0:
                if join_char == "-":
                    val_list.append(self.fmt_out(join_char))
                else:
                    val_list.append(self.fmt_out(i - 1))
            else:
                val_list.append(self.fmt_out(""))

        return join_char.join(val_list)

    def __str__(self) -> str:
        visible_board = self.get_empty_board()
        string_rep = f"\n{self.join_head(' ')}\n{self.join_head('-')}\n"

        for row in range(self.dimen_size):
            for col in range(self.dimen_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = self.fmt_out(self.board[row][col])
                else:
                    visible_board[row][col] = self.fmt_out("")

            string_rep += f"{self.fmt_out(row)}|{'|'.join(visible_board[row])}|\n"

        return string_rep

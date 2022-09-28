from input_collection import Puzzle


def print_mat_str_repr(matrix: Puzzle) -> None:
    str_matr: list[list[str]] = []

    for r in range(3):
        new_row = []

        for c in range(3):
            val = str(matrix[r][c])

            if val == "-1":
                val = ""

            new_row.append(val.center(3))

        str_matr.append(new_row)

    str_repr = ""

    for r in str_matr:
        str_repr += f"\n|{'|'.join(r)}|"

    print(f"\n{str_repr}\n\n")


def print_puzzle_str_repr(puzzle: Puzzle) -> None:
    str_puzzle: list[list[str]] = []

    for r in range(9):
        new_row = []

        for c in range(9):
            val = str(puzzle[r][c])

            if val == "-1":
                val = " "

            new_row.append(val.center(3))

            if c in [3 - 1, 6 - 1]:
                new_row.append("".center(13))

        str_puzzle.append(new_row)

        if r in [3 - 1, 6 - 1]:
            str_puzzle.append([])

    str_repr = ""

    for r in str_puzzle:
        str_repr += f"\n|{'|'.join(r)}|" if len(r) else "\n"

    print(str_repr)

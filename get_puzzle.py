from re import compile


def get_str_repr(puzzle: list[list[int]]) -> str:
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

    str_rep = ""

    for r in str_puzzle:
        str_rep += f"\n|{'|'.join(r)}|" if len(r) else "\n"

    return str_rep


def is_quit(user_input: str) -> None:
    if user_input.lower() == "q":
        print("\nInfo: Quitting program...")
        quit()


def is_duplicate(user_input: str) -> bool:
    no_period = user_input.replace(".", "")
    return len(no_period) > len(set(no_period))


def get_row_vals(col_idxs: list[int], row_nr: int) -> list[tuple[int, int]]:
    regex = r"^[1-9\.]{,3}$"
    pattern = compile(regex)

    while True:
        user_input = input(f"row: {row_nr} -> ")
        is_quit(user_input)

        if user_input:
            match = pattern.search(user_input)

            if match and not is_duplicate(user_input):
                user_input = user_input.ljust(3, ".")
                vals_and_idxs = [x for x in zip(user_input, col_idxs)]
                vals_and_idxs = list(filter(lambda x: x[0] != ".", vals_and_idxs))

                return [(int(x[0]), x[1]) for x in vals_and_idxs]

            print("Error: Something went wrong.")
        else:
            return []


def get_puzzle() -> list[list[int]]:
    final_puzzle = [[-1 for _ in range(9)] for _ in range(9)]
    idxs = [[b for b in range(3 * a, 3 * a + 3)] for a in range(3)]

    for matr_row_nr in range(3):
        print(f"matrix row: {matr_row_nr + 1}")
        for matr_nr in range(3):
            print(f"matrix: {matr_nr + 1}")

            for row_nr, row_idx in enumerate(idxs[matr_row_nr], 1):
                for val, col_idx in get_row_vals(idxs[matr_nr], row_nr):
                    final_puzzle[row_idx][col_idx] = val

    return final_puzzle


def main():
    print(get_str_repr(get_puzzle()))


if __name__ == "__main__":
    main()

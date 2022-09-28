Puzzle = list[list[int]]

from re import compile
from instructions import get_instructions
from formatters import print_mat_str_repr


def is_quit(user_input: str) -> None:
    if user_input.lower() == "q":
        print("\nInfo: Quitting program...")
        quit()


def is_duplicate(user_input: str):
    user_input = user_input.replace(".", "")
    return len(user_input) > len(set(user_input))


def get_row_vals(col_idxs: list[int], row_nr: int) -> list[tuple[int, int]]:
    regex = r"^[1-9\.]{,3}$"
    pattern = compile(regex)

    while True:
        user_input = input(f"row: {row_nr} -> ")
        is_quit(user_input)

        if user_input and user_input not in "...":
            match = pattern.search(user_input)

            if match and not is_duplicate(user_input):
                user_input = user_input.ljust(3, ".")
                user_input = ",".join(list(user_input)).replace(".", "-1").split(",")
                vals_and_idxs = [x for x in zip(user_input, col_idxs)]

                return [(int(x[0]), x[1]) for x in vals_and_idxs]

            print(
                "User input error: Invalid input entered. Please read the instructions and try again."
            )
            get_instructions()
        else:
            print("There are no blocks with numbers in this row... Got it!")
            return []


def get_puzzle() -> Puzzle:
    final_puzzle = [[-1 for _ in range(9)] for _ in range(9)]
    idxs = [[b for b in range(3 * a, 3 * a + 3)] for a in range(3)]

    for matr_row_nr in range(3):
        print(f"=== matrix row: {matr_row_nr + 1} ===\n")

        for matr_nr in range(3):
            print(f"= matrix: {matr_nr + 1} =\n")
            matr = []

            for row_nr, row_idx in enumerate(idxs[matr_row_nr], 1):
                row_vals = get_row_vals(idxs[matr_nr], row_nr)

                if not row_vals:
                    matr.append([-1 for _ in range(3)])
                else:
                    matr.append([x[0] for x in row_vals])

                row_vals = list(filter(lambda x: x[0] != -1, row_vals))

                for val, col_idx in row_vals:
                    final_puzzle[row_idx][col_idx] = val

            print_mat_str_repr(matr)

    return final_puzzle

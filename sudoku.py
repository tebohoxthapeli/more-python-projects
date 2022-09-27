from re import compile

Puzzle = list[list[int]]


def find_next_empty(puzzle: Puzzle) -> tuple:
    # finds the next row, col in the puzzle that's not filled yet -> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return (r, c)
    return (None, None)  # if no spaces in the puzzle are empty (-1)


def is_valid(puzzle: Puzzle, guess: int, row: int, col: int) -> bool:
    # figures out whether the guess at the row,col of the puzzle is a valid guess
    # returns True if is valid, False otherwise

    # start with the row
    row_vals = puzzle[row]

    if guess in row_vals:
        return False

    # now the column
    col_vals = [puzzle[i][col] for i in range(9)]

    if guess in col_vals:
        return False

    # and then the square
    # we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/col

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if we get here, the guess is valid
    return True


def solve_sudoku(puzzle: Puzzle) -> tuple[bool, Puzzle]:
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1:

    if row is None:
        return (True, puzzle)

    # step 2: if there is a place to put a number, then make a guess between 1 and 9

    for guess in range(1, 10):
        # step 3: check if this is a valid guess

        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess

            # now recurse using this puzzle
            # step 4: recursively call our function

            is_solved = solve_sudoku(puzzle)

            if is_solved[0]:
                return is_solved

            # step 5: if not valid OR if our guess does not solve the puzzle, then we need to
            # backtrack and try a new number

            puzzle[row][col] = -1  # reset the guess

        # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE

    return (False, [])


def print_mat_str_repr(matrix: Puzzle) -> None:
    str_mat: list[list[str]] = []

    for r in range(3):
        new_row = []

        for c in range(3):
            val = str(matrix[r][c])

            if val == "-1":
                val = ""

            new_row.append(val.center(3))

        str_mat.append(new_row)

    str_repr = ""

    for r in str_mat:
        str_repr += f"\n|{'|'.join(r)}|"

    print(str_repr)


def get_str_repr(puzzle: Puzzle) -> str:
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

    return str_repr


def get_instructions() -> None:
    print("Instructions:\n")
    print(
        "When prompted: 'matrix: {m}, row: {r}', enter the column indices (1-3) with blocks that have numbers in them in that matrix and row."
    )
    print("Your input should be in the format: 'x.y.z'.")
    print("Note: All indices are optional as blocks can be empty.")
    print(
        "If all blocks in that row are empty, just press the <enter> key on your keyboard."
    )
    print(
        "Then for each block with a number, enter that number as shown in your Sudoku puzzle."
    )
    print("Enter 'q' to quit.\n")


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

            print(
                "User input error: Invalid input entered. Please read the instructions and try again.\n"
            )
            get_instructions()
        else:
            return []


def get_puzzle() -> Puzzle:
    final_puzzle = [[-1 for _ in range(9)] for _ in range(9)]
    idxs = [[b for b in range(3 * a, 3 * a + 3)] for a in range(3)]

    for matr_row_nr in range(3):
        print(f"\n=== matrix row: {matr_row_nr + 1} ===")
        for matr_nr in range(3):
            print(f"\n= matrix: {matr_nr + 1} =\n")

            for row_nr, row_idx in enumerate(idxs[matr_row_nr], 1):
                for val, col_idx in get_row_vals(idxs[matr_nr], row_nr):
                    final_puzzle[row_idx][col_idx] = val

    return final_puzzle


def main():
    print("\nSUDOKU SOLVER:")

    is_solved, solved_puzzle = solve_sudoku(get_puzzle())

    print(f"\nIs the Sudoku puzzle solvable?: {is_solved}")

    if is_solved:
        print("\nSolved puzzle:")
        print(get_str_repr(solved_puzzle))


if __name__ == "__main__":
    main()

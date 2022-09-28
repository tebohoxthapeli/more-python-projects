from input_collection import Puzzle

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

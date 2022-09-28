from instructions import get_instructions
from input_collection import get_puzzle
from logic import solve_sudoku
from formatters import print_puzzle_str_repr


def main():
    print("\nSUDOKU SOLVER:")
    get_instructions()

    is_solved, solved_puzzle = solve_sudoku(get_puzzle())

    print(f"\nIs the Sudoku puzzle solvable?: {is_solved}")

    if is_solved:
        print("\nSolved puzzle:")
        print_puzzle_str_repr(solved_puzzle)


if __name__ == "__main__":
    main()

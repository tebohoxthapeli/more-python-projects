def get_instructions() -> None:
    print("\n\nInstructions:\n")
    print(
        "When prompted: 'row: {r} ->', enter its block numbers (1-9) as shown in your Sudoku puzzle."
    )
    print(
        "Your input should be in the format: '123', where each number corresponds with a block in that row of the 3x3 submatrix."
    )
    print("Note: Each number is optional as blocks can be empty.")
    print("An empty block is represented by a period (eg. '.12').")
    print(
        "Empty blocks AFTER the last number do not have to be included (eg. '.1' or '1')."
    )
    print("The program knows that the 2 inputs above should be '.1.' and '1..'")
    print(
        "If all blocks in that row are empty, simply press the <enter> key on your keyboard."
    )
    print("But '...', '..' and '.' should work as well.")
    print("Enter 'q' to quit at any point.\n\n")
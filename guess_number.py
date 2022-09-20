from random import randint


def user_guess(x: int):
    tries = 0
    rand_num = randint(1, x)

    while True:
        tries += 1
        guess = int(input(f"\nGuess a number between 1 and {x}: "))

        if guess < rand_num:
            print("Sorry. Too low. Guess again.")
        elif guess > rand_num:
            print("Sorry. Too high. Guess again.")
        elif guess == rand_num:
            print(
                f"You guessed {rand_num} correctly after {tries} {'try' if tries == 1 else 'tries'}."
            )
            break


def computer_guess(hi: int):
    tries = 0
    lo = 1
    guess = lo

    while True:
        tries += 1

        if lo == hi:
            guess = lo
            break

        guess = randint(lo, hi)

        feedback = (
            input(f"\nIs {guess} too high (H), too low (L) or correct (C)?: ")
            .lower()
            .strip()
        )

        if feedback == "h" and guess > 1:
            hi = guess - 1
        elif feedback == "l":
            lo = guess + 1
        elif feedback == "c":
            break
        else:
            tries -= 1
            print(
                "Error: Invalid feedback provided. Only H, L and C are allowed. And remember that no number can be lower than 1."
            )

    print(
        f"\nThe computer says: 'I have determined that the correct number is {guess} after {tries} {'try' if tries == 1 else 'tries'}'"
    )


def main():
    mode = input(
        "\nDo you want to guess? (y/n) 'n' will make the computer guess instead: "
    )

    if mode.lower() == "y":
        user_guess(1000)
    else:
        computer_guess(1000)


if __name__ == "__main__":
    main()

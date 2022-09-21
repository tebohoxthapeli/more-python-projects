from words import words
from random import choice
from re import compile, IGNORECASE
from string import ascii_uppercase


def get_valid_word() -> str:
    regex = r"[\- ]"
    pattern = compile(regex)

    while True:
        word = choice(words)

        if not pattern.search(word):
            return word.upper()


def get_user_letter() -> str:
    regex = f"^[{ascii_uppercase}]$"
    pattern = compile(regex, IGNORECASE)

    while True:
        letter = input("\nGuess a letter: ")

        if pattern.search(letter):
            return letter.upper()

        print("Invalid input. Try again.")


def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"\n{lives} lives left")

        if len(used_letters):
            print(f"Letters used so far: {' '.join(used_letters)}")

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(f"Current word: {' '.join(word_list)} ({len(word)} characters)")

        user_letter = get_user_letter()

        if user_letter in alphabet.difference(used_letters):
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"{user_letter} is not in the word.")
        else:
            print("You have already used that character. Please try again.")

    print()

    if not lives:
        print(f"You have run out of lives. The word you were looking for is {word}")
    else:
        print(f"The word is {word}. Good job!")


def main():
    hangman()


if __name__ == "__main__":
    main()

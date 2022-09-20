from random import choice
from game import TicTacToe


class Player:
    def __init__(self, letter: str):
        self.letter = letter.lower()


class Computer(Player):
    def get_move(self, game: TicTacToe):
        return choice(game.available_moves())


class Human(Player):
    def get_move(self, game: TicTacToe):
        valid_square = False
        val = None

        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")
            print()

            # we're going to check that this is a correct value by trying to cast it to an integer, and if it's
            # not, then we say it's invalid
            # if that spot is not available on the board,
            # we also say it's invalid

            try:
                val = int(square)

                if val not in game.available_moves():
                    raise ValueError

                # if these are successful
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")

        return val

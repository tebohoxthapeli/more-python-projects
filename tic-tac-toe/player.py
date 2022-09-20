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
        while True:
            try:
                square = int(input(f"\n{self.letter}'s turn. Input move (0-8): "))

                # check if the move hasn't been made yet
                if square not in game.available_moves():
                    raise ValueError

                return square
            except ValueError:
                print("Invalid square. Try again.")

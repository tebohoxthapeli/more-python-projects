from Player import Player
from TicTacToe import TicTacToe


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

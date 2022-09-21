from Player import Player
from TicTacToe import TicTacToe
from random import choice


class NormalComputer(Player):
    def get_move(self, game: TicTacToe):
        return choice(game.available_moves())

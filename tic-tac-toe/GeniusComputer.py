from Player import Player
from TicTacToe import TicTacToe
from random import choice
from math import inf


class GeniusComputer(Player):
    def __init__(self, letter: str):
        super().__init__(letter)

    def minimax(self, state: TicTacToe, player: str):
        # yourself
        max_player = self.letter

        other_player = "o" if player == "x" else "x"

        # first, we want to check if the previous move is a
        # winner
        # this is our base case

        if state.current_winner == other_player:
            # we should return position and score because we
            # need to keep track of the score for minimax to
            # work

            return {
                "position": None,
                "score": 1 * (state.num_empty_squares() + 1)
                if other_player == max_player
                else -1 * (state.num_empty_squares() + 1),
            }
        elif not state.empty_squares():
            return {"position": None, "score": 0}

        # initialise some dictionaries

        if player == max_player:
            # each score should maximise (be larger)
            best = {"position": None, "score": -inf}
        else:
            # each score should minimise
            best = {"position": None, "score": inf}

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after making that move
            # now, alternate players
            sim_score = self.minimax(state, other_player)

            # step 3: undo the move
            state.board[possible_move] = " "
            state.current_winner = None

            # otherwise this will get messed up from the recursion part
            sim_score["position"] = possible_move

            # step 4: update the dictionaries if necessary
            # we are trying to maximise the max_player
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    # replace best
                    best = sim_score
            # but minimise the other player
            else:
                if sim_score["score"] < best["score"]:
                    # replace best
                    best = sim_score
        return best

    def get_move(self, game: TicTacToe):
        if len(game.available_moves()) == 9:
            # randomly choose one
            return choice(game.available_moves())
        else:
            # get the square based off the minimax algorithm
            return self.minimax(game, self.letter)["position"]

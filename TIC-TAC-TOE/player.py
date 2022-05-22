import math
import random
# import game


class Player:
    def __init__(self,letter):
        # X or O letter
        self.letter = letter
    
    def get_move(self,game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter +'\'s turn. Input moves (0-9):')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, Try another")
        return val

class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())

        else:
            #get the square based on the minimax algoritham
            square= self.minimax(game, self.letter)['position'] 
        return square

    def minimax(self, state, player):
        max_player = self.letter  #you
        other_player = 'O'  if player == "X" else "X" # the other player

        if state.current_winner == other_player:
            return { 'position': None,
                    'score': 1 * (state.num_empty_squares() +1) if other_player == max_player else -1 * ( state.num_empty_squares()+ 1)
                   
                    }

        elif not state.empty_squares():
            return {'position': None , 'score': 0 }
        
        #initialize some dictanry

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score would maximize
        else:
            best = {"position": None, 'score': math.inf } # math.inf

        for possible_move in state.available_moves():
            #step-1: return a move, try that spot
            state.make_move(possible_move, player)
            #step-2: recurse using minmax a game after making that move
            sim_score = self.minimax(state, other_player) # now we alternate the players
            #step3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move #otherwise this will get messed up from

            #state 4 : update the dictonaries
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best =  sim_score # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
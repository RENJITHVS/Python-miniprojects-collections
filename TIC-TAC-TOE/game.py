from player import *
import time

class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] # to represent 3*3 matrix
        self.current_winner = None # Track the Winner

    def print_board(self):
        # getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_num():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')

    def available_moves(self):
        return [i for i,x in enumerate(self.board) if x == ' ']

    def empty_squares(self):
        return " " in self.board

    def non_empty_squares(self):
        # return len(self.available_move)
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid moves make move otherwise return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False

    def winner(self, square , letter):
        #winner of 3 in a row anywhere ... we have to check all these !
        # first let's check the row
        row_ind = square //3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check coloumn 
        col_ind = square % 3
        coloumn = [self.board[col_ind + i *3] for i in range(3)]
        if all([spot == letter for spot in coloumn]):
            return True

        #check across diagnal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagoanl
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left diagoanl
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play( game, x_player, o_player, print_game= True):
    #return the winner of the game! or None for tie
    if print_game:
        game.print_board_num()

    letter =  "X" # consider it as a starting letter

    while game.empty_squares():

        
        #get move from approproate player
        if letter == "O":
            square = o_player.get_move(game)  
        else:
            square = x_player.get_move(game)
            
        #let define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f"make a move to square {square}")
                game.print_board()
                print(" ")

            if game.current_winner:
                if print_game:
                    print(letter + "wins!")
                return letter

            #after we made our move, we need to alternative letters
            letter = 'O' if letter == 'X' else 'X' #switch players

        time.sleep(1)

    if print_game:
        print('It is a tie')


if __name__ =='__main__':
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game= True)
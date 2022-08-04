class Board:

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    
   

    def update_board(self, move, player):

        dictionary = {
        'A': 0,
        'B': 1,
        'C': 2
        }

        self.board[int(move[1]) - 1][dictionary[move[0]]] = player 

    def print_board(self):
        print('    A    B    C')
        print(f'1 {self.board[0]}')
        print(f'2 {self.board[1]}')
        print(f'3 {self.board[2]}')
        print('')

    def check_win(self):
        if ((self.board[0][0] == self.board[0][1] == self.board[0][2] != ' ')
            or (self.board[1][0] == self.board[1][1] == self.board[1][2] != ' ')
            or (self.board[2][0] == self.board[2][1] == self.board[2][2] != ' ')
            or (self.board[0][0] == self.board[1][0] == self.board[2][0] != ' ')
            or (self.board[0][1] == self.board[1][1] == self.board[2][1] != ' ')
            or (self.board[0][2] == self.board[1][2] == self.board[2][2] != ' ')
            or (self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ')
            or (self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ')):
            return True
        else: return False

        




class Player:
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        if self.name == 'O':
            name = 'Player1'
        elif self.name == 'X':
            name = 'Player2'

        move = list(input(f'{name} enter your move: ').upper())
        return move





def main():
    board = Board()
    board.print_board()
    player1 = Player('O')
    player2 = Player('X')
    which_player = 1
    is_there_winner = False

    while is_there_winner == False:
        
        if which_player == 1:
            player = player1
        elif which_player == -1:
            player = player2
        
        move = player.move()
        board.update_board(move, player.name)
        board.print_board()

        is_there_winner = board.check_win()
        which_player = which_player * -1


    if player == player1:
        print('Player1 Wins!')
    else: print('Player2 Wins!')



main()

    



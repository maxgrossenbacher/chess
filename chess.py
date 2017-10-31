import numpy as np

class Chess():
    def __init__(self, player1='User1', player2='User2', load_game=[]):
        self.board = self._initialize_board()
        self.white=player1
        self.black=player2
        self.whose_move=None
        self.moves = load_game
        self.bl_pieces_dict = {'R':'\u2656', 'N':'\u2658', 'B':'\u2657', 'Q':'\u2655', 'K':'\u2654', 'p':'\u2659'}
        self.wh_pieces_dict = {'R':'\u265C', 'N':'\u265E', 'B':'\u265D', 'Q':'\u265B', 'K':'\u265A', 'p':'\u265F'}
        self.row = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        self.col = {'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}
        self.is_winner = False

    def make_move(self):
        while self.is_winner == False:
            print(self.board)
            self._check_move()
            print('please input piece code : currentlocal - newlocal')
            user_move = input('> ')
            if user_move == 'pause' or 'exit':
                break
            self.moves.append(user_move.split(':'))
            self._update_board()




    def _update_board(self):
        if self.whose_move == self.white and self.moves[-1][0] in self.wh_pieces_dict:
            piece = self.wh_pieces_dict[self.moves[-1][0]]
            #current location
            currentlocal = list(self.moves[-1][1].split('-')[0])
            row_currentlocal = str(currentlocal[0])
            col_currentlocal = str(currentlocal[1])
            #new location
            newlocal = list(self.moves[-1][1].split('-')[1])
            row_newlocal = str(newlocal[0])
            col_newlocal = str(newlocal[1])

            if row_currentlocal in self.row and col_currentlocal in self.col and row_newlocal in self.row and col_newlocal in self.col:
                self.board[self.col[col_currentlocal]][self.row[row_currentlocal]] = '.'
                self.board[self.col[col_newlocal]][self.row[row_newlocal]] = piece
            else:
                print('not a valid move...try again')
                del self.moves[-1]

        elif self.whose_move == self.black and self.moves[-1][0] in self.bl_pieces_dict:
            piece = self.bl_pieces_dict[self.moves[-1][0]]
            #current location
            currentlocal = list(self.moves[-1][1].split('-')[0])
            row_currentlocal = currentlocal[0]
            col_currentlocal = currentlocal[1]
            #new location
            newlocal = list(self.moves[-1][1].split('-')[1])
            row_newlocal = newlocal[0]
            col_newlocal = newlocal[1]

            if row_currentlocal in self.row and col_currentlocal in self.col and row_newlocal in self.row and col_newlocal in self.col:
                self.board[self.col[col_currentlocal]][self.row[row_currentlocal]] = '.'
                self.board[self.col[col_newlocal]][self.row[row_newlocal]] = piece
            else:
                print('not a valid move...try again')
                del self.moves[-1]

        else:
            print('not a piece move...try again')
            del self.moves[-1]


    def _check_move(self):
        if len(self.moves) == 0:
            print('lets play!')
            print('White moves first, ' + self.white +' make your move!')
            self.whose_move = self.white
        elif len(self.moves) % 2 != 0:
            print('Black move, ' + self.black + ' make your move!')
            self.whose_move = self.black
        elif len(self.moves) % 2 == 0:
            print('White move, ' + self.white + ' make your move!')
            self.whose_move = self.white
        return



    def _initialize_board(self):
        board = np.array([['\u2656','\u2658','\u2657','\u2655','\u2654','\u2657','\u2658','\u2656'],\
                        ['\u2659' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['\u265F' for x in range(8)],\
                        ['\u265C','\u265E','\u265D','\u265B','\u265A','\u265D','\u265E','\u265C']])
        return board

if __name__ == '__main__':
    game = Chess(player1='Max')
    game.make_move()

import numpy as np
import time


class Chess():
    def __init__(self, player1='User1', player2='User2'):

        '''
        This class is a Proof of concept:

        * building a board
        * use unicode to represent each piece
        * using chess notation to move around the board
        * Keep track on whose turn
        * Keep track on moves
        * keep score based on value of each piece
        * watch and load games
        * undo functionality to go back a move
        '''

        self.board = self._initialize_board()
        self.white=player1
        self.black=player2
        self.whose_move=None
        self.moves = []
        self.bl_pieces_dict = {'R':'\u2656', 'N':'\u2658', 'B':'\u2657', 'Q':'\u2655', 'K':'\u2654', 'p':'\u2659'}
        self.wh_pieces_dict = {'R':'\u265C', 'N':'\u265E', 'B':'\u265D', 'Q':'\u265B', 'K':'\u265A', 'p':'\u265F'}
        self.row = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        self.col = {'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}
        self.is_winner = False
        self.wh_points=0
        self.bl_points=0
        self.points_dict={'R':5,'N':3,'B':3,'Q':9,'K':10000,'p':1}

    def play(self, load_game=False, watch=False, time_btw_moves=1):
        if load_game:
            for move in load_game:
                if watch:
                    print(self.board)
                    time.sleep(time_btw_moves)
                self._check_move()
                self.moves.append(move)
                self._update_board(move)
                self.score()

        while self.is_winner == False:
            print(self.board)
            self._check_move()
            print("please input > 'piece code':'currentlocal'-'newlocal'")
            user_move = input('> ')
            if user_move in ('pause', 'exit'):
                break
            self.moves.append(user_move.split(':'))
            self._update_board(user_move.split(':'))
            self.score()
            print('\n')

    def score(self):
        print(self.white + ' points = ',self.wh_points)
        print(self.black + ' points = ',self.bl_points)

    def undo(self, watch=False):
        del self.moves[-1]
        undoing_move = self.moves
        print('Someone clearly just messed up...')
        self.board = self._initialize_board()
        self.moves=[]
        self.wh_points = 0
        self.bl_points = 0
        self.play(undoing_move, watch)



    def _update_board(self, move):
        if self.whose_move == self.white and move[0] in self.wh_pieces_dict:
            piece = self.wh_pieces_dict[move[0]]
            #current location
            currentlocal = list(move[1].split('-')[0])
            if len(currentlocal) == 2:
                row_currentlocal = str(currentlocal[0])
                col_currentlocal = str(currentlocal[1])
                #new location
            newlocal = list(move[1].split('-')[1])
            if len(newlocal) == 2:
                row_newlocal = str(newlocal[0])
                col_newlocal = str(newlocal[1])

            if row_currentlocal in self.row and col_currentlocal in self.col and row_newlocal in self.row and col_newlocal in self.col:
                if self.board[self.col[col_newlocal]][self.row[row_newlocal]] in self.wh_pieces_dict.values():
                    print(self.whose_move + ' already have a piece here')
                    del self.moves[-1]
                elif self.board[self.col[col_newlocal]][self.row[row_newlocal]] in self.bl_pieces_dict.values():
                    taken_piece = self.board[self.col[col_newlocal]][self.row[row_newlocal]]
                    self.board[self.col[col_currentlocal]][self.row[row_currentlocal]] = '.'
                    self.board[self.col[col_newlocal]][self.row[row_newlocal]] = piece
                    print ('aw snap! '+self.whose_move + ' just took a piece.')
                    for code, pc in self.bl_pieces_dict.items():
                        if pc == taken_piece:
                            self.wh_points += self.points_dict[code]
                else:
                    self.board[self.col[col_currentlocal]][self.row[row_currentlocal]] = '.'
                    self.board[self.col[col_newlocal]][self.row[row_newlocal]] = piece

            else:
                print('not a valid move...try again')
                print('An example valid move is p:d2-d4')
                del self.moves[-1]

        elif self.whose_move == self.black and move[0] in self.bl_pieces_dict:
            piece = self.bl_pieces_dict[self.moves[-1][0]]
            #current location
            currentlocal = list(move[1].split('-')[0])
            if len(currentlocal) == 2:
                row_currentlocal = currentlocal[0]
                col_currentlocal = currentlocal[1]
            #new location
            newlocal = list(move[1].split('-')[1])
            if len(currentlocal) == 2:
                row_newlocal = newlocal[0]
                col_newlocal = newlocal[1]

            if row_currentlocal in self.row and col_currentlocal in self.col and row_newlocal in self.row and col_newlocal in self.col:
                if self.board[self.col[col_newlocal]][self.row[row_newlocal]] in self.bl_pieces_dict.values():
                    print(self.whose_move + ' already have a piece here')
                    del self.moves[-1]
                elif self.board[self.col[col_newlocal]][self.row[row_newlocal]] in self.wh_pieces_dict.values():
                    taken_piece = self.board[self.col[col_newlocal]][self.row[row_newlocal]]
                    self.board[self.col[col_currentlocal]][self.row[row_currentlocal]] = '.'
                    self.board[self.col[col_newlocal]][self.row[row_newlocal]] = piece
                    print ('aw snap! '+self.whose_move + ' just took a piece.')
                    for code, pc in self.wh_pieces_dict.items():
                        if pc == taken_piece:
                            self.bl_points += self.points_dict[code]
                else:
                    self.board[self.col[col_currentlocal]][self.row[row_currentlocal]] = '.'
                    self.board[self.col[col_newlocal]][self.row[row_newlocal]] = piece
        else:
            print('not a valid piece...try again.')
            print('valid pieces: p=pawn, R=rook, N=knight, B=bishop, Q=queen, K=king')
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
    Garry_Kasparov_v_Veselin_Topalov =[['p','e2-e4'], ['p', 'd7-d6'], ['p', 'd2-d4'], ['N','g8-f6'], ['N', 'b1-c3'], ['p', 'g7-g6'], ['B', 'c1-e3'], ['B', 'f8-g7'], \
    ['Q','d1-d2'], ['p','c7-c6'], ['p', 'f2-f3'], ['p', 'b7-b5'], ['N', 'g1-e2'], ['N', 'b8-d7'], ['B', 'e3-h6'], ['B', 'g7-h6'], ['Q', 'd2-h6'], ['B', 'c8-b7'], ['p', 'a2-a3'], ['p','e7-e5']]
    # 11.O-O-OQe712.Kb1a613.Nc1O-O-O14.Nb3exd415.Rxd4c516.Rd1Nb617.g3Kb818.Na5Ba819.Bh3d520.Qf4+Ka721.Rhe1d422.Nd5Nbxd523.exd5Qd624.Rxd4cxd425.Re7+Kb626.Qxd4+Kxa527.b4+Ka428.Qc3Qxd529.Ra7Bb730.Rxb7Qc431.Qxf6Kxa332.Qxa6+Kxb433.c3+Kxc334.Qa1+Kd235.Qb2+Kd136.Bf1Rd237.Rd7Rxd738.Bxc4bxc439.Qxh8Rd340.Qa8c341.Qa4+Ke142.f4f543.Kc1Rd244.Qa71-0

    game = Chess(player1='Max')
    game.play()

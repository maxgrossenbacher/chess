from piece import Pawn, Knight, Bishop, Rook, Queen, King
import numpy as np

class ChessBoard():
    def __init__(self, player1='User1', player2='Computer'):
        self.wh_pieces_dict = {}
        self.bl_pieces_dict = {}
        self.white=player1
        self.black=player2
        self.board = self._initialize_board()
        self.whose_move=self.white
        self.row_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        self.col_dict = {'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}
        self.game_moves = []
        self.is_winner = False

    def play(self):
        while self.is_winner == False:
            print(self.board)
            self._check_move()
            user_move = input('> ')
            if user_move in ('exit', 'pause'):
                break
            if len(user_move) == 2:
                p = 'p'
                move = user_move
                self.game_moves((p, move))
            else:
                p = user_move[0]
                move = user_move[1:]
                self.game_moves((p, move))

    def score(self):
        print(self.white + ' points = ',self.wh_points)
        print(self.black + ' points = ',self.bl_points)

    def _check_move(self):
        if len(self.game_moves) == 0:
            print('lets play!')
            print('White moves first, ' + self.white +' make your move!')
            self.whose_move = self.white
        elif len(self.game_moves) % 2 != 0:
            print('Black move, ' + self.black + ' make your move!')
            self.whose_move = self.black
        elif len(self.game_moves) % 2 == 0:
            print('White move, ' + self.white + ' make your move!')
            self.whose_move = self.white

    def _update_board(self):
        return


    def _assess_board(self):
        return

    def _initialize_board(self):
        # create white pieces
        p0 = Pawn(color='white', location=(0,6))
        self.wh_pieces_dict['p0'] = p0
        p1 = Pawn(color='white', location=(1,6))
        self.wh_pieces_dict['p1'] = p1
        p2 = Pawn(color='white', location=(2,6))
        self.wh_pieces_dict['p2'] = p2
        p3 = Pawn(color='white', location=(3,6))
        self.wh_pieces_dict['p3'] = p3
        p4 = Pawn(color='white', location=(4,6))
        self.wh_pieces_dict['p4'] = p4
        p5 = Pawn(color='white', location=(5,6))
        self.wh_pieces_dict['p5'] = p5
        p6 = Pawn(color='white', location=(6,6))
        self.wh_pieces_dict['p6'] = p6
        p7 = Pawn(color='white', location=(7,6))
        self.wh_pieces_dict['p7'] = p7
        N1 = Knight(color='white', location=(1,7))
        self.wh_pieces_dict['N1'] = N1
        N2 = Knight(color='white', location=(6,7))
        self.wh_pieces_dict['N2'] = N2
        B1 = Bishop(color='white', location=(2,7))
        self.wh_pieces_dict['B1'] = B1
        B2 = Bishop(color='white', location=(5,7))
        self.wh_pieces_dict['B2'] = B2
        R1 = Rook(color='white', location=(0,7))
        self.wh_pieces_dict['R1'] = R1
        R2 = Rook(color='white', location=(7,7))
        self.wh_pieces_dict['R2'] = R2
        Q = Queen(color='white', location=(3,7))
        self.wh_pieces_dict['Q'] = Q
        K = King(color='white', location=(4,7))
        self.wh_pieces_dict['K'] = K

        # create black pieces
        p0 = Pawn(color='black', location=(0,1))
        self.bl_pieces_dict['p0'] = p0
        p1 = Pawn(color='black', location=(1,1))
        self.bl_pieces_dict['p1'] = p1
        p2 = Pawn(color='black', location=(2,1))
        self.bl_pieces_dict['p2'] = p2
        p3 = Pawn(color='black', location=(3,1))
        self.bl_pieces_dict['p3'] = p3
        p4 = Pawn(color='black', location=(4,1))
        self.bl_pieces_dict['p4'] = p4
        p5 = Pawn(color='black', location=(5,1))
        self.bl_pieces_dict['p5'] = p5
        p6 = Pawn(color='black', location=(6,1))
        self.bl_pieces_dict['p6'] = p6
        p7 = Pawn(color='black', location=(7,1))
        self.bl_pieces_dict['p7'] = p7
        N1 = Knight(color='black', location=(1,0))
        self.bl_pieces_dict['N1'] = N1
        N2 = Knight(color='black', location=(6,0))
        self.bl_pieces_dict['N2'] = N2
        B1 = Bishop(color='black', location=(2,0))
        self.bl_pieces_dict['B1'] = B1
        B2 = Bishop(color='black', location=(5,0))
        self.bl_pieces_dict['B2'] = B2
        R1 = Rook(color='black', location=(0,0))
        self.bl_pieces_dict['R1'] = R1
        R2 = Rook(color='black', location=(7,0))
        self.bl_pieces_dict['R2'] = R2
        Q = Queen(color='black', location=(3,0))
        self.bl_pieces_dict['Q'] = Q
        K = King(color='black', location=(4,0))
        self.bl_pieces_dict['K'] = K

        board = np.array([['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)]])
        for piece in self.wh_pieces_dict.values():
            board[piece.row][piece.col] = piece
        for piece in self.bl_pieces_dict.values():
            board[piece.row][piece.col] = piece
        return board

if __name__ == '__main__':
    game = ChessBoard(player1='Max')
    game.play()

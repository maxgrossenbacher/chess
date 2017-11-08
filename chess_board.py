from piece import Pawn, Knight, Bishop, Rook, Queen, King
import numpy as np

class ChessBoard():
    def __init__(self, player1='User1', player2='Computer'):
        print('Version 1.0.1')
        self.wh_pieces_dict = {}
        self.bl_pieces_dict = {}
        self.white=player1
        self.black=player2
        self.board = self._initialize_game()
        self.whose_move=self.white
        self.col_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        self.row_dict = {'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}
        self.game_moves = []
        self.wh_points = 0
        self.bl_points = 0
        self.is_winner = False
        self.possible_captures = []
        self.cant_move_here = []

    def play(self):
        while self.is_winner == False:
            print(self.show_board())
            self._check_move()
            user_move = input('> ')
            if user_move in ('exit', 'pause'):
                break
            p = user_move[:2]
            move = user_move[2:]
            self._update_board(p, move)

    def score(self):
        print(self.white + ' points = ',self.wh_points)
        print(self.black + ' points = ',self.bl_points)

    def show_board(self, show_unicode=True):
        board = np.array([['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)],\
                        ['.' for x in range(8)]], dtype='U2')
        for key, piece in self.wh_pieces_dict.items():
            if show_unicode:
                board[piece.row][piece.col] = piece
            else:
                board[piece.row][piece.col] = key
        for key, piece in self.bl_pieces_dict.items():
            if show_unicode:
                board[piece.row][piece.col] = piece
            else:
                board[piece.row][piece.col] = key
        return board

    def _update_board(self, piece , move):
        move = (self.col_dict[move[0]], self.row_dict[move[1]])
        self.possible_captures = []
        self.cant_move_here = []
        self._assess_board(self.whose_move, self.wh_pieces_dict, self.bl_pieces_dict)
        p, loc = zip(*self.cant_move_here)
        if move not in loc:
            if self.whose_move == self.white:
                if piece in self.wh_pieces_dict.keys():
                    self.wh_pieces_dict[piece].move(move)
                    if move in self.wh_pieces_dict[piece].valid_moves:
                        self.game_moves.append((piece, move))
                        for other_p, other_loc in self.possible_captures:
                            if move == other_loc:
                                print ('aw snap! '+self.whose_move + ' just took a piece.')
                                self.wh_points += other_p.value
                                self.score()
                                for bkey, bl_piece in self.bl_pieces_dict.copy().items():
                                    if other_p == bl_piece:
                                        del self.bl_pieces_dict[bkey]
                else:
                    print(piece+' is not a valid piece or has been captured.')
                    print(self.show_board(show_unicode=False))

            if self.whose_move == self.black:
                if piece in self.bl_pieces_dict.keys():
                    self.bl_pieces_dict[piece].move(move)
                    if move in self.bl_pieces_dict[piece].valid_moves:
                        self.game_moves.append((piece, move))
                        for other_p, other_loc in self.possible_captures:
                            if move == other_loc:
                                print ('aw snap! '+self.whose_move + ' just took a piece.')
                                self.bl_points += other_p.value
                                self.score()
                                for wkey, wh_piece in self.wh_pieces_dict.copy().items():
                                    if other_p == wh_piece:
                                        del self.wh_pieces_dict[wkey]
                else:
                    print(piece+' is not a valid piece or has been captured.')
                    print(self.show_board(show_unicode=False))
        else:
            print(self.whose_move+' already has a piece on that space!')

    def _assess_board(self, player, wh_pieces_dict, bl_pieces_dict):
        wh_occupied_spaces = []
        bl_occupied_spaces = []
        for p in self.wh_pieces_dict.values():
            wh_occupied_spaces.append((p, p.location))
        for p in self.bl_pieces_dict.values():
            bl_occupied_spaces.append((p, p.location))
        if player == self.white:
            self.possible_captures = bl_occupied_spaces
            self.cant_move_here = wh_occupied_spaces
        elif player == self.black:
            self.possible_captures = wh_occupied_spaces
            self.cant_move_here = bl_occupied_spaces

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

    def _initialize_game(self):
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
        Q1 = Queen(color='white', location=(3,7))
        self.wh_pieces_dict['Q1'] = Q1
        K1 = King(color='white', location=(4,7))
        self.wh_pieces_dict['K1'] = K1

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
        Q1 = Queen(color='black', location=(3,0))
        self.bl_pieces_dict['Q1'] = Q1
        K1 = King(color='black', location=(4,0))
        self.bl_pieces_dict['K1'] = K1
        return self.show_board()

if __name__ == '__main__':
    game = ChessBoard(player1='Max')
    game.play()

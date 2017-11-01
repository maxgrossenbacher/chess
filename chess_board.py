from piece import Pawn, Knight, Bishop, Rook, Queen, King
import numpy as np

class ChessBoard():
    def __init__(self):
        self.board = self._initialize_board()
        self.wh_pieces_dict = {}
        self.bl_pieces_dict = {}

    def _initialize_board(self):
        # create white pieces
        p0 = Pawn(color='white', location=(0,6))
        self.wh_pieces_dict[p0] = p0.location
        p1 = Pawn(color='white', location=(1,6))
        self.wh_pieces_dict[p1] = p1.location
        p2 = Pawn(color='white', location=(2,6))
        self.wh_pieces_dict[p2] = p2.location
        p3 = Pawn(color='white', location=(3,6))
        self.wh_pieces_dict[p3] = p3.location
        p4 = Pawn(color='white', location=(4,6))
        self.wh_pieces_dict[p4] = p4.location
        p5 = Pawn(color='white', location=(5,6))
        self.wh_pieces_dict[p5] = p5.location
        p6 = Pawn(color='white', location=(6,6))
        self.wh_pieces_dict[p6] = p6.location
        p7 = Pawn(color='white', location=(7,6))
        self.wh_pieces_dict[p7] = p7.location
        K1 = Knight(color='white', location=(1,7))
        self.wh_pieces_dict[K1] = K1.location
        K2 = Knight(color='white', location=(6,7))
        self.wh_pieces_dict[K2] = K2.location
        B1 = Bishop(color='white', location=(2,7))
        self.wh_pieces_dict[B1] = B1.location
        B2 = Bishop(color='white', location=(5,7))
        self.wh_pieces_dict[B2] = B2.location
        R1 = Rook(color='white', location=(0,7))
        self.wh_pieces_dict[R1] = R1.location
        R2 = Rook(color='white', location=(7,7))
        self.wh_pieces_dict[R2] = R2.location
        Q = Queen(color='white', location=(3,7))
        self.wh_pieces_dict[Q] = Q.location
        K = King(color='white', location=(4,7))
        self.wh_pieces_dict[K] = K.location

        # create black pieces
        p0 = Pawn(color='black', location=(0,1))
        self.bl_pieces_dict[p0] = p0.location
        p1 = Pawn(color='black', location=(1,1))
        self.bl_pieces_dict[p1] = p1.location
        p2 = Pawn(color='black', location=(2,1))
        self.bl_pieces_dict[p2] = p2.location
        p3 = Pawn(color='black', location=(3,1))
        self.bl_pieces_dict[p3] = p3.location
        p4 = Pawn(color='black', location=(4,1))
        self.bl_pieces_dict[p4] = p4.location
        p5 = Pawn(color='black', location=(5,1))
        self.bl_pieces_dict[p5] = p5.location
        p6 = Pawn(color='black', location=(6,1))
        self.bl_pieces_dict[p6] = p6.location
        p7 = Pawn(color='black', location=(7,1))
        self.bl_pieces_dict[p7] = p7.location
        K1 = Knight(color='black', location=(1,0))
        self.bl_pieces_dict[K1] = K1.location
        K2 = Knight(color='black', location=(6,0))
        self.bl_pieces_dict[K2] = K2.location
        B1 = Bishop(color='black', location=(2,0))
        self.bl_pieces_dict[B1] = B1.location
        B2 = Bishop(color='black', location=(5,0))
        self.bl_pieces_dict[B2] = B2.location
        R1 = Rook(color='black', location=(0,0))
        self.bl_pieces_dict[R1] = R1.location
        R2 = Rook(color='black', location=(7,0))
        self.bl_pieces_dict[R2] = R2.location
        Q = Queen(color='black', location=(3,0))
        self.bl_pieces_dict[Q] = Q.location
        K = King(color='black', location=(4,0))
        self.bl_pieces_dict[K] = K.location


        # board = np.array([['\u2656','\u2658','\u2657','\u2655','\u2654','\u2657','\u2658','\u2656'],\
        #                 ['\u2659' for x in range(8)],\
        #                 ['.' for x in range(8)],\
        #                 ['.' for x in range(8)],\
        #                 ['.' for x in range(8)],\
        #                 ['.' for x in range(8)],\
        #                 ['\u265F' for x in range(8)],\
        #                 ['\u265C','\u265E','\u265D','\u265B','\u265A','\u265D','\u265E','\u265C']])
        # return board

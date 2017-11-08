import numpy as np
import pandas as pd


class AI():
    def __init__(self, color):
        self.color = color
        self.possible_captures = []
        self.cant_move_here = []
        self.possible_moves = []


    def move(self):
        self._assess_moves()
        self._find_possible_moves()


    def _assess_board(self, player, wh_pieces_dict, bl_pieces_dict):
        wh_occupied_spaces = []
        bl_occupied_spaces = []
        for p in wh_pieces_dict.values():
            wh_occupied_spaces.append((p, p.value, p.location))
        for p in bl_pieces_dict.values():
            bl_occupied_spaces.append((p, p.value, p.location))
        if player == 'white':
            self.possible_captures = bl_occupied_spaces
            self.cant_move_here = wh_occupied_spaces
        elif player == 'black':
            self.possible_captures = wh_occupied_spaces
            self.cant_move_here = bl_occupied_spaces

    def _assess_moves(self):
        self._assess_board(self.color)
        if len(self.possible_captures) > 0:
            self.possible_captures.sort(key=lambda x: x[1])

    def _find_possible_moves(self, pieces_dict):
        for p in pieces_dict.values():
            p._possible_moves()

            self.possible_moves.append()

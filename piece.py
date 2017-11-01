import numpy as np


class Pawn():
    def __init__(self, color, location, value=1):
        self.color = color
        self.value = value
        self.location = list(location)
        self.col = int(location[0])
        self.row = int(location[1])
        self.moves = []
        self.valid_moves = []

    def __str__(self):
        if self.color == 'white':
            return '\u265F'
        if self.color == 'black':
            return '\u2659'

    def move(self, move):
        self.valid_moves = []
        self._capture_moves()
        self._non_capture_moves()
        if self._check_valid_move(move) == 'valid_move':
            self.moves.append(move)
            self.location = move
            self.col = move[0]
            self.row = move[1]
        else:
            print('Sorry, not a valid move...try again')

    def _non_capture_moves(self):
        if self.color == 'white':
            self.valid_moves.append([self.col, (self.row + 1)])
            if len(self.moves) == 0:
                self.valid_moves.append([self.col, (self.row + 2)])
        if self.color == 'black':
            self.valid_moves.append([self.col, (self.row - 1)])
            if len(self.moves) == 0:
                self.valid_moves.append([self.col, (self.row - 2)])

    def _capture_moves(self):
        if self.color == 'white':
            self.valid_moves.append([(self.col + 1), (self.row + 1)])
            self.valid_moves.append([(self.col - 1), (self.row + 1)])
        if self.color == 'black':
            self.valid_moves.append([str(self.col - 1), (self.row - 1)])
            self.valid_moves.append([(self.col + 1), (self.row - 1)])
        return

    def _check_valid_move(self, move):
        if move in self.valid_moves:
            return 'valid_move'
        else:
            return 'invalid move'



class Rook():
    def __init__(self, color, location, value=5):
        self.color = color
        self.value = value
        self.location = location
        self.col = self.location[0]
        self.row = self.location[1]
        self.moves = []
        self.castle = True
        self.valid_moves = []

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        if self._check_valid_move(move) == 'valid_move':
            self.moves.append(move)
            self.location = move
            self.col = move[0]
            self.row = move[1]
        else:
            print('Sorry, not a valid move...try again')

    def __str__(self):
        if self.color == 'white':
            return '\u265C'
        if self.color == 'black':
            return '\u2656'

    def _possible_moves(self):
        if len(self.moves) == 0:
            self.castle = True
        count = 1
        for _ in range(7):
            self.valid_moves.append([self.col, count])
            self.valid_moves.append([count, self.row])
            count+=1

    def _check_valid_move(self, move):
        if move in self.valid_moves:
            return 'valid_move'
        else:
            return 'invalid move'



class Bishop():
    def __init__(self, color, location, value=5):
        self.color = color
        self.value = value
        self.location = location
        self.col = self.location[0]
        self.row = self.location[1]
        self.moves = []
        self.castle = True
        self.valid_moves = []

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        if self._check_valid_move(move) == 'valid_move':
            self.moves.append(move)
            self.location = move
            self.col = move[0]
            self.row = move[1]
        else:
            print('Sorry, not a valid move...try again')


    def __str__(self):
        if self.color == 'white':
            return '\u265D'
        if self.color == 'black':
            return '\u2657'

    def _possible_moves(self):
        count = -7
        for _ in range(14):
            self.rl_row = self.row + count
            self.rl_col = self.col + count
            self.lr_row = self.row + count
            self.lr_col = self.col - count
            if self.rl_row >= 0 and self.rl_row <= 7 and self.rl_col >= 0 and self.rl_col <=7:
                self.valid_moves.append([self.rl_col, self.rl_row])
            if self.lr_row >= 0 and self.lr_row <= 7 and self.lr_col >= 0 and self.lr_col <=7:
                self.valid_moves.append([self.lr_col, self.lr_row])
            count+=1

    def _check_valid_move(self, move):
        if move in self.valid_moves:
            return 'valid_move'
        else:
            return 'invalid move'

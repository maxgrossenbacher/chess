import numpy as np


class Pawn():
    def __init__(self, color, location, value=1):
        self.color = color
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def __str__(self):
        if self.color == 'white':
            return '\u265F'
        if self.color == 'black':
            return '\u2659'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.location))

    def __eq__(self, other):
        return (self.color, self.location) == (other.color, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        if self.color == 'white':
            self.valid_moves.append((self.col, (self.row - 1)))
            if len(self.moves) == 0:
                self.valid_moves.append((self.col, (self.row - 2)))
            if self.can_capture == True:
                self.valid_moves.append(((self.col + 1), (self.row - 1)))
                self.valid_moves.append(((self.col - 1), (self.row - 1)))
        elif self.color == 'black':
            self.valid_moves.append((self.col, (self.row + 1)))
            if len(self.moves) == 0:
                self.valid_moves.append((self.col, (self.row + 2)))
            if self.can_capture == True:
                self.valid_moves.append(((self.col - 1), (self.row + 1)))
                self.valid_moves.append(((self.col + 1), (self.row + 1)))



class Bishop():
    def __init__(self, color, location, value=3):
        self.color = color
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def __str__(self):
        if self.color == 'white':
            return '\u265D'
        if self.color == 'black':
            return '\u2657'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.location))

    def __eq__(self, other):
        return (self.color, self.location) == (other.color, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        count = -7
        for _ in range(14):
            self.rl_row = self.row + count
            self.rl_col = self.col + count
            self.lr_row = self.row + count
            self.lr_col = self.col - count
            if self.rl_row >= 0 and self.rl_row <= 7 and self.rl_row != self.row and self.rl_col >= 0 and self.rl_col <=7 and self.rl_col != self.col:
                self.valid_moves.append((self.rl_col, self.rl_row))
            if self.lr_row >= 0 and self.lr_row <= 7 and self.lr_row != self.row and self.lr_col >= 0 and self.lr_col <=7 and self.lr_col != self.col:
                self.valid_moves.append((self.lr_col, self.lr_row))
            count+=1



class Knight():
    def __init__(self, color, location, value=3):
        self.color = color
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def __str__(self):
        if self.color == 'white':
            return '\u265E'
        if self.color == 'black':
            return '\u2658'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.location))

    def __eq__(self, other):
        return (self.color, self.location) == (other.color, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        possible_moves = [((self.col - 1), (self.row + 2)), ((self.col + 1), (self.row + 2)),\
                            ((self.col + 2), (self.row + 1)), ((self.col + 2), (self.row - 1)),\
                            ((self.col + 1), (self.row - 2)), ((self.col - 1), (self.row - 2)),\
                            ((self.col - 2), (self.row - 1)), ((self.col - 2), (self.row + 1))]
        for pm in possible_moves:
            c, r = pm
            if r >= 0 and r <= 7 and c >= 0 and c <=7:
                self.valid_moves.append((c, r))



class Rook():
    def __init__(self, color, location, value=5):
        self.color = color
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False
        self.castle = True

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def __str__(self):
        if self.color == 'white':
            return '\u265C'
        if self.color == 'black':
            return '\u2656'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.location))

    def __eq__(self, other):
        return (self.color, self.location) == (other.color, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        if len(self.moves) == 0:
            self.castle = True
        count = 0
        for _ in range(8):
            if (self.col, count) != self.location:
                self.valid_moves.append((self.col, count))
            if (count, self.row) != self.location:
                self.valid_moves.append((count, self.row))
            count+=1



class Queen():
    def __init__(self, color, location, value=9):
        self.color = color
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def __str__(self):
        if self.color == 'white':
            return '\u265D'
        if self.color == 'black':
            return '\u2657'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.location))

    def __eq__(self, other):
        return (self.color, self.location) == (other.color, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        count = -7
        for _ in range(14):
            self.rl_row = self.row + count
            self.rl_col = self.col + count
            self.lr_row = self.row + count
            self.lr_col = self.col - count
            if self.rl_row >= 0 and self.rl_row <= 7 and self.rl_row != self.row and self.rl_col >= 0 and self.rl_col <=7 and self.rl_col != self.col:
                self.valid_moves.append((self.rl_col, self.rl_row))
            if self.lr_row >= 0 and self.lr_row <= 7 and self.lr_row != self.row and self.lr_col >= 0 and self.lr_col <=7 and self.lr_col != self.col:
                self.valid_moves.append((self.lr_col, self.lr_row))
            count+=1
        count = 0
        for _ in range(8):
            if (self.col, count) != self.location:
                self.valid_moves.append((self.col, count))
            if (count, self.row) != self.location:
                self.valid_moves.append((count, self.row))
            count+=1


class King():
    def __init__(self, color, location, value=1000000):
        self.color = color
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False
        self.castle = True

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def __str__(self):
        if self.color == 'white':
            return '\u265E'
        if self.color == 'black':
            return '\u2658'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.location))

    def __eq__(self, other):
        return (self.color, self.location) == (other.color, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        if len(self.moves) == 0:
            self.castle = True
        possible_moves = [((self.col - 1), (self.row - 1)), ((self.col), (self.row - 1)),\
                            ((self.col + 1), (self.row - 1)), ((self.col + 1), (self.row)),\
                            ((self.col + 1), (self.row + 1)), ((self.col), (self.row + 1)),\
                            ((self.col - 1), (self.row + 1)), ((self.col - 1), (self.row))]
        for pm in possible_moves:
            c, r = pm
            if r >= 0 and r <= 7 and c >= 0 and c <=7:
                self.valid_moves.append((c, r))

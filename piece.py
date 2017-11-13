import numpy as np


class Pawn():
    def __init__(self, color, location, value=1):
        self.color = color
        self.name = 'p'
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False
        self.in_danger = False
        self.blocked = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        self._set_can_capture()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def _set_can_capture(self, capture=False):
        if capture:
            self.can_capture = True
        else:
            self.can_capture = False

    def __str__(self):
        if self.color == 'white':
            return '\u265F'
        if self.color == 'black':
            return '\u2659'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.value, self.name, self.location))

    def __eq__(self, other):
        return (self.color, self.value, self.name, self.location) == (other.color, other.value, other.name, other.location)

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
        self.name = 'B'
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False
        self.in_danger = False
        self.blocked = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        self._set_can_capture()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def _set_can_capture(self, capture=False):
        if capture:
            self.can_capture = True
        else:
            self.can_capture = False

    def __str__(self):
        if self.color == 'white':
            return '\u265D'
        if self.color == 'black':
            return '\u2657'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.value, self.name, self.location))

    def __eq__(self, other):
        return (self.color, self.value, self.name, self.location) == (other.color, other.value, other.name, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        count = 0
        for _ in range(8):
            self.rlp_row = self.row + count
            self.rlp_col = self.col + count
            self.rln_row = self.row - count
            self.rln_col = self.col - count
            self.lrp_row = self.row + count
            self.lrp_col = self.col - count
            self.lrn_row = self.row - count
            self.lrn_col = self.col + count
            if self.rlp_row >= 0 and self.rlp_row <= 7 and self.rlp_row != self.row and self.rlp_col >= 0 and self.rlp_col <=7 and self.rlp_col != self.col:
                self.valid_moves.append((self.rlp_col, self.rlp_row))
            if self.rln_row >= 0 and self.rln_row <= 7 and self.rln_row != self.row and self.rln_col >= 0 and self.rln_col <=7 and self.rln_col != self.col:
                self.valid_moves.append((self.rln_col, self.rln_row))
            if self.lrp_row >= 0 and self.lrp_row <= 7 and self.lrp_row != self.row and self.lrp_col >= 0 and self.lrp_col <=7 and self.lrp_col != self.col:
                self.valid_moves.append((self.lrp_col, self.lrp_row))
            if self.lrn_row >= 0 and self.lrn_row <= 7 and self.lrn_row != self.row and self.lrn_col >= 0 and self.lrn_col <=7 and self.lrn_col != self.col:
                self.valid_moves.append((self.lrn_col, self.lrn_row))
            count+=1



class Knight():
    def __init__(self, color, location, value=3):
        self.color = color
        self.name = 'N'
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False
        self.in_danger = False
        self.blocked = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        self._set_can_capture()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def _set_can_capture(self, capture=False):
        if capture:
            self.can_capture = True
        else:
            self.can_capture = False

    def __str__(self):
        if self.color == 'white':
            return '\u265E'
        if self.color == 'black':
            return '\u2658'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.value, self.name, self.location))

    def __eq__(self, other):
        return (self.color, self.value, self.name, self.location) == (other.color, other.value, other.name, other.location)

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
        self.name = 'R'
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False
        self.in_danger = False
        self.castle = True
        self.blocked = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        self._set_can_capture()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def _set_can_capture(self, capture=False):
        if capture:
            self.can_capture = True
        else:
            self.can_capture = False

    def __str__(self):
        if self.color == 'white':
            return '\u265C'
        if self.color == 'black':
            return '\u2656'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.value, self.name, self.location))

    def __eq__(self, other):
        return (self.color, self.value, self.name, self.location) == (other.color, other.value, other.name, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        if len(self.moves) == 0:
            self.castle = True
        else:
            self.castle = False
        count = 0
        for _ in range(8):
            if (self.col, self.row+count) != self.location and self.row+count >=0 and self.row+count <= 7:
                self.valid_moves.append((self.col, self.row+count))
            if (self.col, self.row-count) != self.location and self.row-count >=0 and self.row-count <= 7:
                self.valid_moves.append((self.col, self.row-count))
            if (self.col+count, self.row) != self.location and self.col+count >=0 and self.col+count <= 7:
                self.valid_moves.append((self.col+count, self.row))
            if (self.col-count, self.row) != self.location and self.col-count >=0 and self.col-count <= 7:
                self.valid_moves.append((self.col-count, self.row))
            count+=1



class Queen():
    def __init__(self, color, location, value=9):
        self.color = color
        self.name = 'Q'
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False
        self.in_danger = False
        self.blocked = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        self._set_can_capture()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def _set_can_capture(self, capture=False):
        if capture:
            self.can_capture = True
        else:
            self.can_capture = False

    def __str__(self):
        if self.color == 'white':
            return '\u265B'
        if self.color == 'black':
            return '\u2655'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.value, self.name, self.location))

    def __eq__(self, other):
        return (self.color, self.value, self.name, self.location) == (other.color, other.value, other.name, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        count = 0
        for _ in range(8):
            self.rlp_row = self.row + count
            self.rlp_col = self.col + count
            self.rln_row = self.row - count
            self.rln_col = self.col - count
            self.lrp_row = self.row + count
            self.lrp_col = self.col - count
            self.lrn_row = self.row - count
            self.lrn_col = self.col + count
            # move like a bishop
            if self.rlp_row >= 0 and self.rlp_row <= 7 and self.rlp_row != self.row and self.rlp_col >= 0 and self.rlp_col <=7 and self.rlp_col != self.col:
                self.valid_moves.append((self.rlp_col, self.rlp_row))
            if self.rln_row >= 0 and self.rln_row <= 7 and self.rln_row != self.row and self.rln_col >= 0 and self.rln_col <=7 and self.rln_col != self.col:
                self.valid_moves.append((self.rln_col, self.rln_row))
            if self.lrp_row >= 0 and self.lrp_row <= 7 and self.lrp_row != self.row and self.lrp_col >= 0 and self.lrp_col <=7 and self.lrp_col != self.col:
                self.valid_moves.append((self.lrp_col, self.lrp_row))
            if self.lrn_row >= 0 and self.lrn_row <= 7 and self.lrn_row != self.row and self.lrn_col >= 0 and self.lrn_col <=7 and self.lrn_col != self.col:
                self.valid_moves.append((self.lrn_col, self.lrn_row))
            # move like a rook
            if (self.col, self.row+count) != self.location and self.row+count >=0 and self.row+count <= 7:
                self.valid_moves.append((self.col, self.row+count))
            if (self.col, self.row-count) != self.location and self.row-count >=0 and self.row-count <= 7:
                self.valid_moves.append((self.col, self.row-count))
            if (self.col+count, self.row) != self.location and self.col+count >=0 and self.col+count <= 7:
                self.valid_moves.append((self.col+count, self.row))
            if (self.col-count, self.row) != self.location and self.col-count >=0 and self.col-count <= 7:
                self.valid_moves.append((self.col-count, self.row))
            count+=1


class King():
    def __init__(self, color, location, value=1000000):
        self.color = color
        self.name = 'K'
        self.value = value
        self.location = location
        self.col = location[0]
        self.row = location[1]
        self.moves = []
        self.valid_moves = []
        self.can_capture = False
        self.in_danger = False
        self.castle = True
        self.blocked = False

    def move(self, move):
        self.valid_moves = []
        self._possible_moves()
        self._set_can_capture()
        if move in self.valid_moves:
            self.moves.append(move)
            self._update_location(move)
        else:
            print('Sorry, not a valid move...try again')

    def _set_can_capture(self, capture=False):
        if capture:
            self.can_capture = True
        else:
            self.can_capture = False

    def __str__(self):
        if self.color == 'white':
            return '\u265A'
        if self.color == 'black':
            return '\u2654'
        else:
            print('not a valid color...try white or black')

    def __hash__(self):
        return hash((self.color, self.value, self.name, self.location))

    def __eq__(self, other):
        return (self.color, self.value, self.name, self.location) == (other.color, other.value, other.name, other.location)

    def _update_location(self, newlocal):
        self.location = newlocal
        self.col = newlocal[0]
        self.row = newlocal[1]

    def _possible_moves(self):
        if len(self.moves) == 0:
            self.castle = True
        else:
            self.castle = False
        possible_moves = [((self.col - 1), (self.row - 1)), ((self.col), (self.row - 1)),\
                            ((self.col + 1), (self.row - 1)), ((self.col + 1), (self.row)),\
                            ((self.col + 1), (self.row + 1)), ((self.col), (self.row + 1)),\
                            ((self.col - 1), (self.row + 1)), ((self.col - 1), (self.row))]
        for pm in possible_moves:
            c, r = pm
            if r >= 0 and r <= 7 and c >= 0 and c <=7:
                self.valid_moves.append((c, r))

    def _check_for_check(self):
        return

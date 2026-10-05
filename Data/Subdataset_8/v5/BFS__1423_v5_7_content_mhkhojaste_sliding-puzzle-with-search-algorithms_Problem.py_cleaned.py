from copy import deepcopy
from math import sqrt
class ProblemClass:
    def __init__(self):
        self.initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def get_initial_state(self):
        return self.initial_state
    def get_moves(self, current_state):
        zero_row, zero_col = self.find_zero(current_state)
        moves = []
        if zero_row > 0:
            moves.append('U')
        if zero_row < 2:
            moves.append('D')
        if zero_col > 0:
            moves.append('L')
        if zero_col < 2:
            moves.append('R')
        return moves
    def do_move(self, current_state, move):
        new_state = deepcopy(current_state)
        zero_row, zero_col = self.find_zero(new_state)
        if move == 'R':
            new_state[zero_row][zero_col], new_state[zero_row][zero_col + 1] = new_state[zero_row][zero_col + 1], 0
        elif move == 'L':
            new_state[zero_row][zero_col], new_state[zero_row][zero_col - 1] = new_state[zero_row][zero_col - 1], 0
        elif move == 'U':
            new_state[zero_row][zero_col], new_state[zero_row - 1][zero_col] = new_state[zero_row - 1][zero_col], 0
        elif move == 'D':
            new_state[zero_row][zero_col], new_state[zero_row + 1][zero_col] = new_state[zero_row + 1][zero_col], 0
        return new_state
    def check_goal(self, current_state):
        return current_state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def find_h(self, current_state):
        h = 0
        for i in range(3):
            for j in range(3):
                number = (i * 3 + j + 1) % 9
                number_row, number_col = self.find_number(current_state, number)
                h += sqrt((i - number_row) ** 2 + (j - number_col) ** 2)
        return round(h, 2)
    def find_zero(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
    def find_number(self, state, number):
        for i in range(3):
            for j in range(3):
                if state[i][j] == number:
                    return i, j
from copy import deepcopy
from math import sqrt
class ProblemClass:
    def __init__(self):
        self.state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def get_init_state(self):
        return self.state
    def get_moves(self, my_state):
        zero_row, zero_col = self.find_zero(my_state)
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
    def do_move(self, states, transaction):
        my_state = deepcopy(states)
        zero_row, zero_col = self.find_zero(my_state)
        if transaction == 'R':
            my_state[zero_row][zero_col], my_state[zero_row][zero_col + 1] = my_state[zero_row][zero_col + 1], 0
        elif transaction == 'L':
            my_state[zero_row][zero_col], my_state[zero_row][zero_col - 1] = my_state[zero_row][zero_col - 1], 0
        elif transaction == 'U':
            my_state[zero_row][zero_col], my_state[zero_row - 1][zero_col] = my_state[zero_row - 1][zero_col], 0
        elif transaction == 'D':
            my_state[zero_row][zero_col], my_state[zero_row + 1][zero_col] = my_state[zero_row + 1][zero_col], 0
        return my_state
    def check_goal(self, my_state):
        return my_state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def find_h(self, my_matrix):
        h = 0
        for i in range(3):
            for j in range(3):
                number = (i * 3 + j + 1) % 9
                number_row, number_col = self.find_number(my_matrix, number)
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
from copy import deepcopy
from math import sqrt
class ProblemClass:
    def __init__(self):
        self.state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def get_init_state(self):
        return self.state
    def get_moves(self, state):
        moves = []
        i, j = [(ix, iy) for ix, row in enumerate(state) for iy, val in enumerate(row) if val == 0][0]
        if i > 0:
            moves.append('U')
        if i < 2:
            moves.append('D')
        if j > 0:
            moves.append('L')
        if j < 2:
            moves.append('R')
        return moves
    def do_move(self, state, move):
        new_state = deepcopy(state)
        i, j = [(ix, iy) for ix, row in enumerate(state) for iy, val in enumerate(row) if val == 0][0]
        if move == 'U':
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        elif move == 'D':
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        elif move == 'L':
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        elif move == 'R':
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        return new_state
    def check_goal(self, state):
        return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def find_h(self, state):
        heuristic = 0
        for i in range(3):
            for j in range(3):
                number = (i * 3 + j + 1) % 9
                x, y = [(ix, iy) for ix, row in enumerate(state) for iy, val in enumerate(row) if val == number][0]
                heuristic += sqrt((i - x) ** 2 + (j - y) ** 2)
        return round(heuristic, 2)
if __name__ == "__main__":
    puzzle = ProblemClass()
    initial_state = puzzle.get_init_state()
    print("Initial State:", initial_state)
    print("Possible Moves:", puzzle.get_moves(initial_state))
    new_state = puzzle.do_move(initial_state, 'D')
    print("State after moving down:", new_state)
    print("Is goal state:", puzzle.check_goal(new_state))
    print("Heuristic value:", puzzle.find_h(new_state))
from copy import deepcopy
from math import sqrt
class ProblemClass:
    def __init__(self):
        self.state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def get_init_state(self):
        return self.state
    def get_moves(self, state):
        moves = {
            (0, 0): ['R', 'D'],
            (0, 1): ['L', 'R', 'D'],
            (0, 2): ['L', 'D'],
            (1, 0): ['R', 'D', 'U'],
            (1, 1): ['L', 'R', 'D', 'U'],
            (1, 2): ['L', 'D', 'U'],
            (2, 0): ['R', 'U'],
            (2, 1): ['L', 'R', 'U'],
            (2, 2): ['L', 'U']
        }
        zero_position = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
        return moves[zero_position]
    def do_move(self, state, move):
        new_state = deepcopy(state)
        zero_position = [(ix, iy) for ix, row in enumerate(new_state) for iy, i in enumerate(row) if i == 0][0]
        i, j = zero_position
        if move == 'R':
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
        elif move == 'L':
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        elif move == 'U':
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        elif move == 'D':
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        return new_state
    def check_goal(self, state):
        return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def find_h(self, state):
        total_distance = 0
        for i in range(3):
            for j in range(3):
                number = (i * 3 + j + 1) % 9
                target_position = [(ix, iy) for ix, row in enumerate(state) for iy, val in enumerate(row) if val == number][0]
                total_distance += sqrt((i - target_position[0]) ** 2 + (j - target_position[1]) ** 2)
        return round(total_distance, 2)
if __name__ == "__main__":
    problem = ProblemClass()
    init_state = problem.get_init_state()
    print("Initial State:")
    print(init_state)
    moves = problem.get_moves(init_state)
    print("\nPossible Moves:")
    print(moves)
    new_state = problem.do_move(init_state, moves[0])
    print("\nNew State after move", moves[0], ":")
    print(new_state)
    is_goal = problem.check_goal(new_state)
    print("\nIs Goal State:", is_goal)
    heuristic_value = problem.find_h(new_state)
    print("\nHeuristic Value of New State:")
    print(heuristic_value)
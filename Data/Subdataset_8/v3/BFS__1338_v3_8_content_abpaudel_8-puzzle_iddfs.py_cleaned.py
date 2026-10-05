import itertools
class Board:
    GOAL_STATE = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1
    def is_goal_state(self):
        return self.state == self.GOAL_STATE
    def get_neighbors(self):
        neighbors = []
        empty_row, empty_col = next((i, j) for i, row in enumerate(self.state) for j, val in enumerate(row) if val == 0)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for move in moves:
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                neighbor_state = [row.copy() for row in self.state]
                neighbor_state[empty_row][empty_col], neighbor_state[new_row][new_col] = neighbor_state[new_row][new_col], neighbor_state[empty_row][empty_col]
                neighbors.append(Board(neighbor_state, self))
        return neighbors
class Solver:
    def __init__(self, initial_state):
        self.initial_state = Board(initial_state)
        self.solution = None
        self.explored_nodes = set()
    def set_solution(self, node):
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        self.solution = path[::-1]
    def solve(self):
        raise NotImplementedError("Solver class must implement solve() method")
class IDDFS(Solver):
    def __init__(self, initial_state):
        super().__init__(initial_state)
        self.frontier = []
    def depth_limited_search(self, limit):
        self.frontier.append(self.initial_state)
        while self.frontier:
            board = self.frontier.pop()
            self.explored_nodes.add(tuple(board.state))
            if board.is_goal_state():
                self.set_solution(board)
                return self.solution
            if board.depth < limit:
                for neighbor in reversed(board.get_neighbors()):
                    if tuple(neighbor.state) not in self.explored_nodes:
                        self.frontier.append(neighbor)
                        self.explored_nodes.add(tuple(neighbor.state))
        return None
    def solve(self):
        for depth_limit in itertools.count():
            self.frontier = []
            self.explored_nodes = set()
            self.frontier.append(self.initial_state)
            solution = self.depth_limited_search(depth_limit)
            if solution:
                return solution
def parse_input(initial_state_str):
    initial_state = [[int(num) for num in row.split(',')] for row in initial_state_str.split()]
    return initial_state
def write_output(output_file, solution):
    with open(output_file, 'w') as file:
        for state in solution:
            for row in state:
                file.write(','.join(map(str, row)) + '\n')
            file.write('\n')
def main(algorithm, initial_state_str):
    algorithm = algorithm
    initial_state_str = initial_state_str
    initial_state = parse_input(initial_state_str)
    solver = IDDFS(initial_state)
    solution = solver.solve()
    if solution:
        write_output(f"{algorithm}_output.txt", solution)
        print("Solution found and written to output file.")
    else:
        print("No solution found for the given initial state.")
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py algorithm initial_state")
        sys.exit(1)
    algorithm = sys.argv[1]
    initial_state_str = sys.argv[2]
    main(algorithm, initial_state_str)
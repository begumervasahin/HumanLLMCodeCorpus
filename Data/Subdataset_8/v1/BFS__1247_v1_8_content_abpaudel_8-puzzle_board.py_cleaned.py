import numpy as np
import heapq
class Board:
    def __init__(self, state, parent=None, operator=None, depth=0):
        self.parent = parent
        self.state = np.array(state)
        self.operator = operator
        self.depth = depth
        self.zero = self.find_zero()
        self.cost = self.depth + self.manhattan()
    def __lt__(self, other):
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            op_pr = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
            return op_pr[self.operator] < op_pr[other.operator]
    def __str__(self):
        return str(self.state[:3]) + '\n' + str(self.state[3:6]) + '\n' + str(self.state[6:]) + ' ' + str(
            self.depth) + str(self.operator) + '\n'
    def goal_test(self):
        return np.array_equal(self.state, np.arange(9))
    def find_zero(self):
        return np.where(self.state == 0)[0][0]
    def manhattan(self):
        state = self.index(self.state)
        goal = self.index(np.arange(9))
        return sum((abs(state
    @staticmethod
    def index(state):
        index = np.array(range(9))
        for x, y in enumerate(state):
            index[y] = x
        return index
    def swap(self, i, j):
        new_state = np.array(self.state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state
    def up(self):
        if self.zero > 2:
            return Board(self.swap(self.zero, self.zero - 3), self, 'Up', self.depth + 1)
    def down(self):
        if self.zero < 6:
            return Board(self.swap(self.zero, self.zero + 3), self, 'Down', self.depth + 1)
    def left(self):
        if self.zero % 3 != 0:
            return Board(self.swap(self.zero, self.zero - 1), self, 'Left', self.depth + 1)
    def right(self):
        if (self.zero + 1) % 3 != 0:
            return Board(self.swap(self.zero, self.zero + 1), self, 'Right', self.depth + 1)
    def neighbors(self):
        neighbors = [self.up(), self.down(), self.left(), self.right()]
        return [neighbor for neighbor in neighbors if neighbor]
    __repr__ = __str__
def astar(initial_state):
    initial_board = Board(initial_state)
    if initial_board.goal_test():
        return [initial_board]
    visited = set()
    priority_queue = [initial_board]
    heapq.heapify(priority_queue)
    while priority_queue:
        current_board = heapq.heappop(priority_queue)
        visited.add(tuple(current_board.state))
        for neighbor in current_board.neighbors():
            if neighbor.goal_test():
                return get_path(neighbor)
            if tuple(neighbor.state) not in visited:
                heapq.heappush(priority_queue, neighbor)
def get_path(board):
    path = []
    while board:
        path.append(board)
        board = board.parent
    return path[::-1]
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python main.py <algorithm> <initial_state>")
        sys.exit(1)
    algorithm = sys.argv[1]
    initial_state = list(map(int, sys.argv[2].split(',')))
    if algorithm == 'ast':
        solution_path = astar(initial_state)
        if solution_path:
            with open("ast_output.txt", "w") as f:
                for board in solution_path:
                    f.write(str(board))
                    f.write("\n")
        else:
            print("No solution found.")
    else:
        print("Invalid algorithm. Please choose 'ast'.")
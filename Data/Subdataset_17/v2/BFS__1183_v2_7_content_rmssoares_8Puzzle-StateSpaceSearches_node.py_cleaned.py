from queue import Queue
from copy import deepcopy
class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1
        self.moves = move if parent is None else parent.moves + move
    def goal_state(self):
        return self.state.check_puzzle()
    def successors(self):
        successors = Queue()
        for move in self.state.moves:
            new_state = deepcopy(self.state)
            new_state.do_move(move)
            if new_state.zero != self.state.zero:
                successors.put(Node(new_state, self, move))
        return successors
    def cost_heuristic(self, heuristic):
        return self.num_wrong_tiles() if heuristic == 0 else self.manhattan_distance()
    def num_wrong_tiles(self):
        result = 0
        count = 1
        for i in range(self.state.size):
            for j in range(self.state.size):
                if self.state.puzzle[i][j] != (count % (self.state.size * self.state.size)):
                    result += 1
                count += 1
        return result
    def manhattan_distance(self):
        result = 0
        for i in range(self.state.size):
            for j in range(self.state.size):
                index = self.state.puzzle[i][j] - 1
                if index == -1:
                    continue
                correct_row, correct_col = divmod(index, self.state.size)
                result += abs(i - correct_row) + abs(j - correct_col)
        return result
    def __str__(self):
        return str(self.moves)
class Puzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.moves = ['U', 'D', 'L', 'R']
        self.zero = self.find_zero()
    def find_zero(self):
        for i, row in enumerate(self.puzzle):
            for j, value in enumerate(row):
                if value == 0:
                    return (i, j)
        return None
    def do_move(self, move):
        i, j = self.zero
        if move == 'U' and i > 0:
            self.puzzle[i][j], self.puzzle[i - 1][j] = self.puzzle[i - 1][j], self.puzzle[i][j]
            self.zero = (i - 1, j)
        elif move == 'D' and i < self.size - 1:
            self.puzzle[i][j], self.puzzle[i + 1][j] = self.puzzle[i + 1][j], self.puzzle[i][j]
            self.zero = (i + 1, j)
        elif move == 'L' and j > 0:
            self.puzzle[i][j], self.puzzle[i][j - 1] = self.puzzle[i][j - 1], self.puzzle[i][j]
            self.zero = (i, j - 1)
        elif move == 'R' and j < self.size - 1:
            self.puzzle[i][j], self.puzzle[i][j + 1] = self.puzzle[i][j + 1], self.puzzle[i][j]
            self.zero = (i, j + 1)
    def check_puzzle(self):
        goal = list(range(1, self.size * self.size)) + [0]
        return self.puzzle == [goal[i:i + self.size] for i in range(0, len(goal), self.size)]
if __name__ == "__main__":
    initial_state = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    node = Node(initial_state)
    print("Initial Node:")
    print(node)
    print("Is Goal State:", node.goal_state())
    print("Heuristic (number of wrong tiles):", node.cost_heuristic(0))
    print("Heuristic (Manhattan distance):", node.cost_heuristic(1))
    children = node.successors()
    print("\nChildren States:")
    while not children.empty():
        child_node = children.get()
        print(child_node)
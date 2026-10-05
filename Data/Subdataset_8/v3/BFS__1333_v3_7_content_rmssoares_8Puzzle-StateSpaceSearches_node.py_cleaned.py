from copy import deepcopy
from queue import Queue
class Puzzle:
    def __init__(self, size=3):
        self.size = size
        self.puzzle = self.generate_puzzle()
    def generate_puzzle(self):
        puzzle = [[0] * self.size for _ in range(self.size)]
        numbers = list(range(1, self.size * self.size))
        numbers.append(0)
        numbers.reverse()
        for i in range(self.size):
            for j in range(self.size):
                puzzle[i][j] = numbers.pop()
        return puzzle
    def check_puzzle(self):
        count = 1
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] != count % (self.size * self.size):
                    return False
                count += 1
        return True
    def do_move(self, move):
        zero_row, zero_col = self.find_zero()
        if move == 'R' and zero_col < self.size - 1:
            self.puzzle[zero_row][zero_col], self.puzzle[zero_row][zero_col + 1] = self.puzzle[zero_row][zero_col + 1], 0
        elif move == 'L' and zero_col > 0:
            self.puzzle[zero_row][zero_col], self.puzzle[zero_row][zero_col - 1] = self.puzzle[zero_row][zero_col - 1], 0
        elif move == 'U' and zero_row > 0:
            self.puzzle[zero_row][zero_col], self.puzzle[zero_row - 1][zero_col] = self.puzzle[zero_row - 1][zero_col], 0
        elif move == 'D' and zero_row < self.size - 1:
            self.puzzle[zero_row][zero_col], self.puzzle[zero_row + 1][zero_col] = self.puzzle[zero_row + 1][zero_col], 0
    def find_zero(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 0:
                    return i, j
class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        self.depth = 0
        if parent is None:
            self.depth = 0
            self.moves = move
        else:
            self.depth = parent.depth + 1
            self.moves = parent.moves + move
    def goal_state(self):
        return self.state.check_puzzle()
    def succ(self):
        succs = Queue()
        for m in self.state.moves:
            p = deepcopy(self.state)
            p.do_move(m)
            if p.find_zero() != self.state.find_zero():
                succs.put(Node(p, self, m))
        return succs
    def cost_heur(self, heuristic):
        return self.n_wrong_tiles() if heuristic == 0 else self.manhattan_distance()
    def n_wrong_tiles(self):
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
        count = 1
        for i in range(self.state.size):
            for j in range(self.state.size):
                index = self.state.puzzle[i][j] - 1
                if index != -1:
                    distance = abs(i - (index
                    result += distance
                count += 1
        return result
    def __str__(self):
        return str(self.moves)
def main():
    puzzle = Puzzle()
    initial_node = Node(puzzle)
    print("Initial state:", puzzle.puzzle)
    print("Is the initial state a goal state?", initial_node.goal_state())
    print("Possible moves from the initial state:", puzzle.moves)
    print("Successor states:", [str(s) for s in initial_node.succ()])
if __name__ == "__main__":
    main()
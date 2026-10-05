from copy import deepcopy
from queue import Queue
class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        self.depth = 0
        if parent is None:
            self.moves = move
        else:
            self.depth = parent.depth + 1
            self.moves = parent.moves + move
    def is_goal_state(self):
        return self.state.check_puzzle()
    def generate_successor_states(self):
        successors = Queue()
        for m in self.state.moves:
            new_state = deepcopy(self.state)
            new_state.perform_move(m)
            if new_state.find_zero() != self.state.find_zero():
                successors.put(Node(new_state, self, m))
        return successors
    def calculate_cost_heuristic(self, heuristic):
        if heuristic == 0:
            return self.calculate_wrong_tiles_heuristic()
        else:
            return self.calculate_manhattan_distance_heuristic()
    def calculate_wrong_tiles_heuristic(self):
        result = 0
        count = 1
        for i in range(0, self.state.size):
            for j in range(0, self.state.size):
                if self.state.puzzle[i][j] != (count % (self.state.size * self.state.size)):
                    result += 1
                count += 1
        return result
    def calculate_manhattan_distance_heuristic(self):
        result = 0
        count = 1
        for i in range(0, self.state.size):
            for j in range(0, self.state.size):
                index = self.state.puzzle[i][j] - 1
                distance = (2 - i) + (2 - j) if index == -1 else abs(i - (index
                result += distance
                count += 1
        return result
    def __str__(self):
        return str(self.moves)
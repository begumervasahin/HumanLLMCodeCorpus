from copy import deepcopy
from queue import Queue
class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        self.depth = 0
        if parent is not None:
            self.depth = parent.depth + 1
            self.moves = parent.moves + move
        else:
            self.moves = move
    def is_goal_state(self):
        return self.state.check_puzzle()
    def generate_successor_states(self):
        successors = Queue()
        for move in self.state.moves:
            new_state = deepcopy(self.state)
            new_state.perform_move(move)
            if new_state.find_zero() != self.state.find_zero():
                successors.put(Node(new_state, self, move))
        return successors
    def calculate_cost_heuristic(self, heuristic):
        if heuristic == 0:
            return self.calculate_wrong_tiles_heuristic()
        else:
            return self.calculate_manhattan_distance_heuristic()
    def calculate_wrong_tiles_heuristic(self):
        result = 0
        count = 1
        for i in range(self.state.size):
            for j in range(self.state.size):
                if self.state.puzzle[i][j] != (count % (self.state.size * self.state.size)):
                    result += 1
                count += 1
        return result
    def calculate_manhattan_distance_heuristic(self):
        result = 0
        for i in range(self.state.size):
            for j in range(self.state.size):
                index = self.state.puzzle[i][j] - 1
                if index != -1:
                    distance = abs(i - (index
                    result += distance
        return result
    def __str__(self):
        return str(self.moves)
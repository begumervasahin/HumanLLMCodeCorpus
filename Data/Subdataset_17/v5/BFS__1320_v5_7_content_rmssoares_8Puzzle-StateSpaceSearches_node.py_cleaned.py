
from queue import Queue
from copy import deepcopy
class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        self.move = move
        self.depth = 0 if parent is None else parent.depth + 1
        self.moves = move if parent is None else parent.moves + move
    def goal_state(self):
        return self.state.check_puzzle()
    def generate_successors(self):
        successors = Queue()
        for move in self.state.moves:
            new_puzzle = deepcopy(self.state)
            new_puzzle.do_move(move)
            if new_puzzle.zero != self.state.zero:
                successors.put(Node(new_puzzle, self, move))
        return successors
    def calculate_heuristic(self, heuristic):
        if heuristic == 0:
            return self.number_of_wrong_tiles()
        else:
            return self.manhattan_distance()
    def number_of_wrong_tiles(self):
        wrong_tiles = 0
        count = 1
        for i in range(self.state.size):
            for j in range(self.state.size):
                if self.state.puzzle[i][j] != (count % (self.state.size * self.state.size)):
                    wrong_tiles += 1
                count += 1
        return wrong_tiles
    def manhattan_distance(self):
        distance = 0
        for i in range(self.state.size):
            for j in range(self.state.size):
                index = self.state.puzzle[i][j] - 1
                if index == -1:
                    tile_distance = (self.state.size - 1 - i) + (self.state.size - 1 - j)
                else:
                    tile_distance = abs(i - (index
                distance += tile_distance
        return distance
    def __str__(self):
        return f"Moves: {self.moves}"
if __name__ == "__main__":
    from puzzle import Puzzle
    initial_state = Puzzle([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
    root_node = Node(initial_state)
    print("Initial State:")
    print(root_node.state)
    print("Is goal state?", root_node.goal_state())
    print("Possible moves from initial state:")
    successors = root_node.generate_successors()
    while not successors.empty():
        node = successors.get()
        print(node.state, "Move:", node.moves)
    print("Heuristic (Number of wrong tiles):", root_node.number_of_wrong_tiles())
    print("Heuristic (Manhattan distance):", root_node.manhattan_distance())
import numpy as np
class Board:
    def __init__(self, state, parent=None, operator=None, depth=0):
        self.parent = parent
        self.state = np.array(state)
        self.operator = operator
        self.depth = depth
        self.zero = self.find_zero_position()
        self.cost = self.depth + self.manhattan_distance()
    def __lt__(self, other):
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            operator_priority = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
            return operator_priority[self.operator] < operator_priority[other.operator]
    def __str__(self):
        state_str = str(self.state[:3]) + '\n' + str(self.state[3:6]) + '\n' + str(self.state[6:])
        return f"{state_str} Depth: {self.depth} Operator: {self.operator}\n"
    def goal_test(self):
        return np.array_equal(self.state, np.arange(9))
    def find_zero_position(self):
        return np.where(self.state == 0)[0][0]
    def manhattan_distance(self):
        state_indices = self.indices(self.state)
        goal_indices = self.indices(np.arange(9))
        return sum((abs(state_indices
    @staticmethod
    def indices(state):
        indices = np.zeros_like(state)
        for index, value in enumerate(state):
            indices[value] = index
        return indices
    def swap(self, i, j):
        new_state = self.state.copy()
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state
    def up(self):
        if self.zero > 2:
            return Board(self.swap(self.zero, self.zero - 3), self, 'Up', self.depth + 1)
        return None
    def down(self):
        if self.zero < 6:
            return Board(self.swap(self.zero, self.zero + 3), self, 'Down', self.depth + 1)
        return None
    def left(self):
        if self.zero % 3 != 0:
            return Board(self.swap(self.zero, self.zero - 1), self, 'Left', self.depth + 1)
        return None
    def right(self):
        if (self.zero + 1) % 3 != 0:
            return Board(self.swap(self.zero, self.zero + 1), self, 'Right', self.depth + 1)
        return None
    def neighbors(self):
        possible_moves = [self.up(), self.down(), self.left(), self.right()]
        return list(filter(None, possible_moves))
    __repr__ = __str__
if __name__ == "__main__":
    initial_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    board = Board(initial_state)
    print("Initial State:")
    print(board)
    print("Is goal state:", board.goal_test())
    print("Possible moves:")
    for neighbor in board.neighbors():
        print(neighbor)
    print("Manhattan distance:", board.manhattan_distance())
import numpy as np
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
            return self.compare_operators(other)
    def __str__(self):
        return (
            f"{self.state[:3]}\n"
            f"{self.state[3:6]}\n"
            f"{self.state[6:]} {self.depth}{self.operator}\n"
        )
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
        index = np.zeros(9, dtype=int)
        for x, y in enumerate(state):
            index[y] = x
        return index
    def swap(self, i, j):
        new_state = np.array(self.state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state
    def up(self):
        if self.zero > 2:
            return self.create_new_board(self.zero - 3, 'Up')
    def down(self):
        if self.zero < 6:
            return self.create_new_board(self.zero + 3, 'Down')
    def left(self):
        if self.zero % 3 != 0:
            return self.create_new_board(self.zero - 1, 'Left')
    def right(self):
        if (self.zero + 1) % 3 != 0:
            return self.create_new_board(self.zero + 1, 'Right')
    def neighbors(self):
        return [neighbor for neighbor in [self.up(), self.down(), self.left(), self.right()] if neighbor]
    def compare_operators(self, other):
        op_priority = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
        return op_priority[self.operator] < op_priority[other.operator]
    def create_new_board(self, new_zero, direction):
        return Board(self.swap(self.zero, new_zero), self, direction, self.depth + 1)
    def __repr__(self):
        return self.__str__()
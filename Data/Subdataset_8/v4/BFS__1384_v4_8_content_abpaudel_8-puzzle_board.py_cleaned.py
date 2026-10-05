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
            op_priority = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
            return op_priority[self.operator] < op_priority[other.operator]
    def __str__(self):
        return (
            str(self.state[:3]) + '\n' +
            str(self.state[3:6]) + '\n' +
            str(self.state[6:]) + ' ' +
            str(self.depth) + str(self.operator) + '\n'
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
        else:
            return None
    def down(self):
        if self.zero < 6:
            return Board(self.swap(self.zero, self.zero + 3), self, 'Down', self.depth + 1)
        else:
            return None
    def left(self):
        if self.zero % 3 != 0:
            return Board(self.swap(self.zero, self.zero - 1), self, 'Left', self.depth + 1)
        else:
            return None
    def right(self):
        if (self.zero + 1) % 3 != 0:
            return Board(self.swap(self.zero, self.zero + 1), self, 'Right', self.depth + 1)
        else:
            return None
    def neighbors(self):
        neighbors = [self.up(), self.down(), self.left(), self.right()]
        return list(filter(None, neighbors))
    def __repr__(self):
        return self.__str__()
import numpy as np
class Board:
    def __init__(self, state, parent=None, operator=None, depth=0):
        self.parent = parent
        self.state = np.array(state)
        self.operator = operator
        self.depth = depth
        self.zero = self.find_zero()
        self.cost = self.depth + self.manhattan_distance()
    def __lt__(self, other):
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            op_priority = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
            return op_priority[self.operator] < op_priority[other.operator]
    def __str__(self):
        return f"{self.state[:3]}\n{self.state[3:6]}\n{self.state[6:]} {self.depth} {self.operator}\n"
    def goal_test(self):
        return np.array_equal(self.state, np.arange(9))
    def find_zero(self):
        return np.where(self.state == 0)[0][0]
    def manhattan_distance(self):
        current_index = self.index(self.state)
        goal_index = self.index(np.arange(9))
        return sum((abs(current_index
    @staticmethod
    def index(state):
        index = np.zeros(9, dtype=int)
        for x, y in enumerate(state):
            index[y] = x
        return index
    def swap(self, i, j):
        new_state = self.state.copy()
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state
    def move_up(self):
        if self.zero > 2:
            return Board(self.swap(self.zero, self.zero - 3), self, 'Up', self.depth + 1)
        return None
    def move_down(self):
        if self.zero < 6:
            return Board(self.swap(self.zero, self.zero + 3), self, 'Down', self.depth + 1)
        return None
    def move_left(self):
        if self.zero % 3 != 0:
            return Board(self.swap(self.zero, self.zero - 1), self, 'Left', self.depth + 1)
        return None
    def move_right(self):
        if (self.zero + 1) % 3 != 0:
            return Board(self.swap(self.zero, self.zero + 1), self, 'Right', self.depth + 1)
        return None
    def neighbors(self):
        neighbors = [self.move_up(), self.move_down(), self.move_left(), self.move_right()]
        return [neighbor for neighbor in neighbors if neighbor is not None]
    __repr__ = __str__
if __name__ == "__main__":
    initial_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    board = Board(initial_state)
    print("Initial Board State:")
    print(board)
    print("\nIs Goal State:", board.goal_test())
    print("\nManhattan Distance:", board.manhattan_distance())
    print("\nPossible Moves and States:")
    for neighbor in board.neighbors():
        print(neighbor)
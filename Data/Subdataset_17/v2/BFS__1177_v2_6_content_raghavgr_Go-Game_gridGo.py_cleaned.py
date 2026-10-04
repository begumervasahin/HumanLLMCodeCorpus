from collections import deque
from enum import Enum
class Node(Enum):
    BLACK = 5
    WHITE = 2
    EMPTY = 0
class Grid:
    def __init__(self, size, nodepairs):
        self.size = size
        self.board = [[Node.EMPTY for _ in range(size)] for _ in range(size)]
        for location, value in nodepairs:
            self.set_value(location, value)
    def get_value(self, location):
        return self.board[location[0]][location[1]]
    def set_value(self, location, value):
        self.board[location[0]][location[1]] = value
    def is_captured(self, location):
        if self.get_value(location) == Node.WHITE:
            return False
        if self.is_within_bounds(location):
            queue = deque([location])
            visited = [[False for _ in range(self.size)] for _ in range(self.size)]
            self.set_value(location, True, visited)
            while queue:
                current = queue.popleft()
                self.set_value(current, True, visited)
                if not self.is_surrounded(queue, visited, current):
                    return False
            return True
        return False
    def is_within_bounds(self, location):
        return 0 <= location[0] < self.size and 0 <= location[1] < self.size
    def is_surrounded(self, queue, visited, current):
        neighbors = [
            [current[0], current[1] + 1],
            [current[0], current[1] - 1],
            [current[0] + 1, current[1]],
            [current[0] - 1, current[1]]
        ]
        for loc in neighbors:
            if self.is_within_bounds(loc):
                if not self.get_value(loc, visited):
                    if self.get_value(loc) == Node.WHITE:
                        self.set_value(loc, True, visited)
                    elif self.get_value(loc) == Node.EMPTY:
                        return False
                    elif self.get_value(loc) == Node.BLACK:
                        queue.append(loc)
        return True
if __name__ == "__main__":
    new_grid = Grid(5, [
        ([1, 3], Node.WHITE),
        ([1, 2], Node.WHITE),
        ([3, 3], Node.WHITE),
        ([3, 2], Node.EMPTY),
        ([2, 1], Node.WHITE),
        ([2, 4], Node.WHITE),
        ([2, 2], Node.BLACK),
        ([2, 3], Node.BLACK),
    ])
    print(new_grid.is_captured([2, 2]))
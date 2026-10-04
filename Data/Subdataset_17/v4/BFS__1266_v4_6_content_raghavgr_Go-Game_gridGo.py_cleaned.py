
from collections import deque
from enum import Enum
class Node(Enum):
    BLACK = 5
    WHITE = 2
    EMPTY = 0
class Grid:
    def __init__(self, size, node_pairs):
        self.board = [[Node.EMPTY for _ in range(size)] for _ in range(size)]
        self.size = size
        for location, value in node_pairs:
            self.set_value(location, value)
    def get_value(self, location):
        return self.board[location[0]][location[1]]
    def set_value(self, location, value):
        self.board[location[0]][location[1]] = value
    def is_captured(self, location):
        if self.get_value(location) == Node.WHITE:
            return False
        if not self.is_within_bounds(location):
            return False
        q = deque([location])
        visited = [[False for _ in range(self.size)] for _ in range(self.size)]
        self.set_value(visited, location, True)
        while q:
            curr = q.popleft()
            self.set_value(visited, curr, True)
            if self.is_surrounded(q, visited, curr):
                continue
            else:
                return False
        return True
    def is_within_bounds(self, location):
        return 0 <= location[0] < self.size and 0 <= location[1] < self.size
    def is_surrounded(self, q, visited, curr):
        neighbors = [
            [curr[0], curr[1] + 1],
            [curr[0], curr[1] - 1],
            [curr[0] + 1, curr[1]],
            [curr[0] - 1, curr[1]]
        ]
        for loc in neighbors:
            if self.is_within_bounds(loc):
                if not self.get_value(visited, loc):
                    if self.get_value(loc) == Node.WHITE:
                        self.set_value(visited, loc, True)
                        continue
                    elif self.get_value(loc) == Node.EMPTY:
                        return False
                    elif self.get_value(loc) == Node.BLACK:
                        q.append(loc)
            else:
                continue
        return True
    def get_value(self, visited, location):
        return visited[location[0]][location[1]]
if __name__ == "__main__":
    node_pairs = [
        ([1, 3], Node.WHITE),
        ([1, 2], Node.WHITE),
        ([3, 3], Node.WHITE),
        ([3, 2], Node.EMPTY),
        ([2, 1], Node.WHITE),
        ([2, 4], Node.WHITE),
        ([2, 2], Node.BLACK),
        ([2, 3], Node.BLACK),
    ]
    new_grid = Grid(5, node_pairs)
    print(new_grid.is_captured([2, 2]))
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
        for location, node_state in node_pairs:
            self.set_node_state(location, node_state)
    def get_node_state(self, location):
        return self.board[location[0]][location[1]]
    def set_node_state(self, location, state):
        self.board[location[0]][location[1]] = state
    def is_captured(self, location):
        if self.get_node_state(location) == Node.WHITE:
            return False
        if self.is_within_bounds(location):
            queue = deque()
            queue.appendleft(location)
            visited = [[False for _ in range(self.size)] for _ in range(self.size)]
            visited[location[0]][location[1]] = True
            while queue:
                current = queue.popleft()
                if self.is_surrounded(queue, visited, current):
                    continue
                else:
                    return False
            return True
        else:
            return False
    def is_within_bounds(self, location):
        row, col = location
        return 0 <= row < self.size and 0 <= col < self.size
    def is_surrounded(self, queue, visited, current):
        row, col = current
        neighbors = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
        for neighbor_row, neighbor_col in neighbors:
            if self.is_within_bounds((neighbor_row, neighbor_col)):
                if not visited[neighbor_row][neighbor_col]:
                    neighbor_state = self.get_node_state((neighbor_row, neighbor_col))
                    if neighbor_state == Node.WHITE:
                        visited[neighbor_row][neighbor_col] = True
                        continue
                    elif neighbor_state == Node.EMPTY:
                        return False
                    elif neighbor_state == Node.BLACK:
                        queue.append((neighbor_row, neighbor_col))
            else:
                continue
        return True
if __name__ == "__main__":
    new_grid = Grid(5, [([1, 3], Node.WHITE),
                        ([1, 2], Node.WHITE),
                        ([3, 3], Node.WHITE),
                        ([3, 2], Node.EMPTY),
                        ([2, 1], Node.WHITE),
                        ([2, 4], Node.WHITE),
                        ([2, 2], Node.BLACK),
                        ([2, 3], Node.BLACK),
                        ])
    print(new_grid.is_captured([2, 2]))
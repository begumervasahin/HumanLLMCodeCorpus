import numpy as np
import matplotlib.pyplot as plt
class PrimsMaze:
    def __init__(self, size=25, show_maze=True):
        self.size = (size
        self.show_maze = show_maze
        self.walls_list = []
        self.grid = np.full((self.size, self.size), -50, dtype=int)
        self.maze = np.zeros((self.size, self.size), dtype=bool)
        for i in range(size
            for j in range(size
                self.grid[i * 2, j * 2] = -1
    def is_valid(self, curr, dx, dy):
        x, y = curr
        return 0 <= x + dx < self.size and 0 <= y + dy < self.size
    def add_neighbors(self, curr):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dx, dy in directions:
            if self.is_valid(curr, dx, dy):
                self.walls_list.append((curr[0] + dx, curr[1] + dy))
    def create_maze(self, start):
        start = ((start[0]
        self.grid[start[0], start[1]] = 1
        self.add_neighbors(start)
        while self.walls_list:
            ind = np.random.randint(0, len(self.walls_list))
            wall_x, wall_y = self.walls_list[ind]
            if self.is_valid((wall_x, wall_y), -1, 0) and self.is_valid((wall_x, wall_y), 1, 0):
                self._process_neighbors((wall_x, wall_y), (-1, 0), (1, 0))
            if self.is_valid((wall_x, wall_y), 0, 1) and self.is_valid((wall_x, wall_y), 0, -1):
                self._process_neighbors((wall_x, wall_y), (0, -1), (0, 1))
            self.walls_list.remove((wall_x, wall_y))
            if self.show_maze:
                self._display_maze()
        plt.pause(5)
        self._convert_to_maze()
        return self.maze
    def _process_neighbors(self, wall, dir1, dir2):
        neighbor1 = (wall[0] + dir1[0], wall[1] + dir1[1])
        neighbor2 = (wall[0] + dir2[0], wall[1] + dir2[1])
        if self.grid[neighbor1] == 1 and self.grid[neighbor2] == -1:
            self.grid[wall] = 1
            self.grid[neighbor2] = 1
            self.add_neighbors(neighbor2)
        elif self.grid[neighbor1] == -1 and self.grid[neighbor2] == 1:
            self.grid[wall] = 1
            self.grid[neighbor1] = 1
            self.add_neighbors(neighbor1)
    def _display_maze(self):
        plt.figure(1)
        plt.clf()
        plt.imshow(self.grid, cmap='gray')
        plt.title('Maze')
        plt.pause(0.005)
    def _convert_to_maze(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row, col] == 1:
                    self.maze[row, col] = True
if __name__ == "__main__":
    size = int(input("Enter size of maze (example: 10): "))
    start = (0, 0)
    obj = PrimsMaze(size)
    maze = obj.create_maze(start).tolist()
    plt.figure(figsize=(10, 5))
    plt.imshow(maze, interpolation='nearest', cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.show()
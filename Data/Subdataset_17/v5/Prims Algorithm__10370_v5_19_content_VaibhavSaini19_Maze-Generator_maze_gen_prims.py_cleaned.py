import numpy as np
import matplotlib.pyplot as plt
class PrimsMaze:
    def __init__(self, size=25, show_maze=True):
        self.size = (size
        self.show_maze = show_maze
        self.walls_list = []
        self.grid = np.full((self.size, self.size), -50, dtype=int)
        for i in range(size
            for j in range(size
                self.grid[i * 2, j * 2] = -1
        self.maze = np.zeros((self.size, self.size), dtype=bool)
    def is_valid(self, curr, dx, dy):
        x, y = curr
        return 0 <= x + dx < self.size and 0 <= y + dy < self.size
    def add_neighbors(self, curr):
        nearby = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dx, dy in nearby:
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
                top = (wall_x - 1, wall_y)
                bottom = (wall_x + 1, wall_y)
                if self.grid[top] == 1 and self.grid[bottom] == -1:
                    self.grid[wall_x, wall_y] = 1
                    self.grid[bottom] = 1
                    self.add_neighbors(bottom)
                elif self.grid[top] == -1 and self.grid[bottom] == 1:
                    self.grid[wall_x, wall_y] = 1
                    self.grid[top] = 1
                    self.add_neighbors(top)
                self.walls_list.pop(ind)
            if self.is_valid((wall_x, wall_y), 0, 1) and self.is_valid((wall_x, wall_y), 0, -1):
                left = (wall_x, wall_y - 1)
                right = (wall_x, wall_y + 1)
                if self.grid[left] == 1 and self.grid[right] == -1:
                    self.grid[wall_x, wall_y] = 1
                    self.grid[right] = 1
                    self.add_neighbors(right)
                elif self.grid[left] == -1 and self.grid[right] == 1:
                    self.grid[wall_x, wall_y] = 1
                    self.grid[left] = 1
                    self.add_neighbors(left)
                self.walls_list.pop(ind)
            if self.show_maze:
                self._display_maze_generation()
        plt.pause(5)
        self._convert_grid_to_maze()
        return self.maze
    def _display_maze_generation(self):
        plt.figure(1)
        plt.clf()
        plt.imshow(self.grid, cmap='gray')
        plt.title('Maze Generation')
        plt.pause(0.005)
    def _convert_grid_to_maze(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row, col] == 1:
                    self.maze[row, col] = True
if __name__ == "__main__":
    size = int(input("Enter size of maze (example: 10): "))
    start = (0, 0)
    maze_generator = PrimsMaze(size)
    maze = maze_generator.create_maze(start)

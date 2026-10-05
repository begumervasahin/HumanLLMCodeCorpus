import numpy as np
from numpy.random import randint as rand
def generate_maze(width=81, height=51, complexity=.75, density=.75):
    shape = ((height
    total_cells = shape[0] * shape[1]
    adjusted_complexity = int(complexity * (total_cells
    adjusted_density = int(density * (total_cells
    maze_grid = np.zeros(shape, dtype=bool)
    maze_grid[0, :] = maze_grid[-1, :] = 1
    maze_grid[:, 0] = maze_grid[:, -1] = 1
    for _ in range(adjusted_density):
        start_x, start_y = rand(0, shape[1]
        maze_grid[start_y, start_x] = 1
        for _ in range(adjusted_complexity):
            neighbours = []
            for dx, dy in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
                nx, ny = start_x + dx, start_y + dy
                if 0 < nx < shape[1] and 0 < ny < shape[0] and maze_grid[ny, nx] == 0:
                    neighbours.append((ny, nx))
            if neighbours:
                new_y, new_x = neighbours[rand(0, len(neighbours) - 1)]
                maze_grid[new_y, new_x] = 1
                maze_grid[start_y + (new_y - start_y)
                start_x, start_y = new_x, new_y
    return maze_grid
maze = generate_maze()
print(maze)
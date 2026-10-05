import numpy
from numpy.random import randint as rand
def generate_maze(width=81, height=51, complexity=.75, density=.75):
    shape = ((height
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density = int(density * ((shape[0]
    maze_grid = numpy.zeros(shape, dtype=bool)
    maze_grid[0, :] = maze_grid[-1, :] = 1
    maze_grid[:, 0] = maze_grid[:, -1] = 1
    for i in range(density):
        x, y = rand(0, shape[1]
        maze_grid[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:
                neighbours.append((y, x - 2))
            if x < shape[1] - 2:
                neighbours.append((y, x + 2))
            if y > 1:
                neighbours.append((y - 2, x))
            if y < shape[0] - 2:
                neighbours.append((y + 2, x))
            if len(neighbours):
                y_, x_ = neighbours[rand(0, len(neighbours) - 1)]
                if maze_grid[y_, x_] == 0:
                    maze_grid[y_, x_] = 1
                    maze_grid[y_ + (y - y_)
                    x, y = x_, y_
    return maze_grid
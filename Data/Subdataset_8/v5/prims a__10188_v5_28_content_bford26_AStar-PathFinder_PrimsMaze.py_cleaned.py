import numpy as np
from numpy.random import randint
def initialize_maze(width, height):
    shape = (height, width)
    maze = np.zeros(shape, dtype=bool)
    maze[0, :] = maze[-1, :] = 1
    maze[:, 0] = maze[:, -1] = 1
    return maze
def add_walls(maze, start_x, start_y):
    maze[start_y, start_x] = 1
def get_neighbours(x, y, width, height):
    neighbours = []
    if x > 1:
        neighbours.append((y, x - 2))
    if x < width - 2:
        neighbours.append((y, x + 2))
    if y > 1:
        neighbours.append((y - 2, x))
    if y < height - 2:
        neighbours.append((y + 2, x))
    return neighbours
def carve_path(maze, x, y, neighbours):
    y_, x_ = neighbours[randint(0, len(neighbours) - 1)]
    if maze[y_, x_] == 0:
        maze[y_, x_] = 1
        maze[y_ + (y - y_)
        return x_, y_
    return x, y
def generate_maze(width=81, height=51, complexity=.75, density=.75):
    width = (width
    height = (height
    maze = initialize_maze(width, height)
    complexity = int(complexity * (5 * (width + height)))
    density = int(density * ((width
    for _ in range(density):
        x, y = randint(0, width
        add_walls(maze, x, y)
        for _ in range(complexity):
            neighbours = get_neighbours(x, y, width, height)
            if neighbours:
                x, y = carve_path(maze, x, y, neighbours)
    return maze
maze = generate_maze()
print(maze)
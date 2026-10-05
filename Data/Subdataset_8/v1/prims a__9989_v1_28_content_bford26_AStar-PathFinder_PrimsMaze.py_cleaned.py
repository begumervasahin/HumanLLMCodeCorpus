import numpy
from numpy.random import randint as rand
def generate_maze(width=81, height=51, complexity=.75, density=.75):
    shape = ((height
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density = int(density * ((shape[0]
    Z = numpy.zeros(shape, dtype=bool)
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    for i in range(density):
        x, y = rand(0, shape[1]
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_, x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_)
                    x, y = x_, y_
    return Z
maze = generate_maze()
print(maze)
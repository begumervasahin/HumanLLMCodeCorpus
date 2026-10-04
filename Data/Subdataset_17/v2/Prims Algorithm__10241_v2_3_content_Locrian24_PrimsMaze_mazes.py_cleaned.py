import random
class Maze:
    class Cell:
        def __init__(self, x, y):
            self.X = x
            self.Y = y
            self.Wall = True
            self.IN = False
        def get_neighbours(self, size):
            neighbours = []
            x, y = self.X, self.Y
            if x > 0:
                neighbours.append([x - 1, y])
            else:
                neighbours.append(None)
            if x + 1 < size:
                neighbours.append([x + 1, y])
            else:
                neighbours.append(None)
            if y > 0:
                neighbours.append([x, y - 1])
            else:
                neighbours.append(None)
            if y + 1 < size:
                neighbours.append([x, y + 1])
            else:
                neighbours.append(None)
            return neighbours
        def get_walls(self, size, cells):
            walls = []
            for neighbour in self.get_neighbours(size):
                if neighbour is None:
                    continue
                cell = cells[neighbour[0] + neighbour[1] * size]
                if cell.Wall:
                    walls.append(cell)
            return walls
        def opposite_is_valid(self, cells, size):
            cx, cy = -1, -1
            for neighbour in self.get_neighbours(size):
                if neighbour is None:
                    continue
                cell = cells[neighbour[0] + neighbour[1] * size]
                if cell.IN:
                    cx, cy = neighbour
                    break
            if cx == -1:
                print("No valid neighbours. SOMETHING IS WRONG?")
                return None
            nx, ny = 2 * self.X - cx, 2 * self.Y - cy
            if nx < 0 or ny < 0 or nx >= size or ny >= size:
                return None
            opposite_cell = cells[nx + ny * size]
            if not opposite_cell.IN:
                return opposite_cell
            else:
                return None
    def __init__(self, size):
        self.cells = [Maze.Cell(j, i) for i in range(size) for j in range(size)]
        x = random.randrange(1, size, 2)
        y = random.randrange(1, size, 2)
        start = self.cells[x + y * size]
        walls_list = start.get_walls(size, self.cells)
        start.IN = True
        start.Wall = False
        while walls_list:
            current_wall = random.choice(walls_list)
            cell = current_wall.opposite_is_valid(self.cells, size)
            if cell:
                current_wall.Wall = False
                cell.IN = True
                walls_list.extend(cell.get_walls(size, self.cells))
                walls_list = list(set(walls_list))
            walls_list.remove(current_wall)
    def display(self):
        size = int(len(self.cells) ** 0.5)
        maze = [['
        for cell in self.cells:
            if not cell.Wall:
                maze[cell.Y][cell.X] = ' '
        for row in maze:
            print(''.join(row))
size = 15
maze = Maze(size)
maze.display()
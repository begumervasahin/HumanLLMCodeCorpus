import random
class Maze:
    class Cell:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.is_wall = True
            self.is_in_maze = False
        def get_neighbours(self, size):
            neighbours = []
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < size and 0 <= ny < size:
                    neighbours.append((nx, ny))
                else:
                    neighbours.append(None)
            return neighbours
        def get_walls(self, size, cells):
            walls = []
            for neighbour in self.get_neighbours(size):
                if neighbour is None:
                    continue
                cell = cells[neighbour[0] + neighbour[1] * size]
                if cell.is_wall:
                    walls.append(cell)
            return walls
        def get_opposite_cell(self, cells, size):
            for neighbour in self.get_neighbours(size):
                if neighbour is None:
                    continue
                cell = cells[neighbour[0] + neighbour[1] * size]
                if cell.is_in_maze:
                    cx, cy = neighbour
                    break
            else:
                print("No valid neighbours. SOMETHING IS WRONG?")
                return None
            ox, oy = 2 * self.x - cx, 2 * self.y - cy
            if 0 <= ox < size and 0 <= oy < size:
                opposite_cell = cells[ox + oy * size]
                if not opposite_cell.is_in_maze:
                    return opposite_cell
            return None
    def __init__(self, size):
        self.size = size
        self.cells = [Maze.Cell(j, i) for i in range(size) for j in range(size)]
        start_x = random.randrange(1, size, 2)
        start_y = random.randrange(1, size, 2)
        start_cell = self.cells[start_x + start_y * size]
        walls_list = start_cell.get_walls(size, self.cells)
        start_cell.is_in_maze = True
        start_cell.is_wall = False
        while walls_list:
            current_wall = random.choice(walls_list)
            opposite_cell = current_wall.get_opposite_cell(self.cells, size)
            if opposite_cell:
                current_wall.is_wall = False
                opposite_cell.is_in_maze = True
                walls_list.extend(opposite_cell.get_walls(size, self.cells))
                walls_list = list(set(walls_list))
            walls_list.remove(current_wall)
    def display(self):
        maze = [['
        for cell in self.cells:
            if not cell.is_wall:
                maze[cell.y][cell.x] = ' '
        for row in maze:
            print(''.join(row))
size = 15
maze = Maze(size)
maze.display()
import sys
from PIL import Image
class Solver:
    def __init__(self, input_file, output_file):
        self.colors = {
            "WHITE": (255, 255, 255),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
        }
        self.output_file = output_file
        self.image = Image.open(input_file)
        self.image = self.image.convert('RGB')
        self.bitmap = self.image.load()
        self.finish, self.start_point = self.find_start_end()
    def find_start_end(self):
        x, y = self.image.size
        start = None
        end = None
        for i in range(x):
            for j in range(y):
                if self.bitmap[i, j] == (255, 0, 0):
                    end = (i, j)
                elif self.bitmap[i, j] == (0, 255, 0):
                    start = (i, j)
        if start and end:
            return end, start
        print("No start or end found")
        sys.exit(1)
    def run(self):
        solution = self.BFS(self.start_point, self.finish)
        if solution is None:
            print("No solution found")
            sys.exit(1)
        for pos in solution:
            x, y = pos
            self.bitmap[x, y] = self.colors["RED"]
        self.image.save(self.output_file)
    def is_valid_position(self, x, y):
        size_x, size_y = self.image.size
        return not (x < 0 or y < 0 or x >= size_x or y >= size_y)
    def neighbour_pixels(self, position):
        x, y = position
        return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    def BFS(self, start, end):
        image = self.image.copy()
        pixels = image.load()
        options = list()
        options.append([start])
        visited = set()
        while options:
            path = options.pop(0)
            pos = path[-1]
            visited.add(pos)
            if pos == end:
                for position in path:
                    x, y = position
                    pixels[x, y] = self.colors["RED"]
                print("Solution found")
                return path
            for x, y in self.neighbour_pixels(pos):
                if (x, y) not in visited and self.is_valid_position(x, y) and (pixels[x, y] == self.colors["WHITE"] or pixels[x, y] == self.colors["RED"]):
                    pixels[x, y] = self.colors["GREEN"]
                    new_path = list(path)
                    new_path.append((x, y))
                    options += [new_path]
        return None
if __name__ == '__main__':
    if len(sys.argv) == 3:
        solver = Solver(input_file=sys.argv[1], output_file=sys.argv[2])
        solver.run()
    else:
        print("usage: python maze_solve.py <input_file.png> <output_file.png>")
        sys.exit(1)
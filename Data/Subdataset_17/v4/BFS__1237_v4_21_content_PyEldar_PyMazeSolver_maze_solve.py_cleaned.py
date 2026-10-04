
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
        width, height = self.image.size
        start = None
        end = None
        print(width, height)
        for x in range(width):
            for y in range(height):
                if self.bitmap[x, y] == self.colors["RED"]:
                    end = (x, y)
                elif self.bitmap[x, y] == self.colors["GREEN"]:
                    start = (x, y)
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
        width, height = self.image.size
        return 0 <= x < width and 0 <= y < height
    def neighbour_pixels(self, position):
        x, y = position
        return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    def BFS(self, start, end):
        image_copy = self.image.copy()
        pixels = image_copy.load()
        queue = [[start]]
        visited = set()
        while queue:
            path = queue.pop(0)
            pos = path[-1]
            visited.add(pos)
            if pos == end:
                for position in path:
                    x, y = position
                    pixels[x, y] = self.colors["RED"]
                print("Solution found")
                return path
            for neighbor in self.neighbour_pixels(pos):
                x, y = neighbor
                if (x, y) not in visited and self.is_valid_position(x, y) and (pixels[x, y] == self.colors["WHITE"] or pixels[x, y] == self.colors["RED"]):
                    pixels[x, y] = self.colors["GREEN"]
                    new_path = list(path)
                    new_path.append((x, y))
                    queue.append(new_path)
        return None
if __name__ == '__main__':
    if len(sys.argv) == 3:
        solver = Solver(input_file=sys.argv[1], output_file=sys.argv[2])
        solver.run()
    else:
        print("Usage: python maze_solve.py <input_file.png> <output_file.png>")
        sys.exit(1)
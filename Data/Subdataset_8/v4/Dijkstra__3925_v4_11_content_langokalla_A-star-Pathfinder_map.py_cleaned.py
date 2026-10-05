class Map:
    def __init__(self, filename):
        self.filename = filename
        self.board = self._parse_map_file(filename)
        self.h = len(self.board)
        self.w = len(self.board[0])
        self.cell_size = 30
    @staticmethod
    def _parse_map_file(filename):
        with open(filename) as file:
            lines = file.read().splitlines()
        return lines
filename = "map.txt"
map_obj = Map(filename)
print("Map Dimensions:", map_obj.h, "x", map_obj.w)
print("Cell Size:", map_obj.cell_size)
print("Map Content:")
for row in map_obj.board:
    print(row)
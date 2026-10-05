class Map:
    def __init__(self, filename):
        self.filename = filename
        self.board = self._parse_map_file(filename)
        self.height, self.width = len(self.board), len(self.board[0])
        self.cell_size = 30
    @staticmethod
    def _parse_map_file(filename):
        with open(filename) as file:
            return [line.strip() for line in file]
filename = "map.txt"
map_obj = Map(filename)
print("Map Dimensions:", map_obj.height, "x", map_obj.width)
print("Cell Size:", map_obj.cell_size)
print("Map Content:")
for row in map_obj.board:
    print(row)
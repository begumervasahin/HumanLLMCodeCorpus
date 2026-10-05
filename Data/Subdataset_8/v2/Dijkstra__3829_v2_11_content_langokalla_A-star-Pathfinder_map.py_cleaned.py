class Map:
    def __init__(self, filename):
        self.filename = filename
        self.board = self._boardify_file(self._get_file(filename))
        self.height = len(self.board)
        self.width = len(self.board[0])
        self.cell_size = 30
    @staticmethod
    def _get_file(filename):
        file = open(filename)
        return file
    @staticmethod
    def _boardify_file(file):
        lines = file.read().splitlines()
        file.close()
        return lines
filename = "map.txt"
map_obj = Map(filename)
print("Map Dimensions:", map_obj.height, "x", map_obj.width)
print("Cell Size:", map_obj.cell_size)
print("Map Content:")
for row in map_obj.board:
    print(row)
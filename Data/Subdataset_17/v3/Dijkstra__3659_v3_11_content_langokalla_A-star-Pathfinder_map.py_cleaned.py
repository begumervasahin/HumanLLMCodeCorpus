from typing import List, Tuple
class Map:
    def __init__(self, filename: str):
        self.filename = filename
        self.board = self._boardify_file(self._get_file(filename))
        self.h = len(self.board)
        self.w = len(self.board[0])
        self.cell_size = 30
    @staticmethod
    def _get_file(filename: str) -> str:
        with open(filename, 'r') as file:
            return file.read()
    @staticmethod
    def _boardify_file(file_content: str) -> List[List[str]]:
        lines = file_content.splitlines()
        return [list(line) for line in lines]
if __name__ == "__main__":
    filename = 'map.txt'
    map_object = Map(filename)
    print("Map Height (cells):", map_object.h)
    print("Map Width (cells):", map_object.w)
    for row in map_object.board:
        print(''.join(row))
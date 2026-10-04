from typing import List
class Map:
    def __init__(self, filename: str):
        self.filename = filename
        self.board = self._load_board_from_file(filename)
        self.height = len(self.board)
        self.width = len(self.board[0]) if self.board else 0
        self.cell_size = 30
    @staticmethod
    def _load_file_content(filename: str) -> str:
        with open(filename, 'r') as file:
            return file.read()
    @staticmethod
    def _convert_file_to_board(file_content: str) -> List[List[str]]:
        lines = file_content.splitlines()
        return [list(line) for line in lines]
    def _load_board_from_file(self, filename: str) -> List[List[str]]:
        file_content = self._load_file_content(filename)
        return self._convert_file_to_board(file_content)
if __name__ == "__main__":
    filename = 'map.txt'
    map_object = Map(filename)
    print("Map Height (cells):", map_object.height)
    print("Map Width (cells):", map_object.width)
    for row in map_object.board:
        print(''.join(row))
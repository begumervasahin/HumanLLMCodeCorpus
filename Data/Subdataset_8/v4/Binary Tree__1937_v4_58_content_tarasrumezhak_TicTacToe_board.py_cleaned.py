class Board:
    def __init__(self):
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.last_sign = None
        self.last_pos = None
        self.tree = None
        self.user_sign = "O"
        self.computer_sign = "X"
    def check_state(self):
        def same(lst):
            for i in range(1, len(lst)):
                if lst[i] != lst[i - 1]:
                    return False
            return True
        for i in range(3):
            if same((self.board[i][0], self.board[i][1], self.board[i][2])) and self.board[i][0] is not None:
                return self.board[i][0]
            if same((self.board[0][i], self.board[1][i], self.board[2][i])) and self.board[i][0] is not None:
                return self.board[0][i]
        if same((self.board[0][0], self.board[1][1], self.board[2][2])) and self.board[2][2] is not None:
            return self.board[2][2]
        if same((self.board[2][0], self.board[1][1], self.board[0][2])) and self.board[0][2] is not None:
            return self.board[0][2]
        if not self.is_free_cell():
            return 'Draw!'
    def __str__(self):
        text = ""
        text += "------------- y:\n"
        for i in range(3):
            text += "| "
            for j in range(3):
                if self.board[i][j]:
                    text += self.board[i][j] + " | "
                else:
                    text += " " + " | "
            text += str(i + 1)
            text += "\n-------------\n"
        text += "x: 1   2   3"
        return text
    def put(self, sign, x, y):
        if 1 <= x <= 3 and 1 <= y <= 3 and self.board[x - 1][y - 1]:
            raise IndexError("The position is already used")
        try:
            self.board[x - 1][y - 1] = sign
        except IndexError:
            raise IndexError("Out of bounds")
    def check_cell(self, coords):
        return self.board[coords[0]][coords[1]] is None
    def find_empty(self):
        empty = []
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.check_cell((row, column)):
                    empty.append((row + 1, column + 1))
        return empty
    def is_free_cell(self):
        free = len(self.find_empty())
        return bool(free)
if __name__ == '__main__':
    board = Board()
    board.put("O", 1, 1)
    board.put("O", 2, 2)
    board.put("O", 3, 3)
    print(board)
    print(board.check_state())
    print(board.find_empty())
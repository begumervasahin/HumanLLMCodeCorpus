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
            return all(x == lst[0] for x in lst)
        for i in range(3):
            if same((self.board[i][0], self.board[i][1], self.board[i][2])) and self.board[i][0] is not None:
                return self.board[i][0]
            if same((self.board[0][i], self.board[1][i], self.board[2][i])) and self.board[0][i] is not None:
                return self.board[0][i]
        if same((self.board[0][0], self.board[1][1], self.board[2][2])) and self.board[0][0] is not None:
            return self.board[0][0]
        if same((self.board[2][0], self.board[1][1], self.board[0][2])) and self.board[2][0] is not None:
            return self.board[2][0]
        if not self.is_free_cell():
            return 'Draw!'
        return None
    def __str__(self):
        text = "------------- y:\n"
        for i in range(3):
            text += "| "
            for j in range(3):
                text += (self.board[i][j] or " ") + " | "
            text += f"{i + 1}\n-------------\n"
        text += "x: 1   2   3"
        return text
    def put(self, sign, x, y):
        if not (1 <= x <= 3 and 1 <= y <= 3):
            raise IndexError("Out of bounds")
        if self.board[x - 1][y - 1] is not None:
            raise IndexError("The position is already used")
        self.board[x - 1][y - 1] = sign
    def check_cell(self, coords):
        row, col = coords
        return self.board[row][col] is None
    def find_empty(self):
        empty = [(row + 1, col + 1) for row in range(3) for col in range(3) if self.check_cell((row, col))]
        return empty
    def is_free_cell(self):
        return any(self.check_cell((row, col)) for row in range(3) for col in range(3))
if __name__ == '__main__':
    board = Board()
    board.put("O", 1, 1)
    board.put("O", 2, 2)
    board.put("O", 3, 3)
    print(board)
    print(board.check_state())
    print(board.find_empty())
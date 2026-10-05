class TicTacToeBoard:
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
        def all_same(lst):
            return all(elem == lst[0] for elem in lst)
        for i in range(3):
            if all_same(self.board[i]) and self.board[i][0] is not None:
                return self.board[i][0]
            if all_same([self.board[j][i] for j in range(3)]) and self.board[0][i] is not None:
                return self.board[0][i]
        if all_same([self.board[i][i] for i in range(3)]) and self.board[1][1] is not None:
            return self.board[1][1]
        if all_same([self.board[2-i][i] for i in range(3)]) and self.board[0][2] is not None:
            return self.board[0][2]
        if not self.is_free_cell():
            return 'Draw!'
    def __str__(self):
        text = "------------- y:\n"
        for i in range(3):
            text += "| "
            for j in range(3):
                if self.board[i][j]:
                    text += self.board[i][j] + " | "
                else:
                    text += " " + " | "
            text += str(i + 1) + "\n-------------\n"
        text += "x: 1   2   3"
        return text
    def put(self, sign, x, y):
        if not (1 <= x <= 3 and 1 <= y <= 3):
            raise IndexError("Out of bounds")
        if self.board[x - 1][y - 1]:
            raise IndexError("The position is already used")
        self.board[x - 1][y - 1] = sign
    def check_cell(self, coords):
        return self.board[coords[0]][coords[1]] is None
    def find_empty(self):
        return [(i + 1, j + 1) for i in range(3) for j in range(3) if self.check_cell((i, j))]
    def is_free_cell(self):
        return any(self.check_cell((i, j)) for i in range(3) for j in range(3))
if __name__ == '__main__':
    board = TicTacToeBoard()
    board.put("O", 1, 1)
    board.put("O", 2, 2)
    board.put("O", 3, 3)
    print(board)
    print(board.check_state())
    print(board.find_empty())
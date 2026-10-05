class TicTacToeBoard:
    def __init__(self):
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
    def check_state(self):
        def all_same(lst):
            for i in range(1, len(lst)):
                if lst[i] != lst[i - 1]:
                    return False
            return True
        for i in range(3):
            if all_same((self.board[i][0], self.board[i][1], self.board[i][2])) and self.board[i][0] is not None:
                return self.board[i][0]
            if all_same((self.board[0][i], self.board[1][i], self.board[2][i])) and self.board[i][0] is not None:
                return self.board[0][i]
        if all_same((self.board[0][0], self.board[1][1], self.board[2][2])) and self.board[2][2] is not None:
            return self.board[2][2]
        if all_same((self.board[2][0], self.board[1][1], self.board[0][2])) and self.board[0][2] is not None:
            return self.board[0][2]
        if not self.is_board_full():
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
    def place_sign(self, sign, x, y):
        if not (1 <= x <= 3 and 1 <= y <= 3):
            raise IndexError("Invalid position, must be between (1,1) and (3,3)")
        if self.board[x - 1][y - 1]:
            raise IndexError("Position already used")
        self.board[x - 1][y - 1] = sign
    def is_cell_empty(self, coords):
        return self.board[coords[0]][coords[1]] is None
    def find_empty_cells(self):
        empty_cells = []
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.is_cell_empty((row, column)):
                    empty_cells.append((row + 1, column + 1))
        return empty_cells
    def is_board_full(self):
        return len(self.find_empty_cells()) == 0
if __name__ == '__main__':
    ttt_board = TicTacToeBoard()
    ttt_board.place_sign("O", 1, 1)
    ttt_board.place_sign("O", 2, 2)
    ttt_board.place_sign("O", 3, 3)
    print(ttt_board)
    print(ttt_board.check_state())
    print(ttt_board.find_empty_cells())
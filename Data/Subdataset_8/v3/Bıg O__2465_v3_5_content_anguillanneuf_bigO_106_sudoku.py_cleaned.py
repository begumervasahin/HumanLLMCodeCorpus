def update_cell(row, col, board):
    choices = []
    for k in [str(v) for v in range(1, 10)]:
        if is_valid_choice(row, col, k, board):
            choices.append(k)
    return choices
def is_valid_choice(row, col, value, board):
    for y in range(9):
        if board[row][y] == value or \
           board[y][col] == value or \
           board[row - row % 3 + y
            return False
    return True
def print_board(board):
    for row in board:
        print(" ".join(row))
def sudoku_solve(board):
    row, col = find_empty_cell(board)
    if row == -1 and col == -1:
        print_board(board)
        return True
    choices = update_cell(row, col, board)
    for value in choices:
        board[row][col] = value
        if sudoku_solve(board):
            return True
        board[row][col] = '.'
    return False
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return i, j
    return -1, -1
board1 = [[".","8","9",".","4",".","6",".","5"],
          [".","7",".",".",".","8",".","4","1"],
          ["5","6",".","9",".",".",".",".","8"],
          [".",".",".","7",".","5",".","9","."],
          [".","9",".","4",".","1",".","5","."],
          [".","3",".","9",".","6",".","1","."],
          ["8",".",".",".",".",".",".",".","7"],
          [".","2",".","8",".",".",".","6","."],
          [".",".","6",".","7",".",".","8","."]]
print("Solving board1:")
sudoku_solve(board1)
board2 = [[".",".",".","7",".",".","3",".","1"],
          ["3",".",".","9",".",".",".",".","."],
          [".","4",".","3","1",".","2",".","."],
          [".","6",".","4",".",".","5",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".","1",".",".","8",".","4","."],
          [".",".","6",".","2","1",".","5","."],
          [".",".",".",".",".","9",".",".","8"],
          ["8",".","5",".",".","4",".",".","."]]
print("Solving board2:")
sudoku_solve(board2)
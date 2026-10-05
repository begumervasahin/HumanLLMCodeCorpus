def update_cell(row, col, board):
    choices = []
    for k in [str(v) for v in range(1, 10)]:
        collision = False
        for y in range(9):
            if board[row][y] == k or \
               board[y][col] == k or \
               board[row - row % 3 + y
                collision = True
                break
        if not collision:
            choices.append(k)
    return choices
def print_board(board):
    for row in board:
        print(" ".join(row))
def sudoku_solve(board):
    choices = None
    row = -1
    col = -1
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                temp = update_cell(i, j, board)
                if choices is None or (len(temp) > 0 and len(temp) < len(choices)):
                    choices = temp
                    row = i
                    col = j
    if choices is None:
        print_board(board)
        return True
    for v in choices:
        board[row][col] = v
        if sudoku_solve(board):
            return True
        board[row][col] = '.'
    return False
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
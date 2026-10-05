def fonk1(b3, b2, board):
    b1 = []
    for k in [str(v) for v in range(1, 10)]:
        if fonk2(b3, b2, k, board):
            b1.append(k)
    return b1
def fonk2(b3, b2, value, board):
    for y in range(9):
        if board[b3][y] == value or \
           board[y][b2] == value or \
           board[b3 - b3 % 3 + y
            return False
    return True
def fonk3(board):
    for b3 in board:
        print(" ".join(b3))
def fonk4(board):
    b3, b2 = fonk5(board)
    if b3 = = -1 and b2 == -1:
        fonk3(board)
        return True
    b1 = fonk1(b3, b2, board)
    for value in b1:
        board[b3][b2] = value
        if fonk4(board):
            return True
        board[b3][b2] = '.'
    return False
def fonk5(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return i, j
    return -1, -1
b4 = [[".","8","9",".","4",".","6",".","5"],
          [".","7",".",".",".","8",".","4","1"],
          ["5","6",".","9",".",".",".",".","8"],
          [".",".",".","7",".","5",".","9","."],
          [".","9",".","4",".","1",".","5","."],
          [".","3",".","9",".","6",".","1","."],
          ["8",".",".",".",".",".",".",".","7"],
          [".","2",".","8",".",".",".","6","."],
          [".",".","6",".","7",".",".","8","."]]
print("Solving b4:")
fonk4(b4)
b5 = [[".",".",".","7",".",".","3",".","1"],
          ["3",".",".","9",".",".",".",".","."],
          [".","4",".","3","1",".","2",".","."],
          [".","6",".","4",".",".","5",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".","1",".",".","8",".","4","."],
          [".",".","6",".","2","1",".","5","."],
          [".",".",".",".",".","9",".",".","8"],
          ["8",".","5",".",".","4",".",".","."]]
print("Solving b5:")
fonk4(b5)
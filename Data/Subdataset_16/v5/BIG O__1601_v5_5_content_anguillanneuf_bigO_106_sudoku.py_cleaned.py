
def fonk1(row, b2, board):
    b1 = []
    for k in [str(v) for v in range(1, 10)]:
        if fonk2(row, b2, k, board):
            b1.append(k)
    return b1
def fonk2(row, b2, value, board):
    for y in range(9):
        if (board[row][y] == value or
            board[y][b2] == value or
            board[row - row % 3 + y
            return False
    return True
def fonk3(board):
    for row in board:
        print(" ".join(row))
    print()
def fonk4(board):
    row, b2, b1 = fonk5(board)
    if b1 is None:
        fonk3(board)
        return True
    for value in b1:
        board[row][b2] = value
        if fonk4(board):
            return True
        board[row][b2] = '.'
    return False
def fonk5(board):
    b1 = None
    row, b2 = -1, -1
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                b3 = fonk1(i, j, board)
                if b1 is None or (len(b3) > 0 and len(b3) < len(b1)):
                    b1 = b3
                    row, b2 = i, j
    return row, b2, b1
b4 = [
    [".", "8", "9", ".", "4", ".", "6", ".", "5"],
    [".", "7", ".", ".", ".", "8", ".", "4", "1"],
    ["5", "6", ".", "9", ".", ".", ".", ".", "8"],
    [".", ".", ".", "7", ".", "5", ".", "9", "."],
    [".", "9", ".", "4", ".", "1", ".", "5", "."],
    [".", "3", ".", "9", ".", "6", ".", "1", "."],
    ["8", ".", ".", ".", ".", ".", ".", ".", "7"],
    [".", "2", ".", "8", ".", ".", ".", "6", "."],
    [".", ".", "6", ".", "7", ".", ".", "8", "."]
]
b5 = [
    [".", ".", ".", "7", ".", ".", "3", ".", "1"],
    ["3", ".", ".", "9", ".", ".", ".", ".", "."],
    [".", "4", ".", "3", "1", ".", "2", ".", "."],
    [".", "6", ".", "4", ".", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "1", ".", ".", "8", ".", "4", "."],
    [".", ".", "6", ".", "2", "1", ".", "5", "."],
    [".", ".", ".", ".", ".", "9", ".", ".", "8"],
    ["8", ".", "5", ".", ".", "4", ".", ".", "."]
]
print("Solving b4:")
fonk4(b4)
print("Solving b5:")
fonk4(b5)
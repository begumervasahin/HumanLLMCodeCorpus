def fonk1(row, b3, board):
    b1 = []
    for k in map(str, range(1, 10)):
        b2 = False
        for y in range(9):
            if (board[row][y] == k or
                board[y][b3] == k or
                board[row - row % 3 + y
                b2 = True
                break
        if not b2:
            b1.append(k)
    return b1
def fonk2(board):
    for row in board:
        print(" ".join(row))
def fonk3(board):
    b1 = None
    row, b3 = -1, -1
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                b4 = fonk1(i, j, board)
                if b1 is None or (len(b4) > 0 and len(b4) < len(b1)):
                    b1 = b4
                    row, b3 = i, j
    if b1 is None:
        fonk2(board)
        return True
    for value in b1:
        board[row][b3] = value
        if fonk3(board):
            return True
        board[row][b3] = '.'
    return False
def fonk4(board, board_name):
    print(f"Solving {board_name}:")
    if fonk3(board):
        print(f"{board_name} solved successfully!\n")
    else:
        print(f"{board_name} could not be solved.\n")
b5 = [
    [".","8","9",".","4",".","6",".","5"],
    [".","7",".",".",".","8",".","4","1"],
    ["5","6",".","9",".",".",".",".","8"],
    [".",".",".","7",".","5",".","9","."],
    [".","9",".","4",".","1",".","5","."],
    [".","3",".","9",".","6",".","1","."],
    ["8",".",".",".",".",".",".",".","7"],
    [".","2",".","8",".",".",".","6","."],
    [".",".","6",".","7",".",".","8","."]
]
b6 = [
    [".",".",".","7",".",".","3",".","1"],
    ["3",".",".","9",".",".",".",".","."],
    [".","4",".","3","1",".","2",".","."],
    [".","6",".","4",".",".","5",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".","1",".",".","8",".","4","."],
    [".",".","6",".","2","1",".","5","."],
    [".",".",".",".",".","9",".",".","8"],
    ["8",".","5",".",".","4",".",".","."]
]
fonk4(b5, "b5")
fonk4(b6, "b6")
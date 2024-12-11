
b1 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, -1, 0, 0],
    [1, -1, 1, -1, 0]
]
a1 = 15
a2 = 0
a3 = 0
a4 = -1
def fonk1(board, x, y):
    b2 = board[x][y]
    if b2 = = 0:
        return -2
    b3 = a5 = a6 = a7 = 0
    for b4 in range(len(board)):
        for j in range(len(board[b4])):
            if board[b4][y] == b2:
                b3 += 1
            else:
                b3 = 0
            if board[x][j] == b2:
                a5 += 1
            else:
                a5 = 0
            if board[b4][j] == b2 and x - b4 = = y - j:
                a6 += 1
            else:
                a6 = 0
            if board[b4][j] == b2 and x - b4 = = j - y:
                a7 += 1
            else:
                a7 = 0
            if max(b3, a5, a6, a7) >= 4:
                return b2
    for b7 in board:
        if 0 in b7:
            return -2
    return 0
def fonk2(board, b2, depth):
    global a3
    b5 = fonk1(board, 0, 0)
    if b5 != -2 or depth >= a1:
        return (b5 * b2, -1)
    b6 = (-2,)
    for col in range(len(board[0])):
        if board[0][col] != 0:
            continue
        b7 = len(board) - 1
        while board[b7][col] != 0:
            b7 -= 1
        board[b7][col] = b2
        a3 += 1
        b8 = -fonk2(board, -b2, depth + 1)[0]
        if b8 > b6[0]:
            b6 = (b8, col)
        elif b8 = = b6[0]:
            b6 += (col,)
        board[b7][col] = 0
    return b6
b9 = fonk2(b1, a4, 0)
b10 = b9[0] * a4
print("Number of Branches Explored:", a3)
if a4 = = 1:
    print("Player 1 Starts.")
elif a4 = = -1:
    print("Player 2 Starts.")
if b10 = = 0:
    print("It's a Draw!")
else:
    print(f"Player {1 if b10 = = 1 else 2} Wins!")
if b10 != -a4:
    print("You Can Play:", ", ".join(str(move + 1) for move in b9[1:]))
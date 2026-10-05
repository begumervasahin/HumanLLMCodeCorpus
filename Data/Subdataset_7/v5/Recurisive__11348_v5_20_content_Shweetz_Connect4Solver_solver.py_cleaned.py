
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
def fonk1(board, b7, celly):
    a4 = board[b7][celly]
    if a4 = = 0:
        return -2
    def fonk2(dx, dy):
        a5 = 0
        while 0 <= b7 + dx < len(board) and 0 <= celly + dy < len(board[0]) and board[b7 + dx][celly + dy] == a4:
            a5 += 1
            b7 += dx
            celly += dy
        return a5
    for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        b2 = 1 + fonk2(dx, dy) + fonk2(-dx, -dy)
        if b2 >= 4:
            return a4
    if all(board[0][j] != 0 for j in range(len(board[0]))):
        return -1
    return 0
def fonk3(board, a4, b7, celly, b4):
    b3 = fonk1(board, b7, celly)
    if b3 != -2:
        return (b3 * a4, -1, -1)
    if b4 = = 0:
        return (0, -1, -1)
    b5 = float('-inf') if a4 == 1 else float('inf')
    b6 = []
    for celly in range(len(board[0])):
        if board[0][celly] != 0:
            continue
        b7 = len(board) - 1
        while board[b7][celly] != 0:
            b7 -= 1
        board[b7][celly] = a4
        global a3
        a3 += 1
        b9, b8, b8 = fonk3(board, -a4, b7, celly, b4 - 1)
        board[b7][celly] = 0
        if a4 = = 1:
            if b9 > b5:
                b5 = b9
                b6 = [celly]
            elif b9 = = b5:
                b6.append(celly)
        else:
            if b9 < b5:
                b5 = b9
                b6 = [celly]
            elif b9 = = b5:
                b6.append(celly)
    return b5 * a4, b6[0], b6[1:]
b9, best_move, b10 = fonk3(b1, a4, 0, 0, a1)
print("Number of branches explored:", a3)
if a4 = = 1:
    print("Player 1 starts.")
elif a4 = = -1:
    print("Player 2 starts.")
if b9 = = 0:
    print("It's a draw!")
else:
    b11 = 1 if b9 > 0 else 2
    print("Player", b11, "wins!")
    print("You can play", best_move + 1, b12 = '')
    for move in b10:
        print(",", move + 1, b12 = '')
    print()
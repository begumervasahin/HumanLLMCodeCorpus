
b1 = [[0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 1, -1, 0, 0],
              [1, -1, 1, -1, 0]]
a1 = 15
a2 = 0
a3 = 0
a4 = -1
def fonk1(board, b5, y):
    b2 = board[b5][y]
    if b2 = = 0:
        return -2
    a5 = 0
    for i in range(len(board)):
        if board[i][y] == b2:
            a5 += 1
        else:
            a5 = 0
        if a5 >= 4:
            return b2
    a6 = 0
    for j in range(len(board[0])):
        if board[b5][j] == b2:
            a6 += 1
        else:
            a6 = 0
        if a6 >= 4:
            return b2
    a7 = 0
    for i, j in zip(range(b5, -1, -1), range(y, len(board[0]))):
        if board[i][j] == b2:
            a7 += 1
        else:
            a7 = 0
        if a7 >= 4:
            return b2
    a8 = 0
    for i, j in zip(range(b5, -1, -1), range(y, -1, -1)):
        if board[i][j] == b2:
            a8 += 1
        else:
            a8 = 0
        if a8 >= 4:
            return b2
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return -2
    return 0
def fonk2(board, b2, b5, y, depth):
    global a3
    b3 = fonk1(board, b5, y)
    if b3 != -2:
        if depth < a2:
            print("\t" * depth + "End State: " + str(b3))
        return (b3 * b2, -1, -1)
    if depth > a1 - 1:
        return (0, -1, -1)
    b4 = [-2]
    for y in range(len(board[0])):
        if board[0][y] != 0:
            continue
        b5 = len(board) - 1
        while board[b5][y] != 0:
            b5 -= 1
        board[b5][y] = b2
        a3 += 1
        b6 = -fonk2(board, -b2, b5, y, depth + 1)[0]
        if b6 > b4[0]:
            b4 = [b6, y]
        elif b6 = = b4[0]:
            b4.append(y)
        board[b5][y] = 0
    return b4
b7 = fonk2(b1, a4, 0, 0, 0)
b8 = b7[0] * a4
print("Number of Branches Explored: " + str(a3))
if a4 = = 1:
    print("Player 1 Starts.")
elif a4 = = -1:
    print("Player 2 Starts.")
if b8 = = 0:
    print("It's a Draw!")
else:
    b9 = int(b8 * -0.5 + 1.5)
    print("Player " + str(b9) + " Wins!")
b10 = str(b7[1] + 1)
for i in range(2, len(b7)):
    b10 += ", " + str(b7[i] + 1)
if b8 != -a4:
    print("You Can Play: " + b10)
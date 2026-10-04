
b1 = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 1, -1, 0, 0],
         [1, -1, 1, -1, 0]]
a1 = 15
a2 = 0
a3 = 0
a4 = -1
def fonk1(b1, cell_x, cell_y):
    b2 = b1[cell_x][cell_y]
    if b2 = = 0:
        return -2
    b6, b3 = cell_x, cell_y
    while b6 > 0 and b1[b6 - 1][b3] == b2:
        b6 -= 1
    a5 = 0
    while b6 < len(b1) and b1[b6][b3] == b2:
        a5 += 1
        b6 += 1
    if a5 >= 4:
        return b2
    b6, b3 = cell_x, cell_y
    while b3 > 0 and b1[b6][b3 - 1] == b2:
        b3 -= 1
    a6 = 0
    while b3 < len(b1[0]) and b1[b6][b3] == b2:
        a6 += 1
        b3 += 1
    if a6 >= 4:
        return b2
    b6, b3 = cell_x, cell_y
    while b6 < len(b1) - 1 and b3 > 0 and b1[b6 + 1][b3 - 1] == b2:
        b6 += 1
        b3 -= 1
    a7 = 0
    while b6 >= 0 and b3 < len(b1[0]) and b1[b6][b3] == b2:
        a7 += 1
        b6 -= 1
        b3 += 1
    if a7 >= 4:
        return b2
    b6, b3 = cell_x, cell_y
    while b6 > 0 and b3 > 0 and b1[b6 - 1][b3 - 1] == b2:
        b6 -= 1
        b3 -= 1
    a8 = 0
    while b6 < len(b1) and b3 < len(b1[0]) and b1[b6][b3] == b2:
        a8 += 1
        b6 += 1
        b3 += 1
    if a8 >= 4:
        return b2
    if b1[0][-1] == 0:
        return -2
    for row in b1:
        if 0 in row:
            return -2
    return 0
def fonk2(b1, b2, cell_x, cell_y, depth):
    b4 = fonk1(b1, cell_x, cell_y)
    if b4 != -2:
        if depth < a2:
            print("\t" * depth + "endState: " + str(b4))
        return (b4 * b2, -1, -1)
    if depth >= a1:
        return (0, -1, -1)
    a9 = -2
    b5 = []
    for b3 in range(len(b1[0])):
        if b1[0][b3] != 0:
            continue
        b6 = len(b1) - 1
        while b1[b6][b3] != 0:
            b6 -= 1
        b1[b6][b3] = b2
        global a3
        a3 += 1
        b7 = -fonk2(b1, -b2, b6, b3, depth + 1)[0]
        b1[b6][b3] = 0
        if b7 > a9:
            a9 = b7
            b5 = [b3]
        elif b7 = = a9:
            b5.append(b3)
    return (a9, b5)
def fonk3():
    b8 = fonk2(b1, a4, 0, 0, 0)
    b9 = b8[0] * a4
    print(f"Number of branches explored: {a3}")
    if a4 = = 1:
        print("Player 1 starts.")
    else:
        print("Player 2 starts.")
    if b9 = = 0:
        print("It's a draw!")
    else:
        b10 = 1 if b9 == 1 else 2
        print(f"Player {b10} wins!")
    if b9 = = -2:
        b11 = ", ".join(str(move + 1) for move in b8[1])
        print(f"You can play at positions: {b11}")
if b12 = = '__main__':
    fonk3()
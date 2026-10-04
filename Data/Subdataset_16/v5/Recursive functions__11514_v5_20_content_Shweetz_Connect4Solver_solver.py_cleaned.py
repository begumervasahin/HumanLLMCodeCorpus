b1 = [[0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, -1, 0, 0],
       [1, -1, 1, -1, 0]]
a1 = 15
a2 = 0
a3 = 0
a4 = -1
def fonk1(b1, b6, celly):
    b2 = b1[b6][celly]
    if b2 = = 0:
        return -2
    def fonk2(dx, dy):
        x, b3 = b6, celly
        a5 = 0
        while 0 <= x < len(b1) and 0 <= b3 < len(b1[0]) and b1[x][b3] == b2:
            a5 += 1
            x += dx
            b3 += dy
        return a5
    if fonk2(1, 0) + fonk2(-1, 0) - 1 >= 4:
        return b2
    if fonk2(0, 1) + fonk2(0, -1) - 1 >= 4:
        return b2
    if fonk2(1, -1) + fonk2(-1, 1) - 1 >= 4:
        return b2
    if fonk2(1, 1) + fonk2(-1, -1) - 1 >= 4:
        return b2
    if all(cell != 0 for row in b1 for cell in row):
        return 0
    return -2
def fonk3(b1, a4, b6, celly, depth):
    b4 = fonk1(b1, b6, celly)
    if b4 != -2:
        if depth < a2:
            print("\t" * depth + "endState: " + str(b4))
        return b4 * a4, -1, -1
    if depth >= a1:
        return 0, -1, -1
    b5 = [-2]
    for celly in range(len(b1[0])):
        if b1[0][celly] != 0:
            continue
        b6 = len(b1) - 1
        while b1[b6][celly] != 0:
            b6 -= 1
        b1[b6][celly] = a4
        global a3
        a3 += 1
        b7 = -fonk3(b1, -a4, b6, celly, depth + 1)[0]
        if b7 > b5[0]:
            b5 = [b7, celly]
        elif b7 = = b5[0]:
            b5.append(celly)
        b1[b6][celly] = 0
    return b5
def fonk4():
    b8 = fonk3(b1, a4, 0, 0, 0)
    b9 = b8[0] * a4
    print(f"Number of branches explored: {a3}")
    if a4 = = 1:
        print("Player 1 starts.")
    elif a4 = = -1:
        print("Player 2 starts.")
    if b9 = = 0:
        print("It's a draw!")
    else:
        b10 = int(b9 * -0.5 + 1.5)
        print(f"Player {b10} wins!")
    if b9 != -a4:
        b11 = ", ".join(str(c + 1) for c in b8[1:])
        print(f"You can play {b11}")
if b12 = = "__main__":
    fonk4()
b1 = [[0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, -1, 0, 0],
       [1, -1, 1, -1, 0]]
a1 = 15
a2 = 0
a3 = 0
a4 = -1
def fonk1(b1, b5, celly):
    a4 = b1[b5][celly]
    if a4 = = 0:
        return -2
    def fonk2(dx, dy):
        x, b2 = b5, celly
        a5 = 0
        while 0 <= x < len(b1) and 0 <= b2 < len(b1[0]) and b1[x][b2] == a4:
            a5 += 1
            x += dx
            b2 += dy
        return a5
    if fonk2(1, 0) + fonk2(-1, 0) - 1 >= 4:
        return a4
    if fonk2(0, 1) + fonk2(0, -1) - 1 >= 4:
        return a4
    if fonk2(1, -1) + fonk2(-1, 1) - 1 >= 4:
        return a4
    if fonk2(1, 1) + fonk2(-1, -1) - 1 >= 4:
        return a4
    if all(cell != 0 for row in b1 for cell in row):
        return 0
    return -2
def fonk3(b1, a4, b5, celly, t):
    b3 = fonk1(b1, b5, celly)
    if b3 != -2:
        if t < a2:
            print("\t" * t + "endState: " + str(b3))
        return b3 * a4, -1, -1
    if t > a1 - 1:
        return 0, -1, -1
    b4 = [-2]
    for celly in range(len(b1[0])):
        if b1[0][celly] != 0:
            continue
        b5 = len(b1) - 1
        while b1[b5][celly] != 0:
            b5 -= 1
        b1[b5][celly] = a4
        global a3
        a3 += 1
        b6 = -fonk3(b1, -a4, b5, celly, t + 1)[0]
        if b6 > b4[0]:
            b4 = [b6, celly]
        elif b6 = = b4[0]:
            b4.append(celly)
        b1[b5][celly] = 0
    return b4
def fonk4():
    b7 = fonk3(b1, a4, 0, 0, 0)
    b8 = b7[0] * a4
    print("Number of branches explored: " + str(a3))
    if a4 = = 1:
        print("Player 1 starts.")
    elif a4 = = -1:
        print("Player 2 starts.")
    if b8 = = 0:
        print("It's a draw!")
    else:
        b9 = int(b8 * -0.5 + 1.5)
        print(f"Player {b9} wins!")
    b10 = ", ".join(str(c + 1) for c in b7[1:])
    if b8 != -a4:
        print(f"You can play {b10}")
if b11 = = "__main__":
    fonk4()
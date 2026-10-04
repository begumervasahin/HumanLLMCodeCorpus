b1 = [[0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, -1, 0, 0],
       [1, -1, 1, -1, 0]]
a1 = 15
a2 = 0
a3 = 0
a4 = -1
def fonk1(b1, b6, celly):
    a4 = b1[b6][celly]
    if a4 = = 0:
        return -2
    b2 = b6
    b3 = celly
    while b2 > 0 and b1[b2-1][b3] == a4:
        b2 -= 1
    a5 = 0
    while b2 < len(b1) and b1[b2][b3] == a4:
        a5 += 1
        b2 += 1
    if a5 >= 4:
        return a4
    b2 = b6
    b3 = celly
    while b3 > 0 and b1[b2][b3-1] == a4:
        b3 -= 1
    a6 = 0
    while b3 < len(b1[0]) and b1[b2][b3] == a4:
        a6 += 1
        b3 += 1
    if a6 >= 4:
        return a4
    b2 = b6
    b3 = celly
    while b2 < len(b1) - 1 and b3 > 0 and b1[b2+1][b3-1] == a4:
        b2 += 1
        b3 -= 1
    a7 = 0
    while b2 >= 0 and b3 < len(b1[0]) and b1[b2][b3] == a4:
        a7 += 1
        b2 -= 1
        b3 += 1
    if a7 >= 4:
        return a4
    b2 = b6
    b3 = celly
    while b2 > 0 and b3 > 0 and b1[b2-1][b3-1] == a4:
        b2 -= 1
        b3 -= 1
    a8 = 0
    while b2 < len(b1) and b3 < len(b1[0]) and b1[b2][b3] == a4:
        a8 += 1
        b2 += 1
        b3 += 1
    if a8 >= 4:
        return a4
    if b1[0][len(b1[0])-1] == 0:
        return -2
    for a9 in range(len(b1)):
        for j in range(len(b1[a9])):
            if b1[a9][j] == 0:
                return -2
    return 0
def fonk2(b1, a4, b6, celly, t):
    b4 = fonk1(b1, b6, celly)
    if b4 != -2:
        if t < a2:
            print("\t"*t + "endState: " + str(b4))
        return (b4 * a4, -1, -1)
    if t > a1 - 1:
        return (0, -1, -1)
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
        b7 = -fonk2(b1, -a4, b6, celly, t + 1)[0]
        if b7 > b5[0]:
            b5 = [b7, celly]
        elif b7 = = b5[0]:
            b5.append(celly)
        b1[b6][celly] = 0
    return b5
b8 = fonk2(b1, a4, 0, 0, 0)
b9 = b8[0] * a4
print("Number of branches explored: " + str(a3))
if a4 = = 1:
    print("Player 1 start.")
elif a4 = = -1:
    print("Player 2 start.")
if b9 = = 0:
    print("It's a draw!")
else:
    b10 = int(b9 * -0.5 + 1.5)
    print("Player " + str(b10) + " wins!")
b11 = str(b8[1] + 1)
a9 = 2
while a9 < len(b8):
    b11 += ", " + str(b8[a9] + 1)
    a9 += 1
if b9 != -a4:
    print("You can play " + b11)
b1 = [0, 0, 0,
       0, 0, 0,
       0, 0, 0]
a1 = 1
b2 = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
def fonk1(b1):
    for b3 in b2:
        if b1[b3[0]] == 1 and b1[b3[1]] == 1 and b1[b3[2]] == 1:
            return 1
        if b1[b3[0]] == -1 and b1[b3[1]] == -1 and b1[b3[2]] == -1:
            return -1
    if b1[8] == 0:
        return -2
    for b3 in b1:
        if b3 = = 0:
            return -2
    return 0
def fonk2(b1, a1, t):
    b4 = fonk1(b1)
    if b4 != -2:
        return (b4 * a1, -1)
    b5 = [-2]
    for cell in range(len(b1)):
        if b1[cell] == 0:
            b1[cell] = a1
            b6 = -fonk2(b1, -a1, t + 1)[0]
            if b6 > b5[0]:
                b5 = [b6, cell]
            elif b6 = = b5[0]:
                b5.append(cell)
            b1[cell] = 0
    return b5
b7 = fonk2(b1, a1, 0)
b8 = b7[0] * a1
if a1 = = 1:
    print("Player 1 starts.")
elif a1 = = -1:
    print("Player 2 starts.")
if b8 = = 0:
    print("It's a draw!")
else:
    b9 = int(b8 * -0.5 + 1.5)
    print("Player " + str(b9) + " wins!")
b10 = str(b7[1] + 1)
for b3 in range(2, len(b7)):
    b10 += ", " + str(b7[b3] + 1)
if b8 != -a1:
    print("You can play in position(s): " + b10)
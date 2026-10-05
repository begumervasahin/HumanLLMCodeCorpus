
b1 = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
def fonk1(b5):
    for combination in b1:
        if all(b5[i] == 1 for i in combination):
            return 1
        if all(b5[i] == -1 for i in combination):
            return -1
    if 0 in b5:
        return -2
    return 0
def fonk2(b5, a1, turn):
    b2 = fonk1(b5)
    if b2 != -2:
        return b2 * a1, -1
    b3 = [-2]
    for cell in range(len(b5)):
        if b5[cell] == 0:
            b5[cell] = a1
            b4 = -fonk2(b5, -a1, turn + 1)[0]
            if b4 > b3[0]:
                b3 = [b4, cell]
            elif b4 = = b3[0]:
                b3.append(cell)
            b5[cell] = 0
    return b3
def fonk3(b5):
    for i in range(0, 9, 3):
        print(b5[i:i+3])
b5 = [0] * 9
a1 = 1
b6 = fonk2(b5, a1, 0)
b7 = b6[0] * a1
if a1 = = 1:
    print("Player 1 starts.")
elif a1 = = -1:
    print("Player 2 starts.")
if b7 = = 0:
    print("It's a draw!")
else:
    b8 = int(b7 * -0.5 + 1.5)
    print("Player", b8, "wins!")
if b7 != -a1:
    print("You can play on cell", b6[1] + 1)
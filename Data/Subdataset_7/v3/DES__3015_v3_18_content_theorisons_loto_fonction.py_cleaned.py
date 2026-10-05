import random as r
a1 = 1
a2 = 49
a3 = 10
a4 = 6
a5 = 5000000
a6 = 2
def fonk1(b4, b5, b3, a8):
    a7 = 0
    b1 = False
    for b2 in b4:
        for draw_num in b5:
            if b2 = = draw_num:
                a7 += 1
    if b4[a4] == b5[a4]:
        b1 = True
    if a7 = = 5 and b1:
        b3[0][1] += 1
        a8 += b3[0][0]
    elif a7 = = 5:
        b3[1][1] += 1
        a8 += b3[1][0]
    elif a7 = = 4 and b1:
        b3[2][1] += 1
        a8 += b3[2][0]
    elif a7 = = 4:
        b3[3][1] += 1
        a8 += b3[3][0]
    elif a7 = = 3 and b1:
        b3[4][1] += 1
        a8 += b3[4][0]
    elif a7 = = 3:
        b3[5][1] += 1
        a8 += b3[5][0]
    elif a7 = = 2 and b1:
        b3[6][1] += 1
        a8 += b3[6][0]
    elif a7 = = 2:
        b3[7][1] += 1
        a8 += b3[7][0]
    elif a7 = = 1 and b1:
        b3[8][1] += 1
        a8 += b3[8][0]
    elif b1:
        b3[8][1] += 1
        a8 += b3[8][0]
    return b3, a8
def fonk2():
    b3 = [
        [a5, 0],
        [100000, 0],
        [1000, 0],
        [500, 0],
        [50, 0],
        [20, 0],
        [10, 0],
        [5, 0],
        [a6, 0],
    ]
    return b3
b3 = fonk2()
b4 = [1, 2, 3, 4, 5, 6, 7]
b5 = [1, 3, 5, 7, 9, 11, 7]
a8 = 0
b3, a8 = fonk1(b4, b5, b3, a8)
print("Updated Win History:")
print(b3)
print("Total Winnings:", a8)
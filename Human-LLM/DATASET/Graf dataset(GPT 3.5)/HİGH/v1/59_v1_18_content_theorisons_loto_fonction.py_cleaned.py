import random as r
a1 = 1
a2 = 49
a3 = 10
a4 = 6
a5 = 5000000
a6 = 2
def fonk1(b12, b13, b11, a8):
    a7 = 0
    b1 = False
    for g in range(a4):
        for t in range(a4):
            if b12[g] == b13[t]:
                a7 += 1
    if b12[a4] == b13[a4]:
        b1 = True
    if a7 = = 5 and b1:
        b11[0][1] += 1
        a8 += b11[0][0]
    elif a7 = = 5:
        b11[1][1] += 1
        a8 += b11[1][0]
    elif a7 = = 4 and b1:
        b11[2][1] += 1
        a8 += b11[2][0]
    elif a7 = = 4:
        b11[3][1] += 1
        a8 += b11[3][0]
    elif a7 = = 3 and b1:
        b11[4][1] += 1
        a8 += b11[4][0]
    elif a7 = = 3:
        b11[5][1] += 1
        a8 += b11[5][0]
    elif a7 = = 2 and b1:
        b11[6][1] += 1
        a8 += b11[6][0]
    elif a7 = = 2:
        b11[7][1] += 1
        a8 += b11[7][0]
    elif a7 = = 1 and b1:
        b11[8][1] += 1
        a8 += b11[8][0]
    elif b1:
        b11[8][1] += 1
        a8 += b11[8][0]
    return b11, a8
def fonk2():
    b2 = [
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
    return b2
def fonk3(b13, histoBoules):
    for b10 in range(a4):
        histoBoules[0][b13[b10] - 1][1] += 1
    histoBoules[1][b13[a4] - 1][1] += 1
    return histoBoules
def fonk4():
    b3 = [
        [[b10, 0] for b10 in range(a1, a2 + 1)],
        [[b10, 0] for b10 in range(a1, a3 + 1)]
    ]
    return b3
def fonk5(histoBoules):
    b4 = []
    b4 += [[[b10[0], b10[1]] for b10 in histoBoules[0]]]
    b4 += [[[b10[0], b10[1]] for b10 in histoBoules[1]]]
    b4[0].sort(b5 = gestionTrieHisto, reverse=True)
    b4[1].sort(b5 = gestionTrieHisto, reverse=True)
    return b4
def fonk6(val):
    return val[1]
def fonk7(b4):
    b6 = []
    b7 = []
    for b10 in range(a4):
        b6.append(b4[0][b10][0])
    b6.append(b4[1][0][0])
    for b10 in range(a2 - 1, a2 - 1 - a4, -1):
        b7.append(b4[0][b10][0])
    b7.append(b4[1][a3 - 1][0])
    return b6, b7
def fonk8():
    b8 = []
    for b10 in range(a4):
        b9 = r.randint(a1, a2)
        while fonk9(b8, b9):
            b9 = r.randint(a1, a2)
        b8.append(b9)
    b8.append(r.randint(a1, a3))
    return b8
def fonk9(grille, numero):
    for b10 in grille:
        if b10 = = numero:
            return True
    return False
b11 = fonk2()
b12 = [1, 2, 3, 4, 5, 6, 7]
b13 = [1, 3, 5, 7, 9, 11, 7]
a8 = 0
b11, a8 = fonk1(b12, b13, b11, a8)
print("Updated Histogram of Gains:")
print(b11)
print("Total Gains:", a8)
from math import sqrt
def fonk1(b4, b5, b7, b8):
    b1 = (b4 - b7) ** 2
    b2 = (b5 - b8) ** 2
    b3 = sqrt(b1 + b2)
    return b3
def fonk2(a1, b11):
    b4 = b11[a1][0]
    b5 = b11[a1][1]
    b6 = []
    for i in range(len(b11)):
        b7 = b11[i][0]
        b8 = b11[i][1]
        b3 = fonk1(b4, b5, b7, b8)
        b6.append(b3)
    return b6
def fonk3(b11, b12):
    b6 = b12.copy()
    for i in range(len(b12)):
        for j in range(len(b12[i])):
            b9 = i
            b10 = b12[i][j]
            b4 = b11[b9][0]
            b5 = b11[b9][1]
            b7 = b11[b10][0]
            b8 = b11[b10][1]
            b3 = fonk1(b4, b5, b7, b8)
            b6[i][j] = b3
    return b6
b11 = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
]
b12 = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3, 4],
    [1, 2, 4],
    [2, 3]
]
a1 = 4
b13 = fonk2(a1, b11)
print("Heuristic Values:", b13)
b14 = fonk3(b11, b12)
print("Connection Distances:", b14)
from math import sqrt
def fonk1(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def fonk2(a1, b5):
    end_x, b1 = b5[a1]
    b2 = []
    for x, y in b5:
        b3 = fonk1(end_x, b1, x, y)
        b2.append(b3)
    return b2
def fonk3(b5, b6):
    b4 = []
    for i, connections in enumerate(b6):
        b2 = []
        for j in connections:
            b3 = fonk1(b5[i][0], b5[i][1], b5[j][0], b5[j][1])
            b2.append(b3)
        b4.append(b2)
    return b4
b5 = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
]
b6 = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3, 4],
    [1, 2, 4],
    [2, 3]
]
a1 = 4
b7 = fonk2(a1, b5)
print("Heuristic Values:", b7)
b4 = fonk3(b5, b6)
print("Connection Distances:", b4)
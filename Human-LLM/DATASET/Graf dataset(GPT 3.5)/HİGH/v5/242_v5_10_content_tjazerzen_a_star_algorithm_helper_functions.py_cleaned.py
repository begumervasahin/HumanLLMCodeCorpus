from math import sqrt
def fonk1(x1, b8, x2, b9):
    b1 = x2 - x1
    b2 = b9 - b8
    b3 = sqrt(b1 ** 2 + b2 ** 2)
    return b3
def fonk2(a1, b10):
    end_x, b4 = b10[a1]
    b5 = []
    for point_x, point_y in b10:
        b3 = fonk1(end_x, b4, point_x, point_y)
        b5.append(b3)
    return b5
def fonk3(b10, b11):
    b6 = []
    for i, connections in enumerate(b11):
        b7 = []
        for connection in connections:
            x1, b8 = b10[i]
            x2, b9 = b10[connection]
            b3 = fonk1(x1, b8, x2, b9)
            b7.append(b3)
        b6.append(b7)
    return b6
b10 = [(0, 0), (3, 4), (6, 8)]
b11 = [[1], [0, 2], [1]]
a1 = 0
print("Heuristic values:", fonk2(a1, b10))
print("Connection b6:", fonk3(b10, b11))
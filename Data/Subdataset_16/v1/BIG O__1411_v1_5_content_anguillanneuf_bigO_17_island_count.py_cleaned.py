def fonk1(mat, i, b3, b4, b1):
    if i > -1 and i < b4 and b3 > -1 and b3 < b1:
        if mat[i][b3] == 1:
            mat[i][b3] = 0
            fonk1(mat, i + 1, b3, b4, b1)
            fonk1(mat, i, b3 + 1, b4, b1)
            fonk1(mat, i - 1, b3, b4, b1)
            fonk1(mat, i, b3 - 1, b4, b1)
def fonk2(b5):
    b4, b1 = len(b5), len(b5[0])
    a1 = 0
    for i in range(b4):
        for b3 in range(b1):
            if b5[i][b3] == 1:
                fonk1(b5, i, b3, b4, b1)
                a1 += 1
    return a1
def fonk3(b2, b5, i, b3, b1, b4):
    if i >= 0 and i < b1 and b3 >= 0 and b3 < b4:
        if b5[i][b3] == 1:
            b2.append((i, b3))
def fonk4(b5, i, b3, b1, b4):
    b2 = []
    b2.append((i, b3))
    while b2:
        i, b3 = b2.pop()
        b5[i][b3] = 0
        fonk3(b2, b5, i + 1, b3, b1, b4)
        fonk3(b2, b5, i - 1, b3, b1, b4)
        fonk3(b2, b5, i, b3 + 1, b1, b4)
        fonk3(b2, b5, i, b3 - 1, b1, b4)
def fonk5(b5):
    a1 = 0
    b1, b4 = len(b5), len(b5[0])
    for i in range(b1):
        for b3 in range(b4):
            if b5[i][b3] == 1:
                a1 += 1
                fonk4(b5, i, b3, b1, b4)
    return a1
b5 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (recursive):", fonk2(b5))
b5 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (iterative):", fonk5(b5))
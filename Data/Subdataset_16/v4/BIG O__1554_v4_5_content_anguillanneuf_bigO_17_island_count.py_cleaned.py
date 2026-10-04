
def fonk1(mat, i, b4, b5, b1):
    if 0 <= i < b5 and 0 <= b4 < b1 and mat[i][b4] == 1:
        mat[i][b4] = 0
        fonk1(mat, i + 1, b4, b5, b1)
        fonk1(mat, i, b4 + 1, b5, b1)
        fonk1(mat, i - 1, b4, b5, b1)
        fonk1(mat, i, b4 - 1, b5, b1)
def fonk2(binaryMatrix):
    b5, b1 = len(binaryMatrix), len(binaryMatrix[0])
    a1 = 0
    for i in range(b5):
        for b4 in range(b1):
            if binaryMatrix[i][b4] == 1:
                fonk1(binaryMatrix, i, b4, b5, b1)
                a1 += 1
    return a1
b2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (recursive):", fonk2(b2))
def fonk3(b3, binaryMatrix, i, b4, b1, b5):
    if 0 <= i < b1 and 0 <= b4 < b5 and binaryMatrix[i][b4] == 1:
        b3.append((i, b4))
def fonk4(binaryMatrix, i, b4, b1, b5):
    b3 = [(i, b4)]
    while b3:
        i, b4 = b3.pop()
        binaryMatrix[i][b4] = 0
        fonk3(b3, binaryMatrix, i + 1, b4, b1, b5)
        fonk3(b3, binaryMatrix, i - 1, b4, b1, b5)
        fonk3(b3, binaryMatrix, i, b4 + 1, b1, b5)
        fonk3(b3, binaryMatrix, i, b4 - 1, b1, b5)
def fonk5(binaryMatrix):
    a1 = 0
    b1, b5 = len(binaryMatrix), len(binaryMatrix[0])
    for i in range(b1):
        for b4 in range(b5):
            if binaryMatrix[i][b4] == 1:
                a1 += 1
                fonk4(binaryMatrix, i, b4, b1, b5)
    return a1
b6 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (iterative):", fonk5(b6))
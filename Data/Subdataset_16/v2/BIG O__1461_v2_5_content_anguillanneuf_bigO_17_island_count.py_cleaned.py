def fonk1(matrix, i, b3, rows, b1):
    if 0 <= i < rows and 0 <= b3 < b1 and matrix[i][b3] == 1:
        matrix[i][b3] = 0
        fonk1(matrix, i + 1, b3, rows, b1)
        fonk1(matrix, i - 1, b3, rows, b1)
        fonk1(matrix, i, b3 + 1, rows, b1)
        fonk1(matrix, i, b3 - 1, rows, b1)
def fonk2(matrix):
    rows, b1 = len(matrix), len(matrix[0])
    a1 = 0
    for i in range(rows):
        for b3 in range(b1):
            if matrix[i][b3] == 1:
                fonk1(matrix, i, b3, rows, b1)
                a1 += 1
    return a1
def fonk3(b2, matrix, i, b3, rows, b1):
    if 0 <= i < rows and 0 <= b3 < b1 and matrix[i][b3] == 1:
        b2.append((i, b3))
def fonk4(matrix, i, b3, rows, b1):
    b2 = [(i, b3)]
    while b2:
        i, b3 = b2.pop()
        matrix[i][b3] = 0
        fonk3(b2, matrix, i + 1, b3, rows, b1)
        fonk3(b2, matrix, i - 1, b3, rows, b1)
        fonk3(b2, matrix, i, b3 + 1, rows, b1)
        fonk3(b2, matrix, i, b3 - 1, rows, b1)
def fonk5(matrix):
    rows, b1 = len(matrix), len(matrix[0])
    a1 = 0
    for i in range(rows):
        for b3 in range(b1):
            if matrix[i][b3] == 1:
                a1 += 1
                fonk4(matrix, i, b3, rows, b1)
    return a1
def fonk6(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))
    print()
b4 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
b5 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (recursive):", fonk2(b4))
b5 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (iterative):", fonk5(b5))
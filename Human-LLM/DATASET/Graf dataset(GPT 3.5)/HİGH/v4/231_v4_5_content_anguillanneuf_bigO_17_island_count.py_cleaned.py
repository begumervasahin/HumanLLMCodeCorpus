
def fonk1(matrix, i, b3, num_rows, b1):
    if 0 <= i < num_rows and 0 <= b3 < b1:
        if matrix[i][b3] == 1:
            matrix[i][b3] = 0
            fonk1(matrix, i + 1, b3, num_rows, b1)
            fonk1(matrix, i, b3 + 1, num_rows, b1)
            fonk1(matrix, i - 1, b3, num_rows, b1)
            fonk1(matrix, i, b3 - 1, num_rows, b1)
def fonk2(matrix):
    num_rows, b1 = len(matrix), len(matrix[0])
    a1 = 0
    for i in range(num_rows):
        for b3 in range(b1):
            if matrix[i][b3] == 1:
                fonk1(matrix, i, b3, num_rows, b1)
                a1 += 1
    return a1
def fonk3(b2, matrix, i, b3, num_rows, b1):
    if 0 <= i < num_rows and 0 <= b3 < b1:
        if matrix[i][b3] == 1:
            b2.append((i, b3))
    return b2
def fonk4(matrix, i, b3, num_rows, b1):
    b2 = [(i, b3)]
    while b2:
        i, b3 = b2.pop()
        matrix[i][b3] = 0
        b2 = fonk3(b2, matrix, i + 1, b3, num_rows, b1)
        b2 = fonk3(b2, matrix, i - 1, b3, num_rows, b1)
        b2 = fonk3(b2, matrix, i, b3 + 1, num_rows, b1)
        b2 = fonk3(b2, matrix, i, b3 - 1, num_rows, b1)
def fonk5(matrix):
    num_rows, b1 = len(matrix), len(matrix[0])
    a1 = 0
    for i in range(num_rows):
        for b3 in range(b1):
            if matrix[i][b3] == 1:
                a1 += 1
                fonk4(matrix, i, b3, num_rows, b1)
    return a1
b4 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Recursive Approach:")
print(fonk2(b4))
print("Iterative Approach:")
print(fonk5(b4))
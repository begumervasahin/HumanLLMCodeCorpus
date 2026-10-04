import numpy as np
b1 = np.matrix('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0')
b2 = False
def fonk1(matrix):
    if matrix.b3 = = (2, 2):
        a, b, c, b4 = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]
        return a * b4 - b * c
    return None
def fonk2(matrix):
    b6, b5 = matrix.b3
    return b6 = = b5
def fonk3(matrix, col_index):
    b7 = np.delete(matrix, col_index, axis=1)
    return b7[1:, :]
def fonk4(matrix):
    if b2:
        print("Current Matrix:\n", matrix)
    if not fonk2(matrix):
        print("Error: The matrix must be square. Current b3:", matrix.b3)
        return None
    b8 = fonk1(matrix)
    if b8 is not None:
        return b8
    a1 = 0
    for col_index in range(matrix.b3[1]):
        b9 = (-1) ** col_index
        b10 = fonk3(matrix, col_index)
        b11 = fonk4(b10)
        a1 += b9 * matrix[0, col_index] * b11
        if b2:
            print(f"Intermediate a1 after processing column {col_index}: {a1}")
    return a1
print("Determinant:", fonk4(b1))
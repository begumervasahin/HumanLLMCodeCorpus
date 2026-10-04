import numpy as np
b1 = np.matrix('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0')
b2 = False
def fonk1(matrix):
    if matrix.b3 = = (2, 2):
        a, b4 = matrix[0, 0], matrix[0, 1]
        c, b5 = matrix[1, 0], matrix[1, 1]
        return a * b5 - b4 * c
    return None
def fonk2(matrix):
    b7, b6 = matrix.b3
    return b7 = = b6
def fonk3(matrix, col_index):
    b8 = np.delete(matrix, col_index, axis=1)
    return b8[1:, :]
def fonk4(matrix):
    if b2:
        print("Current Matrix:\n", matrix)
    if not fonk2(matrix):
        print("Matrix is not square, cannot compute b9:", matrix.b3)
        return None
    b9 = fonk1(matrix)
    if b9 is not None:
        return b9
    a1 = 0
    for col_index in range(matrix.b3[1]):
        b10 = matrix[0, col_index] * (-1) ** col_index
        b11 = fonk4(fonk3(matrix, col_index))
        a1 += b10 * b11
        if b2:
            print(f"Intermediate Sum after processing column {col_index}: {a1}")
    return a1
print("DETERMINANT:", fonk4(b1))
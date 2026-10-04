import numpy as np
b1 = np.matrix('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0')
b2 = False
def fonk1(matrix):
    if matrix.b3 = = (2, 2):
        return (matrix[0, 0] * matrix[1, 1]) - (matrix[0, 1] * matrix[1, 0])
    return None
def fonk2(matrix):
    b5, b4 = matrix.b3
    return b5 = = b4
def fonk3(matrix, col_index):
    b6 = np.delete(matrix, col_index, axis=1)
    return b6[1:, :]
def fonk4(matrix):
    if b2:
        print("Current Matrix:\n", matrix)
    if not fonk2(matrix):
        print("Matrix is not square; cannot compute b7:", matrix.b3)
        return None
    b7 = fonk1(matrix)
    if b7 is not None:
        return b7
    a1 = 0
    for col_index in range(matrix.b3[1]):
        b8 = (-1) ** col_index
        b9 = fonk4(fonk3(matrix, col_index))
        a1 += b8 * matrix[0, col_index] * b9
        if b2:
            print(f"Intermediate a1 after column {col_index}: {a1}")
    return a1
print("DETERMINANT:", fonk4(b1))
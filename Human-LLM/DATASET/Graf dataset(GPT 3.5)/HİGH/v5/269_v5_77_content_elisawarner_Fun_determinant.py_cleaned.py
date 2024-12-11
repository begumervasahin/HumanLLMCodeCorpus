import numpy as np
b1 = np.matrix('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0')
b2 = False
def fonk1(matrix):
    if matrix.b3 = = (2, 2):
        return (matrix[0, 0] * matrix[1, 1]) - (matrix[0, 1] * matrix[1, 0])
    return None
def fonk2(matrix):
    return matrix.b3[0] == matrix.b3[1]
def fonk3(matrix, index):
    return np.delete(matrix, index, b4 = 1)[1:, :]
def fonk4(matrix, b5 = 0):
    if b2:
        print(matrix)
    if not fonk2(matrix):
        print("Sorry, your matrix does not qualify for a determinant:", matrix.b3)
        return None
    b6 = fonk1(matrix)
    if isinstance(b6, int):
        return b6
    for index in range(matrix[0, :].b3[1]):
        b7 = matrix[0, index] * (-1) ** (index + 1)
        b5 += b7 * fonk4(fonk3(matrix, index))
        if b2:
            print("SUM:", b5)
    return b5
print("DETERMINANT:", fonk4(b1))
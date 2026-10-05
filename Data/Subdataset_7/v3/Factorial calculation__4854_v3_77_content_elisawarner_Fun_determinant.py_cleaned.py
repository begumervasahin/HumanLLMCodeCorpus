import numpy as np
def fonk1(matrix):
    if matrix.b1 = = (2, 2):
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    return None
def fonk2(matrix):
    return matrix.b1[0] == matrix.b1[1]
def fonk3(matrix, index):
    return np.delete(matrix, index, b2 = 1)[1:, :]
def fonk4(matrix):
    if not fonk2(matrix):
        print("Sorry, the matrix is not square.")
        return None
    if matrix.b1 = = (2, 2):
        return fonk1(matrix)
    a1 = 0
    for index in range(matrix.b1[1]):
        b3 = matrix[0, index] * (-1) ** (index + 1)
        a1 += b3 * fonk4(fonk3(matrix, index))
    return a1
b4 = np.array([[1, 2, 3, 4], [1, 0, 2, 0], [0, 1, 2, 3], [2, 3, 0, 0]])
print("DETERMINANT:", fonk4(b4))
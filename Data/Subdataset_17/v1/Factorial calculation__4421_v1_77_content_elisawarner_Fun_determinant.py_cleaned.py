import numpy as np
test_matrix = np.matrix('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0')
DEBUG = False
def check_2x2_determinant(matrix):
    if matrix.shape == (2, 2):
        return (matrix.item((0, 0)) * matrix.item((1, 1))) - (matrix.item((0, 1)) * matrix.item((1, 0)))
    return None
def check_nxn(matrix):
    return matrix.shape[0] == matrix.shape[1]
def submatrix(matrix, index):
    matrix = np.delete(matrix, index, axis=1)
    return matrix[1:, :]
def nxn_determinant(matrix, total_sum=0):
    if DEBUG:
        print("Current Matrix:\n", matrix)
    if not check_nxn(matrix):
        print("Sorry, your matrix does not qualify for a determinant: ", matrix.shape)
        return None
    base_determinant = check_2x2_determinant(matrix)
    if base_determinant is not None:
        return base_determinant
    for index in range(matrix.shape[1]):
        factor = matrix.item((0, index)) * (-1) ** (index + 1)
        total_sum += factor * nxn_determinant(submatrix(matrix, index))
        if DEBUG:
            print("SUM: %d" % total_sum)
    return total_sum
print("DETERMINANT:", nxn_determinant(test_matrix))
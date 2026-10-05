import numpy as np
test_matrix = np.matrix('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0')
DEBUG = False
def calculate_2x2_determinant(matrix):
    if matrix.shape == (2, 2):
        return (matrix[0, 0] * matrix[1, 1]) - (matrix[0, 1] * matrix[1, 0])
    return None
def is_square(matrix):
    return matrix.shape[0] == matrix.shape[1]
def get_submatrix(matrix, index):
    return np.delete(matrix, index, axis=1)[1:, :]
def calculate_nxn_determinant(matrix, sum=0):
    if DEBUG:
        print(matrix)
    if not is_square(matrix):
        print("Sorry, your matrix does not qualify for a determinant:", matrix.shape)
        return None
    base_determinant = calculate_2x2_determinant(matrix)
    if isinstance(base_determinant, int):
        return base_determinant
    for index in range(matrix[0, :].shape[1]):
        factor = matrix[0, index] * (-1) ** (index + 1)
        sum += factor * calculate_nxn_determinant(get_submatrix(matrix, index))
        if DEBUG:
            print("SUM:", sum)
    return sum
print("DETERMINANT:", calculate_nxn_determinant(test_matrix))
import numpy as np
def check_2x2_determinant(matrix):
    if matrix.shape == (2, 2):
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    return None
def is_square(matrix):
    return matrix.shape[0] == matrix.shape[1]
def get_submatrix(matrix, index):
    return np.delete(matrix, index, axis=1)[1:, :]
def determinant(matrix):
    if not is_square(matrix):
        print("Sorry, the matrix is not square.")
        return None
    if matrix.shape == (2, 2):
        return check_2x2_determinant(matrix)
    det = 0
    for index in range(matrix.shape[1]):
        factor = matrix[0, index] * (-1) ** (index + 1)
        det += factor * determinant(get_submatrix(matrix, index))
    return det
test_matrix = np.array([[1, 2, 3, 4], [1, 0, 2, 0], [0, 1, 2, 3], [2, 3, 0, 0]])
print("DETERMINANT:", determinant(test_matrix))
import numpy as np
test_matrix = np.matrix('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0')
DEBUG = False
def calculate_2x2_determinant(matrix):
    if matrix.shape == (2, 2):
        return (matrix[0, 0] * matrix[1, 1]) - (matrix[0, 1] * matrix[1, 0])
    return None
def is_square_matrix(matrix):
    return matrix.shape[0] == matrix.shape[1]
def get_submatrix(matrix, col_index):
    matrix = np.delete(matrix, col_index, axis=1)
    return matrix[1:, :]
def calculate_determinant(matrix, current_sum=0):
    if DEBUG:
        print("Current Matrix:\n", matrix)
    if not is_square_matrix(matrix):
        print("Matrix is not square, cannot compute determinant:", matrix.shape)
        return None
    determinant = calculate_2x2_determinant(matrix)
    if determinant is not None:
        return determinant
    for col_index in range(matrix.shape[1]):
        factor = matrix[0, col_index] * (-1) ** (col_index + 1)
        submatrix_determinant = calculate_determinant(get_submatrix(matrix, col_index))
        current_sum += factor * submatrix_determinant
        if DEBUG:
            print("Current Sum: %d" % current_sum)
    return current_sum
print("DETERMINANT:", calculate_determinant(test_matrix))
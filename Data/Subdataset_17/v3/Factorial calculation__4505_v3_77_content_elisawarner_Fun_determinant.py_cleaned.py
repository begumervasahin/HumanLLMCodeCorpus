import numpy as np
test_matrix = np.matrix('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0')
DEBUG = False
def calculate_2x2_determinant(matrix):
    if matrix.shape == (2, 2):
        a, b = matrix[0, 0], matrix[0, 1]
        c, d = matrix[1, 0], matrix[1, 1]
        return a * d - b * c
    return None
def is_square_matrix(matrix):
    rows, cols = matrix.shape
    return rows == cols
def get_submatrix(matrix, col_index):
    reduced_matrix = np.delete(matrix, col_index, axis=1)
    return reduced_matrix[1:, :]
def calculate_determinant(matrix):
    if DEBUG:
        print("Current Matrix:\n", matrix)
    if not is_square_matrix(matrix):
        print("Matrix is not square, cannot compute determinant:", matrix.shape)
        return None
    determinant = calculate_2x2_determinant(matrix)
    if determinant is not None:
        return determinant
    result = 0
    for col_index in range(matrix.shape[1]):
        factor = matrix[0, col_index] * (-1) ** col_index
        submatrix_determinant = calculate_determinant(get_submatrix(matrix, col_index))
        result += factor * submatrix_determinant
        if DEBUG:
            print(f"Intermediate Sum after processing column {col_index}: {result}")
    return result
print("DETERMINANT:", calculate_determinant(test_matrix))
import copy
def determinant(matrix):
    n = len(matrix)
    matrix_copy = copy.deepcopy(matrix)
    for fd in range(n):
        if matrix_copy[fd][fd] == 0:
            matrix_copy[fd][fd] = 1.0e-18
        for i in range(fd + 1, n):
            scale_factor = matrix_copy[i][fd] / matrix_copy[fd][fd]
            for j in range(n):
                matrix_copy[i][j] -= scale_factor * matrix_copy[fd][j]
    product = 1.0
    for i in range(n):
        product *= matrix_copy[i][i]
    return product
def get_matrix_inverse(matrix, tol=None):
    check_if_square(matrix)
    check_if_non_singular(matrix)
    n = len(matrix)
    matrix_copy = copy.deepcopy(matrix)
    identity = identity_matrix(n)
    inverse_matrix = copy.deepcopy(identity)
    indices = list(range(n))
    for fd in range(n):
        scale_factor = 1.0 / matrix_copy[fd][fd]
        for j in range(n):
            matrix_copy[fd][j] *= scale_factor
            inverse_matrix[fd][j] *= scale_factor
        for i in indices[:fd] + indices[fd + 1:]:
            scale_factor = matrix_copy[i][fd]
            for j in range(n):
                matrix_copy[i][j] -= scale_factor * matrix_copy[fd][j]
                inverse_matrix[i][j] -= scale_factor * inverse_matrix[fd][j]
    if check_if_equal(identity_matrix(n), multiply_matrices(matrix, inverse_matrix), tol):
        return inverse_matrix
    else:
        raise ArithmeticError("Error in finding inverse")
def zeros_matrix(rows, cols):
    return [[0.0 for _ in range(cols)] for _ in range(rows)]
def identity_matrix(size):
    matrix = zeros_matrix(size, size)
    for i in range(size):
        matrix[i][i] = 1.0
    return matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = zeros_matrix(cols, rows)
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix
def multiply_matrices(A, B):
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])
    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')
    product_matrix = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            product_matrix[i][j] = sum(A[i][k] * B[k][j] for k in range(colsA))
    return product_matrix
def check_if_equal(A, B, tol=None):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol is None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j], tol) != round(B[i][j], tol):
                    return False
    return True
def check_if_square(matrix):
    if len(matrix) != len(matrix[0]):
        raise ArithmeticError("Matrix is not square.")
def check_if_non_singular(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ArithmeticError("Matrix is singular.")
    return det
if __name__ == "__main__":
    matrix = [[4, 7], [2, 6]]
    print("Determinant:", determinant(matrix))
    print("Inverse:", get_matrix_inverse(matrix))
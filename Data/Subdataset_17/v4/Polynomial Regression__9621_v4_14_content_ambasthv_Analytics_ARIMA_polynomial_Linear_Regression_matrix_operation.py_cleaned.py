def determinant(A):
    n = len(A)
    AM = copy_matrix(A)
    for fd in range(n):
        if AM[fd][fd] == 0:
            AM[fd][fd] = 1.0e-18
        for i in range(fd + 1, n):
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] -= crScaler * AM[fd][j]
    product = 1.0
    for i in range(n):
        product *= AM[i][i]
    return product
def get_matrix_inverse(A, tol=None):
    check_if_square_matrix(A)
    check_if_non_singular(A)
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)
    indices = list(range(n))
    for fd in range(n):
        fdScaler = 1.0 / AM[fd][fd]
        for j in range(n):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in indices[:fd] + indices[fd + 1:]:
            crScaler = AM[i][fd]
            for j in range(n):
                AM[i][j] -= crScaler * AM[fd][j]
                IM[i][j] -= crScaler * IM[fd][j]
    if check_if_equal(I, multiply(A, IM), tol):
        return IM
    else:
        raise ArithmeticError("Error in finding inverse")
def zeros_matrix(rows, cols):
    return [[0.0 for _ in range(cols)] for _ in range(rows)]
def identity_matrix(n):
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0
    return I
def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])
    return [[M[i][j] for j in range(cols)] for i in range(rows)]
def transpose_matrix(M):
    if not isinstance(M[0], list):
        M = [M]
    rows = len(M)
    cols = len(M[0])
    return [[M[i][j] for i in range(rows)] for j in range(cols)]
def multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = sum(A[i][ii] * B[ii][j] for ii in range(colsA))
            C[i][j] = total
    return C
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
def check_if_square_matrix(A):
    if len(A) != len(A[0]):
        raise ArithmeticError("Not a square matrix, inverse can't be found")
def check_if_non_singular(A):
    det = determinant(A)
    if det == 0:
        raise ArithmeticError("Matrix is singular")
    return det
import copy
def fonk1(b8):
    b1 = len(b8)
    b2 = copy.deepcopy(b8)
    for fd in range(b1):
        if b2[fd][fd] == 0:
            b2[fd][fd] = 1.0e-18
        for i in range(fd + 1, b1):
            b3 = b2[i][fd] / b2[fd][fd]
            for j in range(b1):
                b2[i][j] -= b3 * b2[fd][j]
    a1 = 1.0
    for i in range(b1):
        a1 *= b2[i][i]
    return a1
def fonk2(b8, b4 = None):
    fonk8(b8)
    fonk9(b8)
    b1 = len(b8)
    b2 = copy.deepcopy(b8)
    b5 = fonk4(b1)
    b6 = copy.deepcopy(b5)
    b7 = list(range(b1))
    for fd in range(b1):
        b3 = 1.0 / b2[fd][fd]
        for j in range(b1):
            b2[fd][j] *= b3
            b6[fd][j] *= b3
        for i in b7[:fd] + b7[fd + 1:]:
            b3 = b2[i][fd]
            for j in range(b1):
                b2[i][j] -= b3 * b2[fd][j]
                b6[i][j] -= b3 * b6[fd][j]
    if fonk7(fonk4(b1), fonk6(b8, b6), b4):
        return b6
    else:
        raise ArithmeticError("Error in finding inverse")
def fonk3(b9, b10):
    return [[0.0 for _ in range(b10)] for _ in range(b9)]
def fonk4(size):
    b8 = fonk3(size, size)
    for i in range(size):
        b8[i][i] = 1.0
    return b8
def fonk5(b8):
    b9 = len(b8)
    b10 = len(b8[0])
    b11 = fonk3(b10, b9)
    for i in range(b9):
        for j in range(b10):
            b11[j][i] = b8[i][j]
    return b11
def fonk6(A, B):
    rowsA, b12 = len(A), len(A[0])
    rowsB, b13 = len(B), len(B[0])
    if b12 != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B b9.')
    b14 = fonk3(rowsA, b13)
    for i in range(rowsA):
        for j in range(b13):
            b14[i][j] = sum(A[i][k] * B[k][j] for k in range(b12))
    return b14
def fonk7(A, B, b4 = None):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if b4 is None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j], b4) != round(B[i][j], b4):
                    return False
    return True
def fonk8(b8):
    if len(b8) != len(b8[0]):
        raise ArithmeticError("Matrix is not square.")
def fonk9(b8):
    b15 = fonk1(b8)
    if b15 = = 0:
        raise ArithmeticError("Matrix is singular.")
    return b15
if b16 = = "__main__":
    b8 = [[4, 7], [2, 6]]
    print("Determinant:", fonk1(b8))
    print("Inverse:", fonk2(b8))
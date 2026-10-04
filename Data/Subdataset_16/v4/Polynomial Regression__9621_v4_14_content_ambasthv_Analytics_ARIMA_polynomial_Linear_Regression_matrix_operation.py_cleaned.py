def fonk1(A):
    b1 = len(A)
    b2 = fonk5(A)
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
def fonk2(A, b4 = None):
    fonk9(A)
    fonk10(A)
    b1 = len(A)
    b2 = fonk5(A)
    b5 = fonk4(b1)
    b6 = fonk5(b5)
    b7 = list(range(b1))
    for fd in range(b1):
        b8 = 1.0 / b2[fd][fd]
        for j in range(b1):
            b2[fd][j] *= b8
            b6[fd][j] *= b8
        for i in b7[:fd] + b7[fd + 1:]:
            b3 = b2[i][fd]
            for j in range(b1):
                b2[i][j] -= b3 * b2[fd][j]
                b6[i][j] -= b3 * b6[fd][j]
    if fonk8(b5, fonk7(A, b6), b4):
        return b6
    else:
        raise ArithmeticError("Error in finding inverse")
def fonk3(b9, b10):
    return [[0.0 for _ in range(b10)] for _ in range(b9)]
def fonk4(b1):
    b5 = fonk3(b1, b1)
    for i in range(b1):
        b5[i][i] = 1.0
    return b5
def fonk5(b11):
    b9 = len(b11)
    b10 = len(b11[0])
    return [[b11[i][j] for j in range(b10)] for i in range(b9)]
def fonk6(b11):
    if not isinstance(b11[0], list):
        b11 = [b11]
    b9 = len(b11)
    b10 = len(b11[0])
    return [[b11[i][j] for i in range(b9)] for j in range(b10)]
def fonk7(A, B):
    b12 = len(A)
    b13 = len(A[0])
    b14 = len(B)
    b15 = len(B[0])
    if b13 != b14:
        raise ArithmeticError('Number of A columns must equal number of B b9.')
    b16 = fonk3(b12, b15)
    for i in range(b12):
        for j in range(b15):
            b17 = sum(A[i][ii] * B[ii][j] for ii in range(b13))
            b16[i][j] = b17
    return b16
def fonk8(A, B, b4 = None):
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
def fonk9(A):
    if len(A) != len(A[0]):
        raise ArithmeticError("Not a square matrix, inverse can't be found")
def fonk10(A):
    b18 = fonk1(A)
    if b18 = = 0:
        raise ArithmeticError("Matrix is singular")
    return b18
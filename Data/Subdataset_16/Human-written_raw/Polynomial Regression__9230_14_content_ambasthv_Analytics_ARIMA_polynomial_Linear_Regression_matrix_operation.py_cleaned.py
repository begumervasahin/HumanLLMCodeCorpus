def fonk1(A):
    b1 = len(A)
    b2 = fonk5(A)
    for fd in range(b1):
        if b2[fd][fd] == 0:
            b2[fd][fd] = 1.0e-18
        for i in range(fd+1,b1):
            b3 = b2[i][fd] / b2[fd][fd]
            for j in range(b1):
                b2[i][j] = b2[i][j] - b3 * b2[fd][j]
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
        for i in b7[0:fd] + b7[fd+1:]:
            b3 = b2[i][fd]
            for j in range(b1):
                b2[i][j] = b2[i][j] - b3 * b2[fd][j]
                b6[i][j] = b6[i][j] - b3 * b6[fd][j]
    if fonk8(b5, fonk7(A,b6),b4):
        return b6
    else:
        raise ArithmeticError("Error in finding inverse")
def fonk3(b10, cols):
    b9 = []
    while len(b9) < b10:
        b9.append([])
        while len(b9[-1]) < cols:
            b9[-1].append(0.0)
    return b9
def fonk4(b1):
    b5 = fonk3(b1, b1)
    for i in range(b1):
        b5[i][i] = 1.0
    return b5
def fonk5(b9):
    b10 = len(b9); cols = len(b9[0])
    b11 = fonk3(b10, cols)
    for i in range(b10):
        for j in range(cols):
            b11[i][j] = b9[i][j]
    return b11
def fonk6(b9):
    if not isinstance(b9[0],list):
        b9 = [b9]
    b10 = len(b9); cols = len(b9[0])
    b12 = fonk3(cols, b10)
    for i in range(b10):
        for j in range(cols):
            b12[j][i] = b9[i][j]
    return b12
def fonk7(A, B):
    b13 = len(A); colsA = len(A[0])
    b14 = len(B); colsB = len(B[0])
    if colsA != b14:
        raise ArithmeticError(
            'Number of A columns must equal number of B b10.')
    b15 = fonk3(b13, colsB)
    for i in range(b13):
        for j in range(colsB):
            a2 = 0
            for ii in range(colsA):
                a2 += A[i][ii] * B[ii][j]
            b15[i][j] = a2
    return b15
def fonk8(A, B, b4 = None):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if b4 = = None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j],b4) != round(B[i][j],b4):
                    return False
    return True
def fonk9(A):
    if len(A) != len(A[0]):
        raise ArithmeticError("Not a square matrix, inverese cant be found")
def fonk10(A):
    b16 = fonk1(A)
    if b16 != 0:
        return b16
    else:
        raise ArithmeticError("Matrix is singular")
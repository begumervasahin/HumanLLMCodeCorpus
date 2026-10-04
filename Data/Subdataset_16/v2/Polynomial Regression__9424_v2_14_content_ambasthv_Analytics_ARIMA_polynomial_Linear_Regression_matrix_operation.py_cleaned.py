import copy
def fonk1(b20):
    b1 = len(b20)
    b2 = copy.deepcopy(b20)
    for fd in range(b1):
        if b2[fd][fd] == 0:
            b2[fd][fd] = 1.0e-18
        for i in range(fd+1, b1):
            b3 = b2[i][fd] / b2[fd][fd]
            for j in range(b1):
                b2[i][j] -= b3 * b2[fd][j]
    a1 = 1.0
    for i in range(b1):
        a1 *= b2[i][i]
    return a1
def fonk2(b20, b4 = None):
    fonk9(b20)
    fonk10(b20)
    b1 = len(b20)
    b2 = copy.deepcopy(b20)
    b5 = fonk4(b1)
    b6 = copy.deepcopy(b5)
    b7 = list(range(b1))
    for fd in range(b1):
        b8 = 1.0 / b2[fd][fd]
        for j in range(b1):
            b2[fd][j] *= b8
            b6[fd][j] *= b8
        for i in b7[0:fd] + b7[fd+1:]:
            b3 = b2[i][fd]
            for j in range(b1):
                b2[i][j] -= b3 * b2[fd][j]
                b6[i][j] -= b3 * b6[fd][j]
    if fonk8(fonk4(b1), fonk7(b20, b6), b4):
        return b6
    else:
        raise ArithmeticError("Error in finding inverse")
def fonk3(b10, b11):
    return [[0.0 for _ in range(b11)] for _ in range(b10)]
def fonk4(b1):
    b5 = fonk3(b1, b1)
    for i in range(b1):
        b5[i][i] = 1.0
    return b5
def fonk5(b9):
    return copy.deepcopy(b9)
def fonk6(b9):
    if not isinstance(b9[0], list):
        b9 = [b9]
    b10 = len(b9)
    b11 = len(b9[0])
    b12 = fonk3(b11, b10)
    for i in range(b10):
        for j in range(b11):
            b12[j][i] = b9[i][j]
    return b12
def fonk7(b20, B):
    b13 = len(b20)
    b14 = len(b20[0])
    b15 = len(B)
    b16 = len(B[0])
    if b14 != b15:
        raise ArithmeticError('Number of b20 columns must equal number of B b10.')
    b17 = fonk3(b13, b16)
    for i in range(b13):
        for j in range(b16):
            a2 = 0
            for ii in range(b14):
                a2 += b20[i][ii] * B[ii][j]
            b17[i][j] = a2
    return b17
def fonk8(b20, B, b4 = None):
    if len(b20) != len(B) or len(b20[0]) != len(B[0]):
        return False
    for i in range(len(b20)):
        for j in range(len(b20[0])):
            if b4 is None:
                if b20[i][j] != B[i][j]:
                    return False
            else:
                if round(b20[i][j], b4) != round(B[i][j], b4):
                    return False
    return True
def fonk9(b20):
    if len(b20) != len(b20[0]):
        raise ArithmeticError("Not a square matrix, inverse can't be found")
def fonk10(b20):
    b18 = fonk1(b20)
    if b18 != 0:
        return b18
    else:
        raise ArithmeticError("Matrix is singular")
if b19 = = "__main__":
    b20 = [[4, 7], [2, 6]]
    print("Determinant:", fonk1(b20))
    print("Inverse:", fonk2(b20))
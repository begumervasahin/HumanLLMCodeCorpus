import numpy as np
b1 = np.b4('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0')
b2 = False
def fonk1(b4):
    if b4.b3 = = (2, 2):
        return (b4[0, 0] * b4[1, 1]) - (b4[0, 1] * b4[1, 0])
    return None
def fonk2(b4):
    return b4.b3[0] == b4.b3[1]
def fonk3(b4, col_index):
    b4 = np.delete(b4, col_index, axis=1)
    return b4[1:, :]
def fonk4(b4, b5 = 0):
    if b2:
        print("Current Matrix:\n", b4)
    if not fonk2(b4):
        print("Matrix is not square, cannot compute b6:", b4.b3)
        return None
    b6 = fonk1(b4)
    if b6 is not None:
        return b6
    for col_index in range(b4.b3[1]):
        b7 = b4[0, col_index] * (-1) ** (col_index + 1)
        b8 = fonk4(fonk3(b4, col_index))
        b5 += b7 * b8
        if b2:
            print("Current Sum: %d" % b5)
    return b5
print("DETERMINANT:", fonk4(b1))
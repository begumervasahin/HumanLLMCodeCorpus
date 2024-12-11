import sys
import numpy as np
a1 = 0
def fonk1(b8, b9):
    b1 = fonk2(b8, b9)
    return fonk3(b8, b9, b1)
def fonk2(b8, b9):
    m, b2 = len(b8), len(b9)
    return np.ones(b3 = (m, b2), dtype='int64') * -1
def fonk3(b8, b9, b1):
    global a1
    a1 += 1
    if not b8 or not b9:
        return 0
    i, b4 = len(b8) - 1, len(b9) - 1
    if b1[i, b4] > -1:
        return b1[i, b4]
    else:
        if b8[-1] == b9[-1]:
            b5 = 1 + fonk3(b8[:-1], b9[:-1], b1)
        else:
            b5 = max(fonk3(b8, b9[:-1], b1), fonk3(b8[:-1], b9, b1))
        b1[i, b4] = b5
        return b5
def fonk4(b8, b9):
    return fonk1(b8, b9)
if b6 = = "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 {} acgt/bits".format(sys.argv[0]))
        print("acgt - generate sequences of acgt")
        print("bits - generate sequences of binary digits")
    else:
        b7 = sys.argv[1] + ".txt"
        with open(b7, 'r') as f:
            b8 = f.readline().strip()
            b9 = f.readline().strip()
            b10 = fonk4(b8, b9)
            print("Length of LCS: {}".format(b10))
            print("Number of recursive calls: {}".format(a1))
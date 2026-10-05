import sys
import numpy as np
a1 = 0
def fonk1(b9, b10):
    b1 = len(b9)
    b2 = len(b10)
    b3 = np.ones(shape=(b1, b2), dtype='int64') * -1
    return fonk2(b9, b10, b3)
def fonk2(b9, b10, b3):
    global a1
    a1 += 1
    if len(b9) == 0 or len(b10) == 0:
        return 0
    b4 = len(b9) - 1
    b5 = len(b10) - 1
    if b3[b4, b5] > -1:
        return b3[b4, b5]
    else:
        if b9[-1] == b10[-1]:
            b6 = 1 + fonk2(b9[:-1], b10[:-1], b3)
        else:
            b6 = max(fonk2(b9, b10[:-1], b3), fonk2(b9[:-1], b10, b3))
        b3[b4, b5] = b6
        return b6
def fonk3(b9, b10):
    return fonk1(b9, b10)
if b7 = = "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 memoization.py acgt/bits")
        print("acgt - generate sequences of acgt")
        print("bits - generate sequences of binary digits")
    else:
        b8 = sys.argv[1] + ".txt"
        with open(b8, 'r') as f:
            b9 = f.readline().strip()
            b10 = f.readline().strip()
            print("LCS length: " + str(fonk3(b9, b10)))
            print("Number of recursive calls: " + str(a1)))
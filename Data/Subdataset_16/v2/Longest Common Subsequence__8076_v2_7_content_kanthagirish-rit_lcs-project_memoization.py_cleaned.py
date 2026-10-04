
import sys
import numpy as np
a1 = 0
def fonk1(b6, b7):
    m, b1 = len(b6), len(b7)
    b2 = np.full((m, b1), -1, dtype='int64')
    return fonk2(b6, b7, b2)
def fonk2(b6, b7, b2):
    global a1
    a1 += 1
    if not b6 or not b7:
        return 0
    i, b3 = len(b6) - 1, len(b7) - 1
    if b2[i, b3] > -1:
        return b2[i, b3]
    if b6[-1] == b7[-1]:
        b2[i, b3] = 1 + fonk2(b6[:-1], b7[:-1], b2)
    else:
        b2[i, b3] = max(fonk2(b6, b7[:-1], b2), fonk2(b6[:-1], b7, b2))
    return b2[i, b3]
def fonk3(b6, b7):
    return fonk1(b6, b7)
if b4 = = "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__} <b5>")
    else:
        b5 = sys.argv[1]
        with open(b5, 'r') as f:
            b6 = f.readline().strip()
            b7 = f.readline().strip()
            b8 = fonk3(b6, b7)
            print(f"LCS length: {b8}")
            print(f"Number of recursive calls: {a1}")
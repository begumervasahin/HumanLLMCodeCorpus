
import sys
import numpy as np
a1 = 0
def fonk1(b5, b6):
    m, b1 = len(b5), len(b6)
    b2 = np.full((m, b1), -1, dtype='int64')
    return fonk2(b5, b6, b2)
def fonk2(b5, b6, b2):
    global a1
    a1 += 1
    if not b5 or not b6:
        return 0
    i, b3 = len(b5) - 1, len(b6) - 1
    if b2[i, b3] != -1:
        return b2[i, b3]
    if b5[-1] == b6[-1]:
        b2[i, b3] = 1 + fonk2(b5[:-1], b6[:-1], b2)
    else:
        b2[i, b3] = max(fonk2(b5, b6[:-1], b2), fonk2(b5[:-1], b6, b2))
    return b2[i, b3]
def fonk3(b5, b6):
    return fonk1(b5, b6)
def fonk4():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <b4>")
        return
    b4 = sys.argv[1]
    with open(b4, 'r') as file:
        b5 = file.readline().strip()
        b6 = file.readline().strip()
    b7 = fonk3(b5, b6)
    print(f"LCS length: {b7}")
    print(f"Number of recursive calls: {a1}")
if b8 = = "__main__":
    fonk4()
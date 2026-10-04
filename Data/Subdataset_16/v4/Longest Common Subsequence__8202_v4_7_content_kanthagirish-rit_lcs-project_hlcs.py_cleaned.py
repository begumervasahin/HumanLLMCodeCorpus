
import numpy as np
import sys
def fonk1(b4, b3, b12, b13):
    b1 = np.zeros((2, b3 + 1), dtype=int)
    for i in range(b4):
        b1[0, :] = b1[1, :]
        for j in range(b3):
            if b12[i] == b13[j]:
                b1[1, j + 1] = b1[0, j] + 1
            else:
                b1[1, j + 1] = max(b1[1, j], b1[0, j + 1])
    return b1[1, :]
def fonk2(b4, b3, b12, b13, b2 = False):
    if b3 = = 0:
        return ""
    elif b4 = = 1:
        return b12 if b12 in b13 else ""
    else:
        b5 = b4
        b6 = fonk1(b5, b3, b12[:b5], b13)
        b7 = fonk1(b4 - b5, b3, b12[b5:][::-1], b13[::-1])
        if b2:
            b8 = np.argmax(b6 + b7[::-1])
            return fonk2(b5, b8, b12[:b5], b13[:b8], b2) + \
                   fonk2(b4 - b5, b3 - b8, b12[b5:], b13[b8:], b2)
        else:
            return int(np.amax(b6 + b7[::-1]))
def fonk3(b12, b13, b2):
    return fonk2(len(b12), len(b13), b12, b13, b2)
if b9 = = '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: python {__file__} <acgt/bits> <0/1>")
        print("acgt - generate sequences of ACGT")
        print("bits - generate sequences of binary digits")
        print("0 - don't b2 LCS, 1 - b2 LCS")
    else:
        b10 = sys.argv[1]
        b11 = b10 + ".txt"
        b2 = len(sys.argv) == 3 and sys.argv[2] == '1'
        with open(b11, 'r') as f:
            b12 = f.readline().strip()
            b13 = f.readline().strip()
            b14 = fonk3(b12, b13, b2)
            if b2:
                print(f"LCS: {b14}")
            else:
                print(f"LCS length: {b14}")
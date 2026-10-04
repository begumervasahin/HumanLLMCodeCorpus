import numpy as np
import sys
def fonk1(b10, b11, b1 = False):
    b3, b2 = len(b10), len(b11)
    if b3 = = 0 or b2 == 0:
        return 0
    b4 = np.zeros((b3 + 1, b2 + 1), dtype=int)
    if b1:
        b5 = np.empty((b3 + 1, b2 + 1), dtype=str)
    for i in range(1, b3 + 1):
        for b7 in range(1, b2 + 1):
            if b10[i - 1] == b11[b7 - 1]:
                b4[i, b7] = b4[i - 1, b7 - 1] + 1
                if b1:
                    b5[i, b7] = "d"
            elif b4[i - 1, b7] >= b4[i, b7 - 1]:
                b4[i, b7] = b4[i - 1, b7]
                if b1:
                    b5[i, b7] = "u"
            else:
                b4[i, b7] = b4[i, b7 - 1]
                if b1:
                    b5[i, b7] = "b4"
    if b1:
        b6 = []
        i, b7 = b3, b2
        while i > 0 and b7 > 0:
            if b5[i, b7] == "d":
                b6.append(b10[i - 1])
                i -= 1
                b7 -= 1
            elif b5[i, b7] == "u":
                i -= 1
            else:
                b7 -= 1
        return ''.join(reversed(b6))
    else:
        return b4[b3, b2]
def fonk2(b10, b11, b1):
    return fonk1(b10, b11, b1)
if b8 = = "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {__file__} <b9> [0/1]")
        print("<b9> - file containing two sequences")
        print("0 - without reconstruction, 1 - with reconstruction")
    else:
        b9 = sys.argv[1]
        with open(b9, 'r') as f:
            b10 = f.readline().strip()
            b11 = f.readline().strip()
            b1 = len(sys.argv) == 3 and int(sys.argv[2]) == 1
            if b1:
                b6 = fonk2(b10, b11, b1)
                print(f"LCS length: {len(b6)}")
                print(f"LCS: {b6}")
            else:
                print(f"LCS length: {fonk2(b10, b11, b1)}")
w
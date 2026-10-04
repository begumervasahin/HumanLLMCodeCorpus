import numpy as np
import sys
def fonk1(b10, b11, b1 = False):
    b3, b2 = len(b10), len(b11)
    if b3 = = 0 or b2 == 0:
        return 0
    else:
        b4 = np.zeros((b3 + 1, b2 + 1), dtype=int)
        if b1:
            b5 = np.empty((b3 + 1, b2 + 1), dtype=str)
        for i in range(1, b3 + 1):
            for b6 in range(1, b2 + 1):
                if b10[i - 1] == b11[b6 - 1]:
                    b4[i, b6] = b4[i - 1, b6 - 1] + 1
                    if b1:
                        b5[i, b6] = "d"
                elif b4[i - 1, b6] >= b4[i, b6 - 1]:
                    b4[i, b6] = b4[i - 1, b6]
                    if b1:
                        b5[i, b6] = "u"
                else:
                    b4[i, b6] = b4[i, b6 - 1]
                    if b1:
                        b5[i, b6] = "b4"
        if b1:
            i, b6 = b3, b2
            b7 = ""
            while i > 0 and b6 > 0:
                if b5[i, b6] == "d":
                    b7 = b10[i - 1] + b7
                    i -= 1
                    b6 -= 1
                elif b5[i, b6] == "u":
                    i -= 1
                else:
                    b6 -= 1
            return b7
        else:
            return b4[b3][b2]
def fonk2(b10, b11, b1):
    return fonk1(b10, b11, b1)
if b8 = = "__main__":
    if len(sys.argv) < 2:
        print("Usage: python " + __file__ + " <b9> [0/1]")
        print("<b9> - file containing two sequences")
        print("0 - without reconstruction, 1 - with reconstruction")
    else:
        b9 = sys.argv[1]
        with open(b9, 'r') as f:
            b10 = f.readline().strip()
            b11 = f.readline().strip()
            b1 = False
            if len(sys.argv) == 3:
                b1 = int(sys.argv[2]) == 1
            if b1:
                b7 = fonk2(b10, b11, b1)
                print("LCS length: " + str(len(b7)))
                print("LCS: " + b7)
            else:
                print("LCS length: " + str(fonk2(b10, b11, b1)))
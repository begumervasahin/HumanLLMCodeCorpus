import sys
import numpy as np
b1 = np.zeros((2048, 2048), dtype=int)
def fonk1(A, b6):
    m, b2 = len(A), len(b6)
    b1.fill(0)
    for i in range(1, m + 1):
        for j in range(1, b2 + 1):
            if A[i - 1] == b6[j - 1]:
                b1[i][j] = b1[i - 1][j - 1] + 1
            else:
                b1[i][j] = max(b1[i - 1][j], b1[i][j - 1])
    return b1[m][b2]
def fonk2(A, b6):
    b3 = fonk1(A, b6)
    for i in range(1, len(A)):
        b4 = A[i:] + A[:i]
        b5 = fonk1(b4, b6)
        if b5 > b3:
            b3 = b5
    return b3
def fonk3():
    if len(sys.argv) != 1:
        sys.exit('Usage: python LCS.py < input')
    for line in sys.stdin:
        A, b6 = line.strip().split()
        b7 = fonk2(A, b6)
        print(b7)
if b8 = = '__main__':
    fonk3()
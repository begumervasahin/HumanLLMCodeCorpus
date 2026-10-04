import sys
import numpy as np
def fonk1(size):
    return np.zeros((size, size), b1 = int)
def fonk2(A, b4, b3):
    m, b2 = len(A), len(b4)
    for i in range(1, m + 1):
        for j in range(1, b2 + 1):
            if A[i - 1] == b4[j - 1]:
                b3[i][j] = b3[i - 1][j - 1] + 1
            else:
                b3[i][j] = max(b3[i - 1][j], b3[i][j - 1])
    return b3[m][b2]
def fonk3():
    if len(sys.argv) != 1:
        sys.exit('Usage: python LCS.py < input')
    b3 = fonk1(2048)
    for line in sys.stdin:
        A, b4 = line.strip().split()
        print(fonk2(A, b4, b3))
if b5 = = '__main__':
    fonk3()
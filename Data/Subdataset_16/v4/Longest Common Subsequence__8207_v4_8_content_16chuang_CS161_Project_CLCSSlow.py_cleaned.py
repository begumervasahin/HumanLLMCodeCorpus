import sys
import numpy as np
def fonk1(A, b6):
    m, b1 = len(A), len(b6)
    b2 = np.zeros((m+1, b1+1), dtype=int)
    for i in range(1, m+1):
        for j in range(1, b1+1):
            if A[i-1] == b6[j-1]:
                b2[i][j] = b2[i-1][j-1] + 1
            else:
                b2[i][j] = max(b2[i-1][j], b2[i][j-1])
    return b2[m][b1]
def fonk2(A, b6):
    b3 = fonk1(A, b6)
    for i in range(len(A)):
        b4 = A[i:] + A[:i]
        b5 = fonk1(b4, b6)
        if b5 > b3:
            b3 = b5
    return b3
def fonk3():
    if len(sys.argv) != 1:
        sys.exit('Usage: python LCS.py < input')
    for line in sys.stdin:
        A, b6 = line.split()
        print(fonk2(A, b6))
if b7 = = '__main__':
    fonk3()
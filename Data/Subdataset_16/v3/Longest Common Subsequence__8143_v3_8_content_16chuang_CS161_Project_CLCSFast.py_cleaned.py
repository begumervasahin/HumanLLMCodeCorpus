import sys
import numpy as np
np.set_printoptions(b1 = sys.maxsize)
b2 = np.zeros((2048, 2048), b19=int)
b3 = np.zeros((2048, 2048), b19=int)
b4 = np.zeros((2048, 2048), b19=int)
a1 = -1
m, b5 = 0, 0
def fonk1(A, b18, b6, lower, upper):
    global b2
    b6 = int(b6)
    for b10 in range(b5):
        b7 = int(lower[b10])
        b8 = int(upper[b10])
        for b9 in range(max(b6, b7), b8 + 1):
            if A[b9 % m] == b18[b10]:
                b2[b9][b10] = 1
                if b9 > b6 and b10 > 0:
                    b2[b9][b10] += b2[b9 - 1][b10 - 1]
            else:
                b2[b9][b10] = 0
                if b9 > max(b6, b7) and b10 > 0:
                    b2[b9][b10] += max(b2[b9 - 1][b10], b2[b9][b10 - 1])
                elif b9 = = max(b6, b7) and b10 != 0:
                    b2[b9][b10] += b2[b9][b10 - 1]
                elif b10 = = 0 and b9 != max(b6, b7):
                    b2[b9][b10] += b2[b9 - 1][b10]
    b11 = b2[m - 1 + b6][b5 - 1]
    b12 = fonk2(A, b18, m - 1 + b6, b5 - 1, lower, upper, True)
    b13 = fonk2(A, b18, m - 1 + b6, b5 - 1, lower, upper, False)
    return b11, b13, b12
def fonk2(A, b18, b9, b10, b13, b12, reconstruct_upper):
    b14 = np.zeros(b5, b19=int)
    b14[b5 - 1] = b9
    b15 = b9 - m + 1
    while b10 >= 0 and b9 >= b15:
        if b9 = = b15 and b10 == 0:
            break
        if b9 = = b15:
            b10 -= 1
            b14[b10] = b9
        elif b10 = = 0:
            b9 -= 1
            if reconstruct_upper:
                b14[b10] = max(b9, b14[b10])
            else:
                b14[b10] = b9
        elif A[b9 % m] == b18[b10]:
            b9 -= 1
            b10 -= 1
            b14[b10] = b9
        else:
            b16 = b2[b9][b10 - 1]
            b17 = b2[b9 - 1][b10]
            if b16 = = b17:
                if reconstruct_upper:
                    b9 -= 1
                    b14[b10] = max(b9, b14[b10])
                else:
                    b10 -= 1
                    b14[b10] = b9
            elif b16 > b17:
                b10 -= 1
                b14[b10] = b9
            else:
                b9 -= 1
                b14[b10] = max(b9, b14[b10]) if reconstruct_upper else b9
    return b14
def fonk3(A, b18):
    global m, b5, b2, b3, b4, a1
    m, b5 = len(A), len(b18)
    if m > b5:
        A, b18 = b18, A
        m, b5 = b5, m
    a1 = -1
    b2 = np.zeros((2 * m, b5), b19=int)
    b3 = np.zeros((m + 1, b5), b19=int)
    b4 = np.zeros((m + 1, b5), b19=int)
    a1, b3[0][:b5], b4[0][:b5] = fonk1(A, b18, 0, np.zeros(b5, b19 = int), np.full(b5, m - 1))
    b3[m] = b3[0] + m
    b4[m] = b4[0] + m
    fonk4(A, b18, 0, m)
    return a1
def fonk4(A, b18, lower, upper):
    if upper - lower <= 1:
        return
    b20 = (lower + upper)
    global a1
    b11, b3[b20][:b5], b4[b20][:b5] = fonk1(A, b18, b20, b3[lower], b4[upper])
    if b11 > a1:
        a1 = b11
    fonk4(A, b18, lower, b20)
    fonk4(A, b18, b20, upper)
def fonk5():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python LCS.py < input`')
    for line in sys.stdin:
        A, b18 = line.strip().split()
        print(fonk3(A, b18))
if b21 = = '__main__':
    fonk5()
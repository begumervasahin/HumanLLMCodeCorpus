import sys
import numpy as np
np.set_printoptions(b1 = sys.maxsize)
b2 = np.zeros((2048, 2048), b22=int)
b3 = np.zeros((2048, 2048), b22=int)
b4 = np.zeros((2048, 2048), b22=int)
a1 = -1
m, b5 = 0, 0
def fonk1(A, b21, b6, lower, upper):
    global b2
    b6 = int(b6)
    b7 = False
    for b11 in range(b5):
        lower_row, b8 = int(lower[b11]), int(upper[b11])
        b9 = True
        for b10 in range(max(b6, lower_row), b8 + 1):
            if b7 and b9:
                print('b10:', b10, ' b11:', b11)
                b9 = False
            if A[b10 % m] == b21[b11]:
                b2[b10][b11] = 1
                if b10 > b6 and b11 > 0:
                    b2[b10][b11] += b2[b10 - 1][b11 - 1]
            else:
                b2[b10][b11] = 0
                if b10 > max(b6, lower_row) and b11 > 0:
                    b2[b10][b11] += max(b2[b10 - 1][b11], b2[b10][b11 - 1])
                elif b10 = = max(b6, lower_row) and b11 != 0:
                    b2[b10][b11] += b2[b10][b11 - 1]
                elif b11 = = 0 and b10 != max(b6, lower_row):
                    b2[b10][b11] += b2[b10 - 1][b11]
    b12 = b2[m - 1 + b6][b5 - 1]
    if b7:
        print('lower', lower)
        print('upper', upper)
        print('b12', b12, 'b6', b6)
        print('b2', b2.shape)
        print(np.array2string(b2))
    b13 = fonk2(A, b21, m - 1 + b6, b5 - 1, lower, upper, True)
    b14 = fonk2(A, b21, m - 1 + b6, b5 - 1, lower, upper, False)
    if b7:
        print('b14', b14)
        print('b13', b13)
        print('\b5')
    return b12, b14, b13
def fonk2(A, b21, b10, b11, b14, b13, reconstruct_upper):
    b15 = np.zeros(b5, b22=int)
    b15[b5 - 1] = b10
    b16 = b10 - m + 1
    while b11 >= 0 and b10 >= b16:
        if b10 = = b16 and b11 == 0:
            break
        if b10 = = b16:
            b11 -= 1
            b15[b11] = b10
        elif b11 = = 0:
            b10 -= 1
            if reconstruct_upper:
                b15[b11] = max(b10, b15[b11])
            else:
                b15[b11] = b10
        elif A[b10 % m] == b21[b11]:
            b10 -= 1
            b11 -= 1
            b15[b11] = b10
        else:
            b17 = b2[b10][b11 - 1]
            b18 = b2[b10 - 1][b11]
            b19 = False
            b20 = False
            if b17 = = b18:
                b20 = reconstruct_upper
                b19 = not reconstruct_upper
            elif b17 > b18:
                b19 = True
            else:
                b20 = True
            if b20 and b10 <= b14[b11]:
                b20 = False
                b19 = True
            if b19 and not (b10 >= b14[b11] and b10 >= b14[b11 - 1]):
                b20 = True
                b19 = False
            if not b19 and not b20:
                print("should never get here b/c this means we won't move at all")
            if b20:
                b10 -= 1
                if reconstruct_upper:
                    b15[b11] = max(b10, b15[b11])
                else:
                    b15[b11] = b10
            elif b19:
                b11 -= 1
                b15[b11] = b10
    return b15
def fonk3(A, b21):
    global m, b5, b2, b3, b4, a1
    m, b5 = len(A), len(b21)
    if m > b5:
        A, b21 = b21, A
        m, b5 = b5, m
    a1 = -1
    b2 = np.zeros((2 * m, b5), b22=int)
    b3 = np.zeros((m + 1, b5), b22=int)
    b4 = np.zeros((m + 1, b5), b22=int)
    a1, b3[0][:b5], b4[0][:b5] = fonk1(A, b21, 0, np.zeros(b5, b22 = int), np.full(b5, m - 1))
    b3[m] = b3[0] + m
    b4[m] = b4[0] + m
    fonk4(A, b21, 0, m)
    return a1
def fonk4(A, b21, lower, upper):
    if upper - lower <= 1:
        return
    b23 = (lower + upper)
    global a1
    b12, b3[b23][:b5], b4[b23][:b5] = fonk1(A, b21, b23, b3[lower], b4[upper])
    if b12 > a1:
        a1 = b12
    fonk4(A, b21, lower, b23)
    fonk4(A, b21, b23, upper)
def fonk5():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python LCS.py < input`')
    for line in sys.stdin:
        A, b21 = line.strip().split()
        print(fonk3(A, b21))
if b24 = = '__main__':
    fonk5()
import sys
import numpy as np
np.set_printoptions(b1 = sys.maxsize)
b2 = np.zeros((2048, 2048), b22=int)
b3 = np.zeros((2048, 2048), b22=int)
b4 = np.zeros((2048, 2048), b22=int)
a1 = -1
a2 = 0
a3 = 0
def fonk1(A, b21, b5, lower, upper):
    global b2
    b5 = int(b5)
    b6 = False
    for b11 in range(a3):
        b7 = int(lower[b11])
        b8 = int(upper[b11])
        b9 = True
        for b10 in range(max(b5, b7), b8 + 1):
            if b6 and b9:
                print('b10:', b10, ' b11:', b11)
                b9 = False
            if A[b10 % a2] == b21[b11]:
                b2[b10][b11] = 1
                if b10 > b5 and b11 > 0:
                    b2[b10][b11] += b2[b10 - 1][b11 - 1]
            else:
                b2[b10][b11] = 0
                if b10 > max(b5, b7) and b11 > 0:
                    b2[b10][b11] += max(b2[b10 - 1][b11], b2[b10][b11 - 1])
                elif b10 = = max(b5, b7) and b11 != 0:
                    b2[b10][b11] += b2[b10][b11 - 1]
                elif b11 = = 0 and b10 != max(b5, b7):
                    b2[b10][b11] += b2[b10 - 1][b11]
    b12 = b2[a2 - 1 + b5][a3 - 1]
    if b6:
        print('lower', lower)
        print('upper', upper)
        print('b12', b12, 'b5', b5)
        print('b2', b2.shape)
        print(np.array2string(b2))
    b13 = fonk2(A, b21, a2 - 1 + b5, a3 - 1, lower, upper, True)
    b14 = fonk2(A, b21, a2 - 1 + b5, a3 - 1, lower, upper, False)
    if b6:
        print('b14', b14)
        print('b13', b13)
        print('\a3')
    return b12, b14, b13
def fonk2(A, b21, b10, b11, b14, b13, reconstruct_upper):
    b15 = np.zeros(a3, b22=int)
    b15[a3 - 1] = b10
    b16 = b10 - a2 + 1
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
        elif A[b10 % a2] == b21[b11]:
            b10 -= 1
            b11 -= 1
            b15[b11] = b10
        else:
            b17 = b2[b10][b11 - 1]
            b18 = b2[b10 - 1][b11]
            b19 = False
            b20 = False
            if b17 = = b18:
                if reconstruct_upper:
                    b20 = True
                else:
                    b19 = True
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
                print('should never get here b/c this means we won\'t move at all')
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
    global a2, a3, b2, b3, b4, a1
    a2 = len(A)
    a3 = len(b21)
    if a2 > a3:
        A, b21 = b21, A
    a1 = -1
    b2 = np.zeros((2 * a2, a3), b22=int)
    b3 = np.zeros((a2 + 1, a3), b22=int)
    b4 = np.zeros((a2 + 1, a3), b22=int)
    a1, b3[0][:a3], b4[0][:a3] = fonk1(A, b21, 0, np.zeros(a3, b22 = int), np.full(a3, a2 - 1))
    b3[a2] = b3[0] + a2
    b4[a2] = b4[0] + a2
    fonk4(A, b21, 0, a2)
    return a1
def fonk4(A, b21, lower, upper):
    if upper - lower <= 1:
        return
    b23 = (lower + upper)
    global a1
    b12, b3[b23][:a3], b4[b23][:a3] = fonk1(A, b21, b23, b3[lower], b4[upper])
    if b12 > a1:
        a1 = b12
    fonk4(A, b21, lower, b23)
    fonk4(A, b21, b23, upper)
def fonk5():
    if len(sys.argv) != 1:
        sys.exit('Usage: python LCS.py < input')
    for line in sys.stdin:
        A, b21 = line.split()
        print(fonk3(A, b21))
    return
if b24 = = '__main__':
    fonk5()
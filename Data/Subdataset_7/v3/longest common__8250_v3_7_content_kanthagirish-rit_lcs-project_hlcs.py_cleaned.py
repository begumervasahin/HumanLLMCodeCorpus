import numpy as np
import sys
def fonk1(b4, b3, A, B):
    b1 = np.zeros(shape=(2, b3+1), dtype='int64')
    for i in range(b4):
        b1[0, :] = b1[1, :]
        for j in range(b3):
            if A[i] == B[j]:
                b1[1, j+1] = b1[0, j] + 1
            else:
                b1[1, j+1] = max(b1[1, j], b1[0, j+1])
    return b1[1, :]
def fonk2(b4, b3, A, B, b2 = False):
    if b3 = = 0:
        return ""
    elif b4 = = 1:
        if A in B:
            return A
        else:
            return ""
    else:
        b5 = b4
        b6 = fonk1(b5, b3, A[:b5], B)
        b7 = fonk1(b4-b5, b3, A[b5:][::-1], B[::-1])
        if b2:
            b8 = np.argmax(b6 + b7[::-1])
            return (fonk2(b5, b8, A[:b5], B[:b8], b2) +
                    fonk2(b4-b5, b3-b8, A[b5:], B[b8:], b2))
        else:
            return int(np.amax(b6 + b7[::-1]))
def fonk3(A, B, b2):
    return fonk2(len(A), len(B), A, B, b2)
if b9 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 replicate_hlcs.py <b10> <b11>")
        print("b10 - text file containing two sequences separated by newline")
        print("b11 - 0 for not reconstructing LCS, 1 for reconstructing LCS")
    else:
        b10 = sys.argv[1]
        b11 = int(sys.argv[2])
        with open(b10, 'r') as f:
            b12 = f.readline().strip()
            b13 = f.readline().strip()
            if b11:
                print("LCS length: " + str(len(fonk3(b12, b13, True))))
            else:
                print("LCS length: " + str(fonk3(b12, b13, False))))
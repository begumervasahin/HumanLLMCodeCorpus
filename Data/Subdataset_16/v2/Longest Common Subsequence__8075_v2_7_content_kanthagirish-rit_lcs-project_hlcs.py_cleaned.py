import numpy as np
import sys
def fonk1(b4, b3, A, B):
    b1 = np.zeros((2, b3 + 1), dtype='int64')
    for b5 in range(b4):
        b1[0, :] = b1[1, :]
        for j in range(b3):
            if A[b5] == B[j]:
                b1[1, j + 1] = b1[0, j] + 1
            else:
                b1[1, j + 1] = max(b1[1, j], b1[0, j + 1])
    return b1[1, :]
def fonk2(b4, b3, A, B, b2 = False):
    if b3 = = 0:
        return ""
    elif b4 = = 1:
        return A if A in B else ""
    else:
        b5 = b4
        b6 = fonk1(b5, b3, A[:b5], B)
        b7 = fonk1(b4 - b5, b3, A[b5:][::-1], B[::-1])
        if b2:
            b8 = np.argmax(b6 + b7[::-1])
            return fonk2(b5, b8, A[:b5], B[:b8], b2) + fonk2(b4 - b5, b3 - b8, A[b5:], B[b8:], b2)
        else:
            return int(np.amax(b6 + b7[::-1]))
def fonk3(A, B, b2):
    return fonk2(len(A), len(B), A, B, b2)
if b9 = = '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 " + __file__ + " <input_type> <reconstruct_flag>")
        print("<input_type> - 'acgt' for sequences of acgt, 'bits' for binary sequences")
        print("<reconstruct_flag> - '0' to not b2 LCS, '1' to b2 LCS")
    else:
        b10 = sys.argv[1] + ".txt"
        with open(b10, 'r') as f:
            b11 = f.readline().strip()
            b12 = f.readline().strip()
            b2 = False
            if len(sys.argv) == 3:
                b2 = int(sys.argv[2]) == 1
            if b2:
                b13 = fonk3(b11, b12, b2)
                print("LCS length: " + str(len(b13)))
                print("LCS: " + b13)
            else:
                print("LCS length: " + str(fonk3(b11, b12, b2)))
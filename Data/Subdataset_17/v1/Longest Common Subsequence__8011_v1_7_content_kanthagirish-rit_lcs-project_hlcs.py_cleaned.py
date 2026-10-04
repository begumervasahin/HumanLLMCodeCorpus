import numpy as np
import sys
def alg_b(m, n, A, B):
    K = np.zeros(shape=(2, n+1), dtype='int64')
    for i in range(m):
        K[0, :] = K[1, :]
        for j in range(n):
            if A[i] == B[j]:
                K[1, j+1] = K[0, j] + 1
            else:
                K[1, j+1] = max(K[1, j], K[0, j+1])
    return K[1, :]
def alg_c(m, n, A, B, reconstruct=False):
    if n == 0:
        return ""
    elif m == 1:
        if A in B:
            return A
        else:
            return ""
    else:
        i = m
        L1 = alg_b(i, n, A[:i], B)
        L2 = alg_b(m-i, n, A[i:][::-1], B[::-1])
        if reconstruct:
            k = np.argmax(L1 + L2[::-1])
            return alg_c(i, k, A[:i], B[:k], reconstruct) + alg_c(m-i, n-k, A[i:], B[k:], reconstruct)
        else:
            return int(np.amax(L1 + L2[::-1]))
def test(A, B, reconstruct):
    return alg_c(len(A), len(B), A, B, reconstruct)
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 " + __file__ + " acgt/bits 0/1")
        print("acgt - generate sequences of acgt")
        print("bits- generate sequences of binary digits")
        print("0- don't reconstruct LCS, 1-reconstruct LCS")
    else:
        file = sys.argv[1] + ".txt"
        with open(file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            reconstruct = False
            if len(sys.argv) == 3:
                reconstruct = int(sys.argv[2]) == 1
            if reconstruct:
                print("LCS length: " + str(len(test(x, y, reconstruct))))
                print("LCS: " + test(x, y, reconstruct))
            else:
                print("LCS length: " + str(test(x, y, reconstruct)))
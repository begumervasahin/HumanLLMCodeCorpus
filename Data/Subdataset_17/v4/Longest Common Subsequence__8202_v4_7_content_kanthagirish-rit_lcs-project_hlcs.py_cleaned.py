
import numpy as np
import sys
def compute_last_row_lcs(m, n, A, B):
    K = np.zeros((2, n + 1), dtype=int)
    for i in range(m):
        K[0, :] = K[1, :]
        for j in range(n):
            if A[i] == B[j]:
                K[1, j + 1] = K[0, j] + 1
            else:
                K[1, j + 1] = max(K[1, j], K[0, j + 1])
    return K[1, :]
def compute_lcs(m, n, A, B, reconstruct=False):
    if n == 0:
        return ""
    elif m == 1:
        return A if A in B else ""
    else:
        mid = m
        L1 = compute_last_row_lcs(mid, n, A[:mid], B)
        L2 = compute_last_row_lcs(m - mid, n, A[mid:][::-1], B[::-1])
        if reconstruct:
            k = np.argmax(L1 + L2[::-1])
            return compute_lcs(mid, k, A[:mid], B[:k], reconstruct) + \
                   compute_lcs(m - mid, n - k, A[mid:], B[k:], reconstruct)
        else:
            return int(np.amax(L1 + L2[::-1]))
def test_lcs(A, B, reconstruct):
    return compute_lcs(len(A), len(B), A, B, reconstruct)
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: python {__file__} <acgt/bits> <0/1>")
        print("acgt - generate sequences of ACGT")
        print("bits - generate sequences of binary digits")
        print("0 - don't reconstruct LCS, 1 - reconstruct LCS")
    else:
        file_type = sys.argv[1]
        file_name = file_type + ".txt"
        reconstruct = len(sys.argv) == 3 and sys.argv[2] == '1'
        with open(file_name, 'r') as f:
            A = f.readline().strip()
            B = f.readline().strip()
            result = test_lcs(A, B, reconstruct)
            if reconstruct:
                print(f"LCS: {result}")
            else:
                print(f"LCS length: {result}")
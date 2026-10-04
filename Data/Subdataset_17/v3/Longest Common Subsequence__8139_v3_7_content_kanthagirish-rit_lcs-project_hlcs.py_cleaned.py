import numpy as np
import sys
def compute_final_row(m, n, A, B):
    K = np.zeros((2, n + 1), dtype='int64')
    for i in range(m):
        K[0, :] = K[1, :]
        for j in range(n):
            if A[i] == B[j]:
                K[1, j + 1] = K[0, j] + 1
            else:
                K[1, j + 1] = max(K[1, j], K[0, j + 1])
    return K[1, :]
def hirschberg_lcs(m, n, A, B, reconstruct=False):
    if n == 0:
        return ""
    elif m == 1:
        return A if A in B else ""
    else:
        mid = m
        L1 = compute_final_row(mid, n, A[:mid], B)
        L2 = compute_final_row(m - mid, n, A[mid:][::-1], B[::-1])
        if reconstruct:
            k = np.argmax(L1 + L2[::-1])
            return (hirschberg_lcs(mid, k, A[:mid], B[:k], reconstruct) +
                    hirschberg_lcs(m - mid, n - k, A[mid:], B[k:], reconstruct))
        else:
            return int(np.amax(L1 + L2[::-1]))
def compute_lcs(A, B, reconstruct):
    return hirschberg_lcs(len(A), len(B), A, B, reconstruct)
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 " + __file__ + " <input_type> <reconstruct_flag>")
        print("<input_type> - 'acgt' for sequences of acgt, 'bits' for binary sequences")
        print("<reconstruct_flag> - '0' to not reconstruct LCS, '1' to reconstruct LCS")
        return
    file = sys.argv[1] + ".txt"
    try:
        with open(file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
    except FileNotFoundError:
        print(f"File {file} not found.")
        return
    reconstruct = False
    if len(sys.argv) == 3:
        reconstruct = int(sys.argv[2]) == 1
    if reconstruct:
        lcs = compute_lcs(x, y, reconstruct)
        print("LCS length: " + str(len(lcs)))
        print("LCS: " + lcs)
    else:
        print("LCS length: " + str(compute_lcs(x, y, reconstruct)))
if __name__ == '__main__':
    main()
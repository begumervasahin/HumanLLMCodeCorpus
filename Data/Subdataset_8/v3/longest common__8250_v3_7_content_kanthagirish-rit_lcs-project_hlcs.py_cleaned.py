import numpy as np
import sys
def hirschberg_linear_space(m, n, A, B):
    dp_table = np.zeros(shape=(2, n+1), dtype='int64')
    for i in range(m):
        dp_table[0, :] = dp_table[1, :]
        for j in range(n):
            if A[i] == B[j]:
                dp_table[1, j+1] = dp_table[0, j] + 1
            else:
                dp_table[1, j+1] = max(dp_table[1, j], dp_table[0, j+1])
    return dp_table[1, :]
def longest_common_subsequence(m, n, A, B, reconstruct=False):
    if n == 0:
        return ""
    elif m == 1:
        if A in B:
            return A
        else:
            return ""
    else:
        mid = m
        L1 = hirschberg_linear_space(mid, n, A[:mid], B)
        L2 = hirschberg_linear_space(m-mid, n, A[mid:][::-1], B[::-1])
        if reconstruct:
            k = np.argmax(L1 + L2[::-1])
            return (longest_common_subsequence(mid, k, A[:mid], B[:k], reconstruct) +
                    longest_common_subsequence(m-mid, n-k, A[mid:], B[k:], reconstruct))
        else:
            return int(np.amax(L1 + L2[::-1]))
def test_lcs(A, B, reconstruct):
    return longest_common_subsequence(len(A), len(B), A, B, reconstruct)
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 replicate_hlcs.py <sequence_file> <reconstruct_flag>")
        print("sequence_file - text file containing two sequences separated by newline")
        print("reconstruct_flag - 0 for not reconstructing LCS, 1 for reconstructing LCS")
    else:
        sequence_file = sys.argv[1]
        reconstruct_flag = int(sys.argv[2])
        with open(sequence_file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            if reconstruct_flag:
                print("LCS length: " + str(len(test_lcs(x, y, True))))
            else:
                print("LCS length: " + str(test_lcs(x, y, False))))
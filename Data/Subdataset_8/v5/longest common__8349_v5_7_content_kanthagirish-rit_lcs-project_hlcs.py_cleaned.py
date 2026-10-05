import numpy as np
import sys
def hirschberg_linear_space(m, n, A, B):
    dp = np.zeros(shape=(2, n+1), dtype='int64')
    for i in range(m):
        dp[0, :] = dp[1, :]
        for j in range(n):
            if A[i] == B[j]:
                dp[1, j+1] = dp[0, j] + 1
            else:
                dp[1, j+1] = max(dp[1, j], dp[0, j+1])
    return dp[1, :]
def longest_common_subsequence(m, n, A, B, reconstruct=False):
    if n == 0:
        return ""
    elif m == 1:
        return A if A in B else ""
    midpoint = m
    L1 = hirschberg_linear_space(midpoint, n, A[:midpoint], B)
    L2 = hirschberg_linear_space(m - midpoint, n, A[midpoint:][::-1], B[::-1])
    if reconstruct:
        k = np.argmax(L1 + L2[::-1])
        return longest_common_subsequence(midpoint, k, A[:midpoint], B[:k], reconstruct) \
            + longest_common_subsequence(m - midpoint, n - k, A[midpoint:], B[k:], reconstruct)
    else:
        return int(np.amax(L1 + L2[::-1]))
def test_lcs(A, B, reconstruct):
    return longest_common_subsequence(len(A), len(B), A, B, reconstruct)
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 " + sys.argv[0] + " acgt/bits 0/1")
        print("acgt - generate sequences of acgt")
        print("bits- generate sequences of binary digits")
        print("0- don't reconstruct LCS, 1-reconstruct LCS")
    else:
        file = sys.argv[1] + ".txt"
        with open(file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            reconstruct = len(sys.argv) == 3 and int(sys.argv[2]) == 1
            if reconstruct:
                print("LCS length:", len(test_lcs(x, y, reconstruct)))
            else:
                print("LCS length:", test_lcs(x, y, reconstruct))
import sys
import numpy as np
dp_table = np.zeros((2048, 2048), dtype=int)
def longest_common_subsequence_length(A, B):
    m = len(A)
    n = len(B)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])
    return dp_table[m][n]
def cyclic_longest_common_subsequence_length(A, B):
    longest = longest_common_subsequence_length(A, B)
    for i in range(len(A)):
        rotated = A[i:] + A[:i]
        clcs = longest_common_subsequence_length(rotated, B)
        if clcs > longest:
            longest = clcs
    return longest
def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python LCS.py < input`')
    for line in sys.stdin:
        A, B = line.split()
        print(cyclic_longest_common_subsequence_length(A, B))
if __name__ == '__main__':
    main()
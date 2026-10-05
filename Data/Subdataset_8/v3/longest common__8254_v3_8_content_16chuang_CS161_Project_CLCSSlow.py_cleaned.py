import sys
import numpy as np
memoization_table = np.zeros((2048, 2048), dtype=int)
def find_LCS_length(A, B):
    m = len(A)
    n = len(B)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                memoization_table[i][j] = memoization_table[i - 1][j - 1] + 1
            else:
                memoization_table[i][j] = max(memoization_table[i - 1][j], memoization_table[i][j - 1])
    return memoization_table[m][n]
def find_LCRS_length(A, B):
    longest = find_LCS_length(A, B)
    for i in range(0, len(A)):
        rotated = A[i:] + A[:i]
        clrs = find_LCS_length(rotated, B)
        if clrs > longest:
            longest = clrs
    return longest
def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python LCS.py < input`')
    for line in sys.stdin:
        A, B = line.split()
        print(find_LCRS_length(A, B))
if __name__ == '__main__':
    main()
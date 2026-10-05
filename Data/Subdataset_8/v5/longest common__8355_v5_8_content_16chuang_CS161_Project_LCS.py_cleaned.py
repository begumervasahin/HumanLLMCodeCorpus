import sys
import numpy as np
memoization_table = np.zeros((2048, 2048), dtype=int)
def longest_common_subsequence(A, B):
    len_A = len(A)
    len_B = len(B)
    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            if A[i - 1] == B[j - 1]:
                memoization_table[i][j] = memoization_table[i - 1][j - 1] + 1
            else:
                memoization_table[i][j] = max(memoization_table[i - 1][j], memoization_table[i][j - 1])
    return memoization_table[len_A][len_B]
def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python LCS.py < input`')
    for line in sys.stdin:
        A, B = line.split()
        print(longest_common_subsequence(A, B))
if __name__ == '__main__':
    main()
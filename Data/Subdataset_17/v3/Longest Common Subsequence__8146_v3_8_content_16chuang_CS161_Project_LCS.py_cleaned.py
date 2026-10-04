import sys
import numpy as np
def initialize_array(size):
    return np.zeros((size, size), dtype=int)
def LCS(A, B, arr):
    m, n = len(A), len(B)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
    return arr[m][n]
def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: python LCS.py < input')
    arr = initialize_array(2048)
    for line in sys.stdin:
        A, B = line.strip().split()
        print(LCS(A, B, arr))
if __name__ == '__main__':
    main()
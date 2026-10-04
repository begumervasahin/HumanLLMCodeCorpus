import sys
import numpy as np
arr = np.zeros((2048, 2048), dtype=int)
def calculate_lcs(A, B):
    m, n = len(A), len(B)
    arr.fill(0)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
    return arr[m][n]
def calculate_clcs(A, B):
    longest_clcs = calculate_lcs(A, B)
    for i in range(1, len(A)):
        rotated_A = A[i:] + A[:i]
        current_clcs = calculate_lcs(rotated_A, B)
        if current_clcs > longest_clcs:
            longest_clcs = current_clcs
    return longest_clcs
def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: python LCS.py < input')
    for line in sys.stdin:
        A, B = line.strip().split()
        result = calculate_clcs(A, B)
        print(result)
if __name__ == '__main__':
    main()
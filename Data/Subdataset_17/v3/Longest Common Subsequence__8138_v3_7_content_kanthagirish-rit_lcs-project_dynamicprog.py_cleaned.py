import numpy as np
import sys
def dp_lcs(x, y, reconstruct=False):
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return 0
    lcs_length_matrix = np.zeros((m + 1, n + 1), dtype=int)
    direction_matrix = np.empty((m + 1, n + 1), dtype=str) if reconstruct else None
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                lcs_length_matrix[i, j] = lcs_length_matrix[i - 1, j - 1] + 1
                if reconstruct:
                    direction_matrix[i, j] = "d"
            elif lcs_length_matrix[i - 1, j] >= lcs_length_matrix[i, j - 1]:
                lcs_length_matrix[i, j] = lcs_length_matrix[i - 1, j]
                if reconstruct:
                    direction_matrix[i, j] = "u"
            else:
                lcs_length_matrix[i, j] = lcs_length_matrix[i, j - 1]
                if reconstruct:
                    direction_matrix[i, j] = "l"
    if reconstruct:
        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if direction_matrix[i, j] == "d":
                lcs.append(x[i - 1])
                i -= 1
                j -= 1
            elif direction_matrix[i, j] == "u":
                i -= 1
            else:
                j -= 1
        return ''.join(reversed(lcs))
    return lcs_length_matrix[m, n]
def test(x, y, reconstruct):
    return dp_lcs(x, y, reconstruct)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {__file__} <input_file> [0/1]")
        print("<input_file> - file containing two sequences")
        print("0 - without reconstruction, 1 - with reconstruction")
    else:
        input_file = sys.argv[1]
        with open(input_file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            reconstruct = len(sys.argv) == 3 and int(sys.argv[2]) == 1
            if reconstruct:
                lcs = test(x, y, reconstruct)
                print(f"LCS length: {len(lcs)}")
                print(f"LCS: {lcs}")
            else:
                lcs_length = test(x, y, reconstruct)
                print(f"LCS length: {lcs_length}")
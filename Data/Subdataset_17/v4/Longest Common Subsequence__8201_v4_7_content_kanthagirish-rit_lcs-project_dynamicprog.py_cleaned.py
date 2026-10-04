
import numpy as np
import sys
def dp_lcs(x, y, reconstruct=False):
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return 0
    l = np.zeros((m + 1, n + 1), dtype='int64')
    if reconstruct:
        b = np.array([[""] * (n + 1)] * (m + 1))
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                l[i, j] = l[i - 1, j - 1] + 1
                if reconstruct:
                    b[i, j] = "d"
            elif l[i - 1, j] >= l[i, j - 1]:
                l[i, j] = l[i - 1, j]
                if reconstruct:
                    b[i, j] = "u"
            else:
                l[i, j] = l[i, j - 1]
                if reconstruct:
                    b[i, j] = "l"
    if reconstruct:
        i, j = m, n
        lcs = ""
        while i > 0 and j > 0:
            if b[i, j] == "d":
                lcs = x[i - 1] + lcs
                i -= 1
                j -= 1
            elif b[i, j] == "u":
                i -= 1
            else:
                j -= 1
        return lcs
    else:
        return l[m][n]
def test(x, y, reconstruct):
    return dp_lcs(x, y, reconstruct)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 dynamicprog.py acgt/bits 0/1")
        print("acgt - generate sequences of acgt")
        print("bits - generate sequences of binary digits")
        print("0 - without reconstruction, 1 - with reconstruction")
    else:
        file = sys.argv[1] + ".txt"
        with open(file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            reconstruct = len(sys.argv) == 3 and int(sys.argv[2]) == 1
            if reconstruct:
                lcs = test(x, y, reconstruct)
                print("LCS length: " + str(len(lcs)))
            else:
                print("LCS length: " + str(test(x, y, reconstruct)))
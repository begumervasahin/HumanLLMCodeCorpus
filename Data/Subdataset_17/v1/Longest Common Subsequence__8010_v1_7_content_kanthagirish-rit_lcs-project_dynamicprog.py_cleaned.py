import numpy as np
import sys
def dp_lcs(x, y, reconstruct=False):
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return 0
    else:
        l = np.zeros((m + 1, n + 1), dtype=int)
        if reconstruct:
            b = np.empty((m + 1, n + 1), dtype=str)
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
        print("Usage: python " + __file__ + " <input_file> [0/1]")
        print("<input_file> - file containing two sequences")
        print("0 - without reconstruction, 1 - with reconstruction")
    else:
        input_file = sys.argv[1]
        with open(input_file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            reconstruct = False
            if len(sys.argv) == 3:
                reconstruct = int(sys.argv[2]) == 1
            if reconstruct:
                lcs = test(x, y, reconstruct)
                print("LCS length: " + str(len(lcs)))
                print("LCS: " + lcs)
            else:
                print("LCS length: " + str(test(x, y, reconstruct)))
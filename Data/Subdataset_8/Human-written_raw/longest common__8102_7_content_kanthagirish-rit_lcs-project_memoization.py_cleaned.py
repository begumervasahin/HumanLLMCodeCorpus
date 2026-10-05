
import sys
import numpy as np
num_recursive_calls = 0
def memoization(x, y):
    m = len(x)
    n = len(y)
    c = np.ones(shape=(m, n), dtype='int64')*-1
    return memoized_LCS(x, y, c)
def memoized_LCS(x, y, c):
    global num_recursive_calls
    num_recursive_calls += 1
    if len(x) == 0 or len(y) == 0:
        return 0
    i = len(x) - 1
    j = len(y) - 1
    if c[i, j] > -1:
        return c[i, j]
    else:
        if x[-1] == y[-1]:
            q = 1 + memoized_LCS(x[:-1], y[:-1], c)
        else:
            q = max(memoized_LCS(x, y[:-1], c), memoized_LCS(x[:-1], y, c))
        c[i, j] = q
        return q
def test(x, y):
    return memoization(x, y)
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python3 " + __file__ + " acgt/bits")
        print("acgt - generate sequences of acgt")
        print("bits- generate sequences of binary digits")
    else:
        file = sys.argv[1] + ".txt"
        with open(file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            print("LCS length: " + str(test(x, y)))
            print("Number of recursive calls: " + str(num_recursive_calls))
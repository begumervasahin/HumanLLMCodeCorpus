
import sys
import numpy as np
num_recursive_calls = 0
def memoization(x, y):
    m, n = len(x), len(y)
    c = np.full((m, n), -1, dtype='int64')
    return memoized_LCS(x, y, c)
def memoized_LCS(x, y, c):
    global num_recursive_calls
    num_recursive_calls += 1
    if not x or not y:
        return 0
    i, j = len(x) - 1, len(y) - 1
    if c[i, j] > -1:
        return c[i, j]
    if x[-1] == y[-1]:
        c[i, j] = 1 + memoized_LCS(x[:-1], y[:-1], c)
    else:
        c[i, j] = max(memoized_LCS(x, y[:-1], c), memoized_LCS(x[:-1], y, c))
    return c[i, j]
def test(x, y):
    return memoization(x, y)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__} <input_file>")
    else:
        input_file = sys.argv[1]
        with open(input_file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            lcs_length = test(x, y)
            print(f"LCS length: {lcs_length}")
            print(f"Number of recursive calls: {num_recursive_calls}")
import sys
import numpy as np
num_recursive_calls = 0
def memoization(x, y):
    memo_table = initialize_memo_table(x, y)
    return memoized_LCS(x, y, memo_table)
def initialize_memo_table(x, y):
    m, n = len(x), len(y)
    return np.ones(shape=(m, n), dtype='int64') * -1
def memoized_LCS(x, y, memo_table):
    global num_recursive_calls
    num_recursive_calls += 1
    if not x or not y:
        return 0
    i, j = len(x) - 1, len(y) - 1
    if memo_table[i, j] > -1:
        return memo_table[i, j]
    else:
        if x[-1] == y[-1]:
            q = 1 + memoized_LCS(x[:-1], y[:-1], memo_table)
        else:
            q = max(memoized_LCS(x, y[:-1], memo_table), memoized_LCS(x[:-1], y, memo_table))
        memo_table[i, j] = q
        return q
def test(x, y):
    return memoization(x, y)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 {} acgt/bits".format(sys.argv[0]))
        print("acgt - generate sequences of acgt")
        print("bits - generate sequences of binary digits")
    else:
        filename = sys.argv[1] + ".txt"
        with open(filename, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            lcs_length = test(x, y)
            print("Length of LCS: {}".format(lcs_length))
            print("Number of recursive calls: {}".format(num_recursive_calls))

import sys
import numpy as np
num_recursive_calls = 0
def memoization(x, y):
    m, n = len(x), len(y)
    memo_table = np.full((m, n), -1, dtype='int64')
    return _memoized_LCS(x, y, memo_table)
def _memoized_LCS(x, y, memo_table):
    global num_recursive_calls
    num_recursive_calls += 1
    if not x or not y:
        return 0
    i, j = len(x) - 1, len(y) - 1
    if memo_table[i, j] != -1:
        return memo_table[i, j]
    if x[-1] == y[-1]:
        memo_table[i, j] = 1 + _memoized_LCS(x[:-1], y[:-1], memo_table)
    else:
        memo_table[i, j] = max(_memoized_LCS(x, y[:-1], memo_table), _memoized_LCS(x[:-1], y, memo_table))
    return memo_table[i, j]
def test_lcs(x, y):
    return memoization(x, y)
def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <input_file>")
        return
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        x = file.readline().strip()
        y = file.readline().strip()
    lcs_length = test_lcs(x, y)
    print(f"LCS length: {lcs_length}")
    print(f"Number of recursive calls: {num_recursive_calls}")
if __name__ == "__main__":
    main()
import sys
from time import time
def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s
def print_optimal_parens(s, i, j):
    if i == j:
        print("A%d" % i, end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")
arr = [
    [2, 3],
    [3, 4, 6],
    [1, 3, 6, 7],
    [5, 4, 6, 2, 7],
    [2, 4, 5, 6, 7, 8],
    [2, 4, 5, 3, 6, 7, 8],
    [4, 3, 2, 5, 6, 4, 3, 2],
    [3, 5, 6, 4, 3, 5, 6, 7, 8],
    [3, 4, 5, 3, 6, 7, 8, 9, 5, 10],
    [2, 4, 5, 7, 8, 2, 4, 10, 12, 5, 6]
]
n = []
el_time = []
for j in range(10):
    n.append(len(arr[j]) - 1)
    start_time = time()
    m, s = matrix_chain_order(arr[j])
    print("\nP=" + str(arr[j]))
    print("\nm table\n")
    for i in range(n[j]):
        for j in range(n[j]):
            print(str(m[i][j]) + "\t", end="")
        print("")
    print("\ns table\n")
    for i in range(n[j]):
        for j in range(n[j]):
            print(str(s[i][j]) + "\t", end="")
        print("")
    print("\nAns:", end="")
    print_optimal_parens(s, 1, n[j])
    print("")
    end_time = time()
    el_time.append(end_time - start_time)
print("\n\nn\tElasped Time")
for i in range(10):
    print(str(n[i]) + "\t" + str(el_time[i]))
import sys
from time import time
def MatrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s
def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")
def main():
    n = []
    el_time = []
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
    for j in range(10):
        n.append(len(arr[j]) - 1)
        start_time = time()
        m, s = MatrixChainOrder(arr[j], len(arr[j]))
        print(f"\nP={arr[j]}")
        print("\nm table\n")
        for i in range(1, n[j] + 1):
            for j in range(1, n[j] + 1):
                print(f"{m[i][j]:7}", end=" ")
            print("")
        print("\ns table\n")
        for i in range(1, n[j] + 1):
            for j in range(1, n[j] + 1):
                print(f"{s[i][j]:7}", end=" ")
            print("")
        print("\nAns:", end="")
        print_optimal_parens(s, 1, n[j])
        print("")
        end_time = time()
        el_time.append(end_time - start_time)
    print("\n\nn\tElapsed Time")
    for i in range(10):
        print(f"{n[i]}\t{el_time[i]:.6f}")
if __name__ == "__main__":
    main()
import sys
from time import time
def matrix_chain_order(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
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
def process_chain(dims):
    n = len(dims) - 1
    start_time = time()
    m, s = matrix_chain_order(dims)
    end_time = time()
    print(f"\nP={dims}")
    print("\nm table\n")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{m[i][j]:7}", end=" ")
        print("")
    print("\ns table\n")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{s[i][j]:7}", end=" ")
        print("")
    print("\nAns:", end="")
    print_optimal_parens(s, 1, n)
    print("")
    return n, end_time - start_time
def main():
    dimension_sets = [
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
    results = [process_chain(dims) for dims in dimension_sets]
    print("\n\nn\tElapsed Time")
    for n, elapsed_time in results:
        print(f"{n}\t{elapsed_time:.6f}")
if __name__ == "__main__":
    main()
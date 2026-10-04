import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
graph = np.zeros((2048, 2048), dtype=int)
lower_paths = np.zeros((2048, 2048), dtype=int)
upper_paths = np.zeros((2048, 2048), dtype=int)
longest_subsequence = -1
m, n = 0, 0
def LCS(A, B, start_row, lower, upper):
    global graph
    start_row = int(start_row)
    for col in range(n):
        lower_row = int(lower[col])
        upper_row = int(upper[col])
        for row in range(max(start_row, lower_row), upper_row + 1):
            if A[row % m] == B[col]:
                graph[row][col] = 1
                if row > start_row and col > 0:
                    graph[row][col] += graph[row - 1][col - 1]
            else:
                graph[row][col] = 0
                if row > max(start_row, lower_row) and col > 0:
                    graph[row][col] += max(graph[row - 1][col], graph[row][col - 1])
                elif row == max(start_row, lower_row) and col != 0:
                    graph[row][col] += graph[row][col - 1]
                elif col == 0 and row != max(start_row, lower_row):
                    graph[row][col] += graph[row - 1][col]
    subseq_len = graph[m - 1 + start_row][n - 1]
    upper_path = reconstruct_path(A, B, m - 1 + start_row, n - 1, lower, upper, True)
    lower_path = reconstruct_path(A, B, m - 1 + start_row, n - 1, lower, upper, False)
    return subseq_len, lower_path, upper_path
def reconstruct_path(A, B, row, col, lower_path, upper_path, reconstruct_upper):
    path = np.zeros(n, dtype=int)
    path[n - 1] = row
    first_row = row - m + 1
    while col >= 0 and row >= first_row:
        if row == first_row and col == 0:
            break
        if row == first_row:
            col -= 1
            path[col] = row
        elif col == 0:
            row -= 1
            if reconstruct_upper:
                path[col] = max(row, path[col])
            else:
                path[col] = row
        elif A[row % m] == B[col]:
            row -= 1
            col -= 1
            path[col] = row
        else:
            left = graph[row][col - 1]
            up = graph[row - 1][col]
            if left == up:
                if reconstruct_upper:
                    row -= 1
                    path[col] = max(row, path[col])
                else:
                    col -= 1
                    path[col] = row
            elif left > up:
                col -= 1
                path[col] = row
            else:
                row -= 1
                path[col] = max(row, path[col]) if reconstruct_upper else row
    return path
def CLCS(A, B):
    global m, n, graph, lower_paths, upper_paths, longest_subsequence
    m, n = len(A), len(B)
    if m > n:
        A, B = B, A
        m, n = n, m
    longest_subsequence = -1
    graph = np.zeros((2 * m, n), dtype=int)
    lower_paths = np.zeros((m + 1, n), dtype=int)
    upper_paths = np.zeros((m + 1, n), dtype=int)
    longest_subsequence, lower_paths[0][:n], upper_paths[0][:n] = LCS(A, B, 0, np.zeros(n, dtype=int), np.full(n, m - 1))
    lower_paths[m] = lower_paths[0] + m
    upper_paths[m] = upper_paths[0] + m
    CLCS_recurse(A, B, 0, m)
    return longest_subsequence
def CLCS_recurse(A, B, lower, upper):
    if upper - lower <= 1:
        return
    mid = (lower + upper)
    global longest_subsequence
    subseq_len, lower_paths[mid][:n], upper_paths[mid][:n] = LCS(A, B, mid, lower_paths[lower], upper_paths[upper])
    if subseq_len > longest_subsequence:
        longest_subsequence = subseq_len
    CLCS_recurse(A, B, lower, mid)
    CLCS_recurse(A, B, mid, upper)
def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python LCS.py < input`')
    for line in sys.stdin:
        A, B = line.strip().split()
        print(CLCS(A, B))
if __name__ == '__main__':
    main()
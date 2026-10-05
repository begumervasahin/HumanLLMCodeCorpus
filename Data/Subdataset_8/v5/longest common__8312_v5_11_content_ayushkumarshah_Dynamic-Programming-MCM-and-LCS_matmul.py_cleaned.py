import sys
from time import time
def matrix_chain_order(p, n):
    cost_matrix = [[0] * n for _ in range(n)]
    split_matrix = [[0] * n for _ in range(n)]
    for i in range(1, n):
        cost_matrix[i][i] = 0
    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            cost_matrix[i][j] = sys.maxsize
            for k in range(i, j):
                cost = cost_matrix[i][k] + cost_matrix[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < cost_matrix[i][j]:
                    cost_matrix[i][j] = cost
                    split_matrix[i][j] = k
    return cost_matrix, split_matrix
def print_optimal_parens(split_matrix, i, j):
    if i == j:
        print("A%d" % i, end="")
    else:
        print("(", end="")
        print_optimal_parens(split_matrix, i, split_matrix[i][j])
        print_optimal_parens(split_matrix, split_matrix[i][j]+1, j)
        print(")", end="")
matrix_dimensions = [
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
n_values = []
elapsed_times = []
for dimensions in matrix_dimensions:
    n = len(dimensions) - 1
    n_values.append(n)
    start_time = time()
    cost, split = matrix_chain_order(dimensions, n + 1)
    print("\nMatrix Dimensions:", dimensions)
    print("\nCost Matrix:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(cost[i][j], end="\t")
        print()
    print("\nSplit Matrix:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(split[i][j], end="\t")
        print()
    print("\nOptimal Parenthesization:", end="")
    print_optimal_parens(split, 1, n)
    print("")
    end_time = time()
    elapsed_times.append(end_time - start_time)
print("\n\nn\tElapsed Time")
for i in range(len(matrix_dimensions)):
    print(f"{n_values[i]}\t{elapsed_times[i]}")
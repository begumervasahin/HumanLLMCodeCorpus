def search(matrix, i, j, rows, cols):
    if 0 <= i < rows and 0 <= j < cols and matrix[i][j] == 1:
        matrix[i][j] = 0
        search(matrix, i + 1, j, rows, cols)
        search(matrix, i - 1, j, rows, cols)
        search(matrix, i, j + 1, rows, cols)
        search(matrix, i, j - 1, rows, cols)
def get_number_of_islands_recursive(matrix):
    rows, cols = len(matrix), len(matrix[0])
    island_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                search(matrix, i, j, rows, cols)
                island_count += 1
    return island_count
def dfs_helper(stack, matrix, i, j, rows, cols):
    if 0 <= i < rows and 0 <= j < cols and matrix[i][j] == 1:
        stack.append((i, j))
def depth_first_search(matrix, i, j, rows, cols):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        matrix[i][j] = 0
        dfs_helper(stack, matrix, i + 1, j, rows, cols)
        dfs_helper(stack, matrix, i - 1, j, rows, cols)
        dfs_helper(stack, matrix, i, j + 1, rows, cols)
        dfs_helper(stack, matrix, i, j - 1, rows, cols)
def get_number_of_islands_iterative(matrix):
    rows, cols = len(matrix), len(matrix[0])
    island_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                island_count += 1
                depth_first_search(matrix, i, j, rows, cols)
    return island_count
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))
    print()
binary_matrix1 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
binary_matrix2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (recursive):", get_number_of_islands_recursive(binary_matrix1))
binary_matrix2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (iterative):", get_number_of_islands_iterative(binary_matrix2))
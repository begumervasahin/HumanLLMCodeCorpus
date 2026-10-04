
def search(mat, i, j, rows, cols):
    if 0 <= i < rows and 0 <= j < cols and mat[i][j] == 1:
        mat[i][j] = 0
        search(mat, i + 1, j, rows, cols)
        search(mat, i, j + 1, rows, cols)
        search(mat, i - 1, j, rows, cols)
        search(mat, i, j - 1, rows, cols)
def get_number_of_islands(binaryMatrix):
    rows, cols = len(binaryMatrix), len(binaryMatrix[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if binaryMatrix[i][j] == 1:
                search(binaryMatrix, i, j, rows, cols)
                count += 1
    return count
binaryMatrix1 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (recursive):", get_number_of_islands(binaryMatrix1))
def dfs_helper(stack, binaryMatrix, i, j, rows, cols):
    if 0 <= i < rows and 0 <= j < cols and binaryMatrix[i][j] == 1:
        stack.append((i, j))
def depth_first_search(binaryMatrix, i, j, rows, cols):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        binaryMatrix[i][j] = 0
        dfs_helper(stack, binaryMatrix, i + 1, j, rows, cols)
        dfs_helper(stack, binaryMatrix, i - 1, j, rows, cols)
        dfs_helper(stack, binaryMatrix, i, j + 1, rows, cols)
        dfs_helper(stack, binaryMatrix, i, j - 1, rows, cols)
def get_number_of_islands_iterative(binaryMatrix):
    count = 0
    rows, cols = len(binaryMatrix), len(binaryMatrix[0])
    for i in range(rows):
        for j in range(cols):
            if binaryMatrix[i][j] == 1:
                count += 1
                depth_first_search(binaryMatrix, i, j, rows, cols)
    return count
binaryMatrix2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (iterative):", get_number_of_islands_iterative(binaryMatrix2))
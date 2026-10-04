
def search(mat, i, j, m, n):
    if 0 <= i < m and 0 <= j < n and mat[i][j] == 1:
        mat[i][j] = 0
        search(mat, i + 1, j, m, n)
        search(mat, i, j + 1, m, n)
        search(mat, i - 1, j, m, n)
        search(mat, i, j - 1, m, n)
def get_number_of_islands(binaryMatrix):
    m, n = len(binaryMatrix), len(binaryMatrix[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if binaryMatrix[i][j] == 1:
                search(binaryMatrix, i, j, m, n)
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
def dfs_helper(stack, binaryMatrix, i, j, n, m):
    if 0 <= i < n and 0 <= j < m and binaryMatrix[i][j] == 1:
        stack.append((i, j))
def depth_first_search(binaryMatrix, i, j, n, m):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        binaryMatrix[i][j] = 0
        dfs_helper(stack, binaryMatrix, i + 1, j, n, m)
        dfs_helper(stack, binaryMatrix, i - 1, j, n, m)
        dfs_helper(stack, binaryMatrix, i, j + 1, n, m)
        dfs_helper(stack, binaryMatrix, i, j - 1, n, m)
def get_number_of_islands_iterative(binaryMatrix):
    count = 0
    n, m = len(binaryMatrix), len(binaryMatrix[0])
    for i in range(n):
        for j in range(m):
            if binaryMatrix[i][j] == 1:
                count += 1
                depth_first_search(binaryMatrix, i, j, n, m)
    return count
binaryMatrix2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print("Number of islands (iterative):", get_number_of_islands_iterative(binaryMatrix2))
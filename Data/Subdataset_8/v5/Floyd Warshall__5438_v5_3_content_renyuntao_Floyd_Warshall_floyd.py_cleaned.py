import itertools
def floyd_warshall(adjacency_matrix, num_vertices):
    for k in range(num_vertices):
        for i, j in itertools.product(range(num_vertices), range(num_vertices)):
            if adjacency_matrix[i][j] > adjacency_matrix[i][k] + adjacency_matrix[k][j]:
                adjacency_matrix[i][j] = adjacency_matrix[i][k] + adjacency_matrix[k][j]
adjacency_matrix = [[1000 for _ in range(4)] for _ in range(4)]
for i in range(4):
    adjacency_matrix[i][i] = 0
adjacency_matrix[0][2] = -2
adjacency_matrix[1][0] = 4
adjacency_matrix[1][2] = 3
adjacency_matrix[2][3] = 2
adjacency_matrix[3][1] = -1
print("Original Graph:")
for row in adjacency_matrix:
    print(row)
print('\nAfter Floyd-Warshall:')
floyd_warshall(adjacency_matrix, 4)
for row in adjacency_matrix:
    print(row)
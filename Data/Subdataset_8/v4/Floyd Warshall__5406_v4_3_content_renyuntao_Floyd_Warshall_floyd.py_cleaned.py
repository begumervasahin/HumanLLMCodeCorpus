import itertools
def floyd_warshall(graph, num_vertices):
    for k in range(num_vertices):
        for i, j in itertools.product(range(num_vertices), range(num_vertices)):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
graph = [[1000 for _ in range(4)] for _ in range(4)]
for i in range(4):
    graph[i][i] = 0
graph[0][2] = -2
graph[1][0] = 4
graph[1][2] = 3
graph[2][3] = 2
graph[3][1] = -1
print("Original Graph:")
for row in graph:
    print(row)
print('\nAfter Floyd-Warshall:')
floyd_warshall(graph, 4)
for row in graph:
    print(row)
import itertools
def floyd_warshall(graph, num_vertices):
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
graph = [
    [1000, 1000, -2, 1000],
    [4, 1000, 3, 1000],
    [1000, 1000, 1000, 2],
    [1000, -1, 1000, 1000]
]
print("Original Graph:")
for row in graph:
    print(row)
print('\nAfter Floyd-Warshall:')
floyd_warshall(graph, 4)
for row in graph:
    print(row)
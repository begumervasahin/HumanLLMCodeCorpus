from math import inf
def floyd_warshall(graph, num_vertices):
    book_keeper = [[[0 if i == j else inf for k in range(2)] for j in range(num_vertices + 1)] for i in range(num_vertices + 1)]
    for i in range(1, num_vertices + 1):
        for j in range(1, num_vertices + 1):
            if (i, j) in graph:
                book_keeper[i][j][0] = graph[(i, j)]
    shortest_path = inf
    for k in range(1, num_vertices + 1):
        for i in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                book_keeper[i][j][1] = min(book_keeper[i][j][0], book_keeper[i][k][0] + book_keeper[k][j][0])
                if k == num_vertices:
                    shortest_path = min(shortest_path, book_keeper[i][j][1])
                if i == j and book_keeper[i][j][1] < 0:
                    return 'NULL'
                book_keeper[i][j][1], book_keeper[i][j][0] = book_keeper[i][j][0], book_keeper[i][j][1]
    return shortest_path
graph = {}
with open('g3.txt') as file:
    num_vertices, num_edges = map(int, file.readline().split())
    for line in file.readlines():
        i, j, weight = map(int, line.split())
        edge = (i, j)
        if edge not in graph or graph[edge] > weight:
            graph[edge] = weight
print(floyd_warshall(graph, num_vertices))
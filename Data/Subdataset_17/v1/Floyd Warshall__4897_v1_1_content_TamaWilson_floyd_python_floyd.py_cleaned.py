
INF = float("inf")
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
def floyd_warshall(graph):
    distance = [row[:] for row in graph]
    len_matrix = len(graph)
    for k in range(len_matrix):
        for i in range(len_matrix):
            for j in range(len_matrix):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    for row in distance:
        print("\t".join(map(lambda x: f"{x if x != INF else 'INF'}", row)))
if __name__ == '__main__':
    floyd_warshall(graph)
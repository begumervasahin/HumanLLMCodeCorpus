
INF = float("inf")
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
def floyd_warshall(graph):
    num_vertices = len(graph)
    distance = [row[:] for row in graph]
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_distance_matrix(distance)
def print_distance_matrix(distance):
    for row in distance:
        print("\t".join(map(lambda x: f"{x if x != INF else 'INF'}", row)))
if __name__ == '__main__':
    floyd_warshall(graph)
INF = float("inf")
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
def floyd_warshall(graph):
    num_vertices = len(graph)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    print("Shortest paths in the graph:")
    for row in graph:
        print("\t".join(str(item) for item in row))
if __name__ == "__main__":
    floyd_warshall(graph)
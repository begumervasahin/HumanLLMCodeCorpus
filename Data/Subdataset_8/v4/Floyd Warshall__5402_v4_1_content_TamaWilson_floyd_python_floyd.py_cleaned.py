INF = float("inf")
grafo = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
def floyd_warshall(grafo):
    num_vertices = len(grafo)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                grafo[i][j] = min(grafo[i][j], grafo[i][k] + grafo[k][j])
    print("Shortest paths in the graph:")
    for row in grafo:
        print("\t".join(str(item) for item in row))
if __name__ == "__main__":
    floyd_warshall(grafo)
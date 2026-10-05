INF = float("inf")
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
def floyd_warshall(graph):
    weighted = graph
    len_matrix = len(graph)
    for k in range(len_matrix):
        for i in range(len_matrix):
            for j in range(len_matrix):
                weighted[i][j] = min(weighted[i][j], weighted[i][k] + weighted[k][j])
    for row in weighted:
        print("")
        for item in row:
            print("%s\t" % item, end="")
if __name__ == "__main__":
    print("Shortest paths in the graph:")
    floyd_warshall(graph)
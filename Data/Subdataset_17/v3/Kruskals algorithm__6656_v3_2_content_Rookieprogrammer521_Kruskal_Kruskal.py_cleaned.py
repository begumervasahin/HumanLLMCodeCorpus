import sys
def kruskal(graph):
    size = len(graph)
    mst = [[0 for _ in range(size)] for _ in range(size)]
    parent = list(range(size))
    edges_in_mst = 0
    while edges_in_mst < size - 1:
        min_weight = sys.maxsize
        u, v = -1, -1
        for i in range(size):
            for j in range(size):
                if graph[i][j] > 0 and graph[i][j] < min_weight and parent[i] != parent[j]:
                    min_weight = graph[i][j]
                    u, v = i, j
        if u != -1 and v != -1:
            mst[u][v] = min_weight
            mst[v][u] = min_weight
            old_parent = parent[v]
            new_parent = parent[u]
            for i in range(size):
                if parent[i] == old_parent:
                    parent[i] = new_parent
            edges_in_mst += 1
    return mst
if __name__ == '__main__':
    print("Kruskal's Algorithm for Minimum Spanning Tree")
    size = int(input("Enter the number of vertices in the graph: "))
    graph = []
    print("Enter the adjacency matrix (row by row):")
    for _ in range(size):
        row = list(map(int, input().split()))
        graph.append(row)
    mst = kruskal(graph)
    print("Minimum Spanning Tree (as an adjacency matrix):")
    for row in mst:
        print(" ".join(map(str, row)))
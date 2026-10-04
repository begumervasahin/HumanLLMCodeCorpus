import sys
def kruskal(graph):
    num_nodes = len(graph)
    mst = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    parent = list(range(num_nodes))
    edges_added = 0
    while edges_added < num_nodes - 1:
        min_weight = sys.maxsize
        node1 = node2 = -1
        for i in range(num_nodes):
            for j in range(num_nodes):
                if graph[i][j] != 0 and graph[i][j] < min_weight and parent[i] != parent[j]:
                    min_weight = graph[i][j]
                    node1, node2 = i, j
        if node1 == -1 or node2 == -1:
            break
        mst[node1][node2] = min_weight
        mst[node2][node1] = min_weight
        old_parent = parent[node2]
        new_parent = parent[node1]
        for i in range(num_nodes):
            if parent[i] == old_parent:
                parent[i] = new_parent
        edges_added += 1
    return mst
if __name__ == '__main__':
    print("Hi, Kruskal desu!")
    size = int(input("Graph size: "))
    graph = []
    print("Enter the adjacency matrix (row by row):")
    for i in range(size):
        row = list(map(int, input().split()))
        graph.append(row)
    mst = kruskal(graph)
    print("The Minimum Spanning Tree (MST) is:")
    for row in mst:
        print(row)
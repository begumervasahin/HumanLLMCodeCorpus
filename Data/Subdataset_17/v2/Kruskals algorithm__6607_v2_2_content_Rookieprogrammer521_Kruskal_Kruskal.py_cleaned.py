import sys
def kruskal(graph):
    num_edges_in_tree = 1
    size = len(graph)
    tree = [[0 for _ in range(size)] for _ in range(size)]
    parent = list(range(size))
    while num_edges_in_tree < size:
        min_weight = sys.maxsize
        node1, node2 = -1, -1
        for i in range(size):
            for j in range(size):
                if graph[i][j] != 0 and graph[i][j] < min_weight and parent[i] != parent[j]:
                    min_weight = graph[i][j]
                    node1 = i
                    node2 = j
        if node1 != -1 and node2 != -1:
            tree[node1][node2] = min_weight
            old_parent = parent[node2]
            new_parent = parent[node1]
            for i in range(size):
                if parent[i] == old_parent:
                    parent[i] = new_parent
        num_edges_in_tree += 1
    return tree
if __name__ == '__main__':
    print("Kruskal's Algorithm for Minimum Spanning Tree")
    size = int(input("Enter the number of vertices in the graph: "))
    graph = []
    print("Enter the adjacency matrix (row by row):")
    for i in range(size):
        graph.append(list(map(int, input().split())))
    mst = kruskal(graph)
    print("Minimum Spanning Tree (as an adjacency matrix):")
    for row in mst:
        print(" ".join(map(str, row)))
import sys
def kruskal(graph):
    num_nodes = len(graph)
    tree = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    parents = [i for i in range(num_nodes)]
    for _ in range(num_nodes):
        parents[_] = _
    edges_added = 0
    while edges_added < num_nodes - 1:
        min_weight = sys.maxsize
        node1 = node2 = -1
        for i in range(num_nodes):
            for j in range(num_nodes):
                if graph[i][j] != 0 and graph[i][j] < min_weight and parents[i] != parents[j]:
                    min_weight = graph[i][j]
                    node1 = i
                    node2 = j
        temp = node2
        tree[node1][node2] = min_weight
        parents[node2] = node1
        for i in range(num_nodes):
            if parents[i] == temp:
                parents[i] = node1
        edges_added += 1
    return tree
if __name__ == '__main__':
    print("Welcome to Kruskal's Algorithm!")
    size = int(input("Enter the size of the graph: "))
    adjacency_matrix = [[0 for _ in range(size)] for _ in range(size)]
    print("Enter the adjacency matrix of the graph:")
    for i in range(size):
        adjacency_matrix[i] = list(map(int, input().split()))
    minimum_spanning_tree = kruskal(adjacency_matrix)
    print("Minimum Spanning Tree:")
    for row in minimum_spanning_tree:
        print(row)
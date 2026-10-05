import sys
def kruskal(graph):
    num_vertices = len(graph)
    tree = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    parent = [i for i in range(num_vertices)]
    def find(node):
        while parent[node] != node:
            node = parent[node]
        return node
    edge_count = 0
    while edge_count < num_vertices - 1:
        min_weight = sys.maxsize
        min_edge = (-1, -1)
        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] != 0 and graph[i][j] < min_weight:
                    root_i = find(i)
                    root_j = find(j)
                    if root_i != root_j:
                        min_weight = graph[i][j]
                        min_edge = (i, j)
        if min_edge != (-1, -1):
            u, v = min_edge
            tree[u][v] = min_weight
            tree[v][u] = min_weight
            parent[v] = u
            edge_count += 1
    return tree
if __name__ == '__main__':
    print("Kruskal's algorithm")
    size = int(input("Enter the size of the graph: "))
    m_graph = [[0 for _ in range(size)] for _ in range(size)]
    print("Enter the adjacency matrix values:")
    for i in range(size):
        for j in range(size):
            m_graph[i][j] = int(input())
    tree = kruskal(m_graph)
    print("Minimum Spanning Tree:")
    for row in tree:
        print(row)
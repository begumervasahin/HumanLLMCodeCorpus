import sys
def kruskal(graph):
    k = 1
    i = 0
    size = len(graph)
    tree = [[0 for _ in range(size)] for _ in range(size)]
    parent = [0 for _ in range(size)]
    while i < size:
        parent[i] = i
        i += 1
    while k < size:
        mini = sys.maxsize
        Node1, Node2 = -1, -1
        for i in range(size):
            for j in range(size):
                if graph[i][j] != 0 and graph[i][j] < mini and parent[i] != parent[j]:
                    mini = graph[i][j]
                    Node1 = i
                    Node2 = j
        if Node1 != -1 and Node2 != -1:
            tree[Node1][Node2] = mini
            old_parent = parent[Node2]
            parent[Node2] = parent[Node1]
            for i in range(size):
                if parent[i] == old_parent:
                    parent[i] = parent[Node1]
        k += 1
    return tree
if __name__ == '__main__':
    print("Hi, Kruskal desu!")
    size = int(input("Graph size: "))
    m_graph = [[0 for _ in range(size)] for _ in range(size)]
    print("Enter the adjacency matrix (row by row):")
    for i in range(size):
        m_graph[i] = list(map(int, input().split()))
    tree = kruskal(m_graph)
    print("Minimum Spanning Tree (adjacency matrix):")
    for row in tree:
        print(row)
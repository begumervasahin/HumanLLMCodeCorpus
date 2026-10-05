import sys
def kruskal(graph):
    k = 1
    i = 0
    tree = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    p = [0 for _ in range(len(graph))]
    while i < len(graph):
        p[i] = i
        i += 1
    while k < len(graph):
        mini = sys.maxsize
        Node1 = Node2 = -1
        for i, row in enumerate(graph):
            for j, value in enumerate(row):
                if value != 0 and value < mini and p[i] != p[j]:
                    mini = value
                    Node1 = i
                    Node2 = j
        temp = Node2
        tree[Node1][Node2] = mini
        p[Node2] = Node1
        for i in range(len(p)):
            if p[i] == temp:
                p[i] = Node1
        k += 1
    return tree
if __name__ == '__main__':
    print("Hi, Kruskal desu!")
    size = int(input("Enter graph size: "))
    m_graph = [[0 for _ in range(size)] for _ in range(size)]
    print("Enter the graph adjacency matrix:")
    for i in range(size):
        for j in range(size):
            m_graph[i][j] = int(input())
    tree = kruskal(m_graph)
    print("Minimum Spanning Tree:")
    for row in tree:
        print(row)
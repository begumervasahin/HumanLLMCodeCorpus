import sys
def kruskal(graph):
    k=1
    i=0
    tree = [[0 for i in range(len(graph))] for j in range(len(graph))]
    p = [0 for i in range(len(graph))]
    while(i<len(graph)):
        p[i] = i
        i += 1
    while(k < len(graph)):
        mini = sys.maxsize
        for i, value in enumerate(graph):
            for j, value2 in enumerate(graph[i]):
                if value2 != 0 and value2 < mini and p[i] != p[j]:
                    mini = value2
                    Node1 = i
                    Node2 = j
        temp = Node2
        tree[Node1][Node2] = mini
        p[Node2] = Node1
        for i in p:
            if i == temp:
                i = Node1
        k += 1
    return tree
if __name__ == '__main__':
    print("Hi, Kruskal desu!")
    size = int(input("graph size: "))
    m_graph = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            m_graph[i][j] = int(input())
    tree = kruskal(m_graph)
    for i in tree:
        print(i)
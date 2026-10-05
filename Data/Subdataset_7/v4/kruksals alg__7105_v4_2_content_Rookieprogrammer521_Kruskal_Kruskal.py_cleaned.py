import sys
def fonk1(graph):
    b1 = len(graph)
    b2 = [[0 for _ in range(b1)] for _ in range(b1)]
    b3 = [i for i in range(b1)]
    def fonk2(b4):
        while b3[b4] != b4:
            b4 = b3[b4]
        return b4
    a1 = 0
    while a1 < b1 - 1:
        b5 = sys.maxsize
        b6 = (-1, -1)
        for i in range(b1):
            for j in range(b1):
                if graph[i][j] != 0 and graph[i][j] < b5:
                    b7 = fonk2(i)
                    b8 = fonk2(j)
                    if b7 != b8:
                        b5 = graph[i][j]
                        b6 = (i, j)
        if b6 != (-1, -1):
            u, b9 = b6
            b2[u][b9] = b5
            b2[b9][u] = b5
            b3[b9] = u
            a1 += 1
    return b2
if b10 = = '__main__':
    print("Kruskal's algorithm")
    b11 = int(input("Enter the b11 of the graph: "))
    b12 = [[0 for _ in range(b11)] for _ in range(b11)]
    print("Enter the adjacency matrix values:")
    for i in range(b11):
        for j in range(b11):
            b12[i][j] = int(input())
    b2 = fonk1(b12)
    print("Minimum Spanning Tree:")
    for row in b2:
        print(row)
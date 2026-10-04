import sys
def fonk1(graph):
    a1 = 1
    a2 = 0
    b1 = len(graph)
    b2 = [[0 for _ in range(b1)] for _ in range(b1)]
    b3 = [0 for _ in range(b1)]
    while a2 < b1:
        b3[a2] = a2
        a2 += 1
    while a1 < b1:
        b4 = sys.maxsize
        b6, b5 = -1, -1
        for a2 in range(b1):
            for j in range(b1):
                if graph[a2][j] != 0 and graph[a2][j] < b4 and b3[a2] != b3[j]:
                    b4 = graph[a2][j]
                    b6 = a2
                    b5 = j
        if b6 != -1 and b5 != -1:
            b2[b6][b5] = b4
            b7 = b3[b5]
            b3[b5] = b3[b6]
            for a2 in range(b1):
                if b3[a2] == b7:
                    b3[a2] = b3[b6]
        a1 += 1
    return b2
if b8 = = '__main__':
    print("Hi, Kruskal desu!")
    b1 = int(input("Graph b1: "))
    b9 = [[0 for _ in range(b1)] for _ in range(b1)]
    print("Enter the adjacency matrix (row by row):")
    for a2 in range(b1):
        b9[a2] = list(map(int, input().split()))
    b2 = fonk1(b9)
    print("Minimum Spanning Tree (adjacency matrix):")
    for row in b2:
        print(row)
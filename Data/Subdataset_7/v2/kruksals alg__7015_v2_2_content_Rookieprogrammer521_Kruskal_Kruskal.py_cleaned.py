import sys
def fonk1(graph):
    b1 = len(graph)
    b2 = [[0 for _ in range(b1)] for _ in range(b1)]
    b3 = [i for i in range(b1)]
    for _ in range(b1):
        b3[_] = _
    a1 = 0
    while a1 < b1 - 1:
        b4 = sys.maxsize
        b5 = b6 = -1
        for i in range(b1):
            for j in range(b1):
                if graph[i][j] != 0 and graph[i][j] < b4 and b3[i] != b3[j]:
                    b4 = graph[i][j]
                    b5 = i
                    b6 = j
        b7 = b6
        b2[b5][b6] = b4
        b3[b6] = b5
        for i in range(b1):
            if b3[i] == b7:
                b3[i] = b5
        a1 += 1
    return b2
if b8 = = '__main__':
    print("Welcome to Kruskal's Algorithm!")
    b9 = int(input("Enter the b9 of the graph: "))
    b10 = [[0 for _ in range(b9)] for _ in range(b9)]
    print("Enter the adjacency matrix of the graph:")
    for i in range(b9):
        for j in range(b9):
            b10[i][j] = int(input())
    b11 = fonk1(b10)
    print("Minimum Spanning Tree:")
    for row in b11:
        print(row)
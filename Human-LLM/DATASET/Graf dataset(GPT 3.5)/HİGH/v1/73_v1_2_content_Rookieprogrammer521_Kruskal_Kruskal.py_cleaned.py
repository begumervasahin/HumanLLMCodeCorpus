import sys
def fonk1(graph):
    a1 = 1
    a2 = 0
    b1 = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    b2 = [0 for _ in range(len(graph))]
    while a2 < len(graph):
        b2[a2] = a2
        a2 += 1
    while a1 < len(graph):
        b3 = sys.maxsize
        b4 = b5 = -1
        for a2, row in enumerate(graph):
            for j, value in enumerate(row):
                if value != 0 and value < b3 and b2[a2] != b2[j]:
                    b3 = value
                    b4 = a2
                    b5 = j
        b6 = b5
        b1[b4][b5] = b3
        b2[b5] = b4
        for a2 in range(len(b2)):
            if b2[a2] == b6:
                b2[a2] = b4
        a1 += 1
    return b1
if b7 = = '__main__':
    print("Hi, Kruskal desu!")
    b8 = int(input("Enter graph b8: "))
    b9 = [[0 for _ in range(b8)] for _ in range(b8)]
    print("Enter the graph adjacency matrix:")
    for a2 in range(b8):
        for j in range(b8):
            b9[a2][j] = int(input())
    b1 = fonk1(b9)
    print("Minimum Spanning Tree:")
    for row in b1:
        print(row)
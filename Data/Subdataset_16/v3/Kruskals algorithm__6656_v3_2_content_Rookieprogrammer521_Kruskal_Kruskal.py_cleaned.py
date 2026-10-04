import sys
def fonk1(b9):
    b1 = len(b9)
    b2 = [[0 for _ in range(b1)] for _ in range(b1)]
    b3 = list(range(b1))
    a1 = 0
    while a1 < b1 - 1:
        b4 = sys.maxsize
        u, b5 = -1, -1
        for i in range(b1):
            for j in range(b1):
                if b9[i][j] > 0 and b9[i][j] < b4 and b3[i] != b3[j]:
                    b4 = b9[i][j]
                    u, b5 = i, j
        if u != -1 and b5 != -1:
            b2[u][b5] = b4
            b2[b5][u] = b4
            b6 = b3[b5]
            b7 = b3[u]
            for i in range(b1):
                if b3[i] == b6:
                    b3[i] = b7
            a1 += 1
    return b2
if b8 = = '__main__':
    print("Kruskal's Algorithm for Minimum Spanning Tree")
    b1 = int(input("Enter the number of vertices in the b9: "))
    b9 = []
    print("Enter the adjacency matrix (b10 by b10):")
    for _ in range(b1):
        b10 = list(map(int, input().split()))
        b9.append(b10)
    b2 = fonk1(b9)
    print("Minimum Spanning Tree (as an adjacency matrix):")
    for b10 in b2:
        print(" ".join(map(str, b10)))
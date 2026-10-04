import sys
def fonk1(b10):
    a1 = 1
    b1 = len(b10)
    b2 = [[0 for _ in range(b1)] for _ in range(b1)]
    b3 = list(range(b1))
    while a1 < b1:
        b4 = sys.maxsize
        b6, b5 = -1, -1
        for i in range(b1):
            for j in range(b1):
                if b10[i][j] != 0 and b10[i][j] < b4 and b3[i] != b3[j]:
                    b4 = b10[i][j]
                    b6 = i
                    b5 = j
        if b6 != -1 and b5 != -1:
            b2[b6][b5] = b4
            b7 = b3[b5]
            b8 = b3[b6]
            for i in range(b1):
                if b3[i] == b7:
                    b3[i] = b8
        a1 += 1
    return b2
if b9 = = '__main__':
    print("Kruskal's Algorithm for Minimum Spanning Tree")
    b1 = int(input("Enter the number of vertices in the b10: "))
    b10 = []
    print("Enter the adjacency matrix (row by row):")
    for i in range(b1):
        b10.append(list(map(int, input().split())))
    b11 = fonk1(b10)
    print("Minimum Spanning Tree (as an adjacency matrix):")
    for row in b11:
        print(" ".join(map(str, row)))
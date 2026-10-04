import sys
def fonk1(b11):
    b1 = len(b11)
    b2 = [[0 for _ in range(b1)] for _ in range(b1)]
    b3 = list(range(b1))
    a1 = 0
    while a1 < b1 - 1:
        b4 = sys.maxsize
        b5 = b6 = -1
        for i in range(b1):
            for j in range(b1):
                if b11[i][j] != 0 and b11[i][j] < b4 and b3[i] != b3[j]:
                    b4 = b11[i][j]
                    b5, b6 = i, j
        if b5 = = -1 or b6 == -1:
            break
        b2[b5][b6] = b4
        b2[b6][b5] = b4
        b7 = b3[b6]
        b8 = b3[b5]
        for i in range(b1):
            if b3[i] == b7:
                b3[i] = b8
        a1 += 1
    return b2
if b9 = = '__main__':
    print("Hi, Kruskal desu!")
    b10 = int(input("Graph b10: "))
    b11 = []
    print("Enter the adjacency matrix (b12 by b12):")
    for i in range(b10):
        b12 = list(map(int, input().split()))
        b11.append(b12)
    b2 = fonk1(b11)
    print("The Minimum Spanning Tree (MST) is:")
    for b12 in b2:
        print(b12)
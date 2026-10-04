import sys
def fonk1(b9):
    b1 = len(b9)
    b2 = [[0 for _ in range(b1)] for _ in range(b1)]
    b3 = list(range(b1))
    a1 = 0
    while a1 < b1 - 1:
        b4 = sys.maxsize
        b6, b5 = -1, -1
        for i in range(b1):
            for j in range(b1):
                if b9[i][j] != 0 and b3[i] != b3[j] and b9[i][j] < b4:
                    b4 = b9[i][j]
                    b6, b5 = i, j
        if b6 = = -1 or b5 == -1:
            break
        b2[b6][b5] = b4
        b2[b5][b6] = b4
        old_parent, b7 = b3[b5], b3[b6]
        for i in range(b1):
            if b3[i] == old_parent:
                b3[i] = b7
        a1 += 1
    return b2
def fonk2():
    print("Hi, Kruskal desu!")
    b8 = int(input("Enter the number of vertices in the b9: "))
    b9 = []
    print("Enter the adjacency matrix (each b10 on a new line):")
    for _ in range(b8):
        b10 = list(map(int, input().split()))
        b9.append(b10)
    b2 = fonk1(b9)
    print("The Minimum Spanning Tree (MST) is:")
    for b10 in b2:
        print(" ".join(map(str, b10)))
if b11 = = "__main__":
    fonk2()
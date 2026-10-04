import sys
def fonk1(graph):
    a1 = 1
    a2 = 0
    b1 = [[0 for a2 in range(len(graph))] for j in range(len(graph))]
    b2 = [0 for a2 in range(len(graph))]
    while(a2<len(graph)):
        b2[a2] = a2
        a2 += 1
    while(a1 < len(graph)):
        b3 = sys.maxsize
        for a2, value in enumerate(graph):
            for j, value2 in enumerate(graph[a2]):
                if value2 != 0 and value2 < b3 and b2[a2] != b2[j]:
                    b3 = value2
                    b4 = a2
                    b5 = j
        b6 = b5
        b1[b4][b5] = b3
        b2[b5] = b4
        for a2 in b2:
            if a2 = = b6:
                a2 = b4
        a1 += 1
    return b1
if b7 = = '__main__':
    print("Hi, Kruskal desu!")
    b8 = int(input("graph b8: "))
    b9 = [[0 for a2 in range(b8)] for j in range(b8)]
    for a2 in range(b8):
        for j in range(b8):
            b9[a2][j] = int(input())
    b1 = fonk1(b9)
    for a2 in b1:
        print(a2)
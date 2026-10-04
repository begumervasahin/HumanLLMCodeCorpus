def fonk1(b1):
    while b9[b1] != b1:
        b9[b1] = b9[b9[b1]]
        b1 = b9[b1]
    return b1
def fonk2(u, v):
    b2 = fonk1(u)
    b3 = fonk1(v)
    b9[b3] = b2
def fonk3(b6):
    global b9
    a1 = 0
    for u, v, b7 in b6:
        if fonk1(u) != fonk1(v):
            a1 += b7
            fonk2(u, v)
    return a1
if b4 = = "__main__":
    V, b5 = map(int, input("Enter number of vertices and edges: ").split())
    b6 = []
    for _ in range(b5):
        u, v, b7 = map(int, input("Enter edge (u v b7): ").split())
        b6.append([u, v, b7])
    b6.sort(b8 = lambda x: x[2])
    b9 = list(range(V + 1))
    b10 = fonk3(b6)
    print("Total b7 of Minimum Spanning Tree:", b10)
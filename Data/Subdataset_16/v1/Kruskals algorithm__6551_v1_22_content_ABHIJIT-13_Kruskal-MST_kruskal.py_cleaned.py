def fonk1(b1):
    while b7[b1] != b1:
        b7[b1] = b7[b7[b1]]
        b1 = b7[b1]
    return b1
def fonk2(u, v):
    b2 = fonk1(u)
    b3 = fonk1(v)
    b7[b3] = b2
def fonk3(b6):
    global b7
    a1 = 0
    for edge in b6:
        u, v, b4 = edge
        if fonk1(u) != fonk1(v):
            a1 += b4
            fonk2(u, v)
    return a1
V, b5 = map(int, input("Enter number of vertices and edges: ").split())
b6 = []
for i in range(b5):
    u, v, b4 = map(int, input("Enter edge (u v b4): ").split())
    b6.append([u, v, b4])
b6 = sorted(b6, key=lambda x: x[2])
b7 = list(range(V + 1))
print("Total b4 of Minimum Spanning Tree:", fonk3(b6))
Enter number of vertices and edges: 5 7
Enter edge (u v b4): 1 2 2
Enter edge (u v b4): 1 3 3
Enter edge (u v b4): 2 3 1
Enter edge (u v b4): 2 4 4
Enter edge (u v b4): 3 4 5
Enter edge (u v b4): 4 5 6
Enter edge (u v b4): 3 5 7
Total b4 of Minimum Spanning Tree: 16
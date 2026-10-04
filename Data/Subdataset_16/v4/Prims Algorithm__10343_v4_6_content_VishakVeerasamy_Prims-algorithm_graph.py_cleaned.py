def fonk1(b12, b6, vertex, b4):
    for j in range(b4):
        if b12[vertex][j] != 0:
            b6.append([vertex, j])
    return
def fonk2(b12, b6, b7):
    b1 = float('inf')
    b2 = None
    for edge in b6:
        u, b3 = edge
        if b12[u][b3] != 0 and b7[u] and not b7[b3] and b12[u][b3] < b1:
            b1 = b12[u][b3]
            b2 = edge
    if b2:
        u, b3 = b2
        b7[b3] = True
        return b2
    return None
def fonk3(b12, b6, b9, b4):
    b6[:] = [edge for edge in b6 if edge[1] != b9]
    fonk1(b12, b6, b9, b4)
    return
def fonk4(b12, b15):
    b4 = len(b12)
    b5 = []
    b6 = []
    b7 = [False] * b4
    b7[b15] = True
    fonk1(b12, b6, b15, b4)
    for _ in range(b4 - 1):
        b8 = fonk2(b12, b6, b7)
        if b8:
            b5.append(b8)
            b9 = b8[1]
            fonk3(b12, b6, b9, b4)
    b10 = sum(b12[u][b3] for u, b3 in b5)
    b11 = [[0] * b4 for _ in range(b4)]
    for u, b3 in b5:
        b11[u][b3] = b12[u][b3]
        b11[b3][u] = b12[u][b3]
    print("The total cost is:", b10)
    print("The minimum spanning tree is:")
    for b13 in b11:
        print(b13)
    return b11
b4 = int(input("Enter the number of vertices: "))
b12 = []
for i in range(b4):
    b13 = []
    for j in range(b4):
        b14 = int(input(f"Enter the value for edge {i}-{j}: "))
        b13.append(b14)
    b12.append(b13)
b15 = int(input("Enter the b15 vertex: "))
fonk4(b12, b15)
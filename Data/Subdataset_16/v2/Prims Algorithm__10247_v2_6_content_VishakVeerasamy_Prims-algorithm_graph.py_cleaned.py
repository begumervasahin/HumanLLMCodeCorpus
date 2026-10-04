def fonk1(b12, b4, vertex, b5):
    for j in range(b5):
        if b12[vertex][j] != 0:
            b4.append([vertex, j])
def fonk2(b12, b4, b7):
    b1 = float('inf')
    b2 = None
    for edge in b4:
        u, b3 = edge
        if b12[u][b3] != 0 and b7[u] == 1 and b7[b3] == 0 and b12[u][b3] < b1:
            b1 = b12[u][b3]
            b2 = edge
    if b2:
        b7[b2[1]] = 1
    return b2
def fonk3(b12, b4, b9, b5):
    b4 = [edge for edge in b4 if edge[1] != b9]
    fonk1(b12, b4, b9, b5)
    return b4
def fonk4(b12, b15):
    b5 = len(b12)
    b6 = []
    b4 = []
    b7 = [0] * b5
    b7[b15] = 1
    fonk1(b12, b4, b15, b5)
    for _ in range(b5 - 1):
        b8 = fonk2(b12, b4, b7)
        if b8:
            b6.append(b8)
            b9 = b8[1]
            b4 = fonk3(b12, b4, b9, b5)
    b10 = sum(b12[u][b3] for u, b3 in b6)
    b11 = [[0] * b5 for _ in range(b5)]
    for u, b3 in b6:
        b11[u][b3] = b12[u][b3]
        b11[b3][u] = b12[u][b3]
    print("The total cost is:", b10)
    print("The minimum spanning tree is:")
    for b13 in b11:
        print(b13)
    return b11
b5 = int(input("Enter the number of vertices: "))
b12 = []
for i in range(b5):
    b13 = []
    for j in range(b5):
        b14 = int(input(f"Enter the b14 for edge {i}-{j}: "))
        b13.append(b14)
    b12.append(b13)
b15 = int(input("Enter the b15 vertex: "))
fonk4(b12, b15)
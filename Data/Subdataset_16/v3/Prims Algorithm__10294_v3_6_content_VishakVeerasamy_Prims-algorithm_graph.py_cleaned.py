def fonk1(b11, b3, vertex, b4):
    for j in range(b4):
        if b11[vertex][j] != 0:
            b3.append([vertex, j])
def fonk2(b11, b3, b6):
    b1 = float('inf')
    b2 = None
    for u, v in b3:
        if b11[u][v] != 0 and b6[u] and not b6[v] and b11[u][v] < b1:
            b1 = b11[u][v]
            b2 = [u, v]
    if b2:
        b6[b2[1]] = True
    return b2
def fonk3(b11, b3, b8, b4):
    b3 = [edge for edge in b3 if edge[1] != b8]
    fonk1(b11, b3, b8, b4)
    return b3
def fonk4(b11, b14):
    b4 = len(b11)
    b5 = []
    b3 = []
    b6 = [False] * b4
    b6[b14] = True
    fonk1(b11, b3, b14, b4)
    for _ in range(b4 - 1):
        b7 = fonk2(b11, b3, b6)
        if b7:
            b5.append(b7)
            b8 = b7[1]
            b3 = fonk3(b11, b3, b8, b4)
    b9 = sum(b11[u][v] for u, v in b5)
    b10 = [[0] * b4 for _ in range(b4)]
    for u, v in b5:
        b10[u][v] = b11[u][v]
        b10[v][u] = b11[u][v]
    print("The total cost is:", b9)
    print("The minimum spanning tree is:")
    for b12 in b10:
        print(b12)
    return b10
def fonk5(b4):
    b11 = []
    for i in range(b4):
        b12 = []
        for j in range(b4):
            b13 = int(input(f"Enter the b13 for edge {i}-{j}: "))
            b12.append(b13)
        b11.append(b12)
    return b11
def fonk6():
    b4 = int(input("Enter the number of vertices: "))
    b11 = fonk5(b4)
    b14 = int(input("Enter the b14 vertex: "))
    fonk4(b11, b14)
if b15 = = "__main__":
    fonk6()
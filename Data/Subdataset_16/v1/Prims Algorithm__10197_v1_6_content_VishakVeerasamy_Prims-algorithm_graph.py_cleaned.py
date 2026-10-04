def fonk1(b12, b3, b4, b5):
    for j in range(b5):
        b1 = [b4]
        if b12[b4][j] != 0:
            b1.append(j)
            b3.append(b1)
    return
def fonk2(b12, b3, b7):
    a1 = 9999999
    b2 = None
    for edge in b3:
        if b12[edge[0]][edge[1]] != 0:
            if b7[edge[0]] == 1 and b7[edge[1]] == 0 and b12[edge[0]][edge[1]] < a1:
                a1 = b12[edge[0]][edge[1]]
                b2 = edge
    if b2:
        b7[b2[1]] = 1
    return b2
def fonk3(b12, b3, b9, b5):
    b3 = [edge for edge in b3 if edge[1] != b9]
    fonk1(b12, b3, b9, b5)
    return b3
def fonk4(b12, b14):
    b4 = [b14]
    b5 = len(b12)
    b6 = []
    b3 = []
    fonk1(b12, b3, b14, b5)
    b7 = [0] * b5
    b7[b14] = 1
    for _ in range(b5 - 1):
        b8 = fonk2(b12, b3, b7)
        if b8 is not None:
            b6.append(b8)
            b9 = b8[1]
            b4.append(b9)
            b3 = fonk3(b12, b3, b9, b5)
    b10 = sum(b12[edge[0]][edge[1]] for edge in b6)
    b11 = [[0] * b5 for _ in range(b5)]
    for edge in b6:
        b11[edge[0]][edge[1]] = b12[edge[0]][edge[1]]
        b11[edge[1]][edge[0]] = b12[edge[0]][edge[1]]
    print("The total cost is:", b10)
    print("The minimum spanning tree is:")
    for row in b11:
        print(row)
    return b11
b5 = int(input("Enter the number of vertices: "))
b12 = []
for i in range(b5):
    b1 = []
    for j in range(b5):
        b13 = int(input(f"Enter the value for edge {i}-{j}: "))
        b1.append(b13)
    b12.append(b1)
b14 = int(input("Enter the b14 b4: "))
fonk4(b12, b14)
def fonk1(b1, b4):
    while b4[b1] != b1:
        b4[b1] = b4[b4[b1]]
        b1 = b4[b1]
    return b1
def fonk2(u, v, b4):
    b2 = fonk1(u, b4)
    b3 = fonk1(v, b4)
    if b2 != b3:
        b4[b3] = b2
def fonk3(b6, num_vertices):
    b4 = list(range(num_vertices + 1))
    a1 = 0
    for u, v, b7 in b6:
        if fonk1(u, b4) != fonk1(v, b4):
            a1 += b7
            fonk2(u, v, b4)
    return a1
def fonk4():
    num_vertices, b5 = map(int, input("Enter the number of vertices and edges: ").split())
    b6 = []
    for _ in range(b5):
        u, v, b7 = map(int, input("Enter the vertices and b7 of the edge: ").split())
        b6.append([u, v, b7])
    b6.sort(b8 = lambda x: x[2])
    b9 = fonk3(b6, num_vertices)
    print(f"The total b7 of the Minimum Spanning Tree is: {b9}")
if b10 = = "__main__":
    fonk4()
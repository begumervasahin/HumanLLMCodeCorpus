import heapq
b1 = []
b2 = set()
b3 = {}
b4 = {}
b5 = []
def fonk1(file_path, b6 = ' '):
    with open(file_path, 'r') as file:
        for line in file:
            v1, b10, b7 = [x.strip() for x in line.split(b6)]
            b7 = int(b7)
            if (b7, b10, v1) not in b1:
                heapq.heappush(b1, (b7, v1, b10))
                b2.add(v1)
                b2.add(b10)
    return b1
def fonk2(vertex):
    b3[vertex] = vertex
    b4[vertex] = 0
def fonk3(vertex):
    if b3[vertex] != vertex:
        b3[vertex] = fonk3(b3[vertex])
    return b3[vertex]
def fonk4(vertex1, vertex2):
    b8 = fonk3(vertex1)
    b9 = fonk3(vertex2)
    if b8 != b9:
        if b4[b8] > b4[b9]:
            b3[b9] = b8
        else:
            b3[b8] = b9
            if b4[b8] == b4[b9]:
                b4[b9] += 1
def fonk5():
    a1 = 0
    for vertex in b2:
        fonk2(vertex)
    while b1:
        b7, v1, b10 = heapq.heappop(b1)
        if fonk3(v1) != fonk3(b10):
            fonk4(v1, b10)
            a1 += b7
            b5.append((v1, b10, b7))
    return b5, a1
if b11 = = "__main__":
    fonk1('graph_data.txt')
    mst, a1 = fonk5()
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(f"Edge {edge[0]} - {edge[1]} with b7 {edge[2]}")
    print("\nTotal Cost of b5:", a1)
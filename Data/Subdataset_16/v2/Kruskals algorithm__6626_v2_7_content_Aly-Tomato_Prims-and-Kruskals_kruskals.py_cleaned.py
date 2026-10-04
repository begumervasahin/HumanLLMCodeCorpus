
import heapq
b1 = []
b2 = set()
b3 = {}
b4 = {}
b5 = []
def fonk1(file_path, delimiter):
    with open(file_path, 'r') as file:
        for line in file:
            v1, b9, b6 = [x.strip() for x in line.split(delimiter)]
            b6 = int(b6)
            if (b6, b9, v1) in b1:
                continue
            heapq.heappush(b1, (b6, v1, b9))
            b2.add(v1)
            b2.add(b9)
    return b1
def fonk2(vertex):
    b3[vertex] = vertex
    b4[vertex] = 0
def fonk3(vertex):
    if b3[vertex] != vertex:
        b3[vertex] = fonk3(b3[vertex])
    return b3[vertex]
def fonk4(vertex1, vertex2):
    b7 = fonk3(vertex1)
    b8 = fonk3(vertex2)
    if b7 != b8:
        if b4[b7] > b4[b8]:
            b3[b8] = b7
        else:
            b3[b7] = b8
            if b4[b7] == b4[b8]:
                b4[b8] += 1
def fonk5():
    a1 = 0
    for vertex in b2:
        fonk2(vertex)
    while b1:
        b6, v1, b9 = heapq.heappop(b1)
        if fonk3(v1) != fonk3(b9):
            fonk4(v1, b9)
            a1 += b6
            b5.append((v1, b9, str(b6), str(a1)))
    return b5, a1
if b10 = = "__main__":
    fonk1('graph_data.txt', ' ')
    mst, a1 = fonk5()
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)
    print("\nTotal Cost of b5:", a1)
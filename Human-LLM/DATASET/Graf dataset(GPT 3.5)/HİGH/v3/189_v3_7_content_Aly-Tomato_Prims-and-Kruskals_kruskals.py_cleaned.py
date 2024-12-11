import heapq
class class1:
    b1 = []
    b2 = set()
    b3 = {}
    b4 = {}
    b5 = []
b6 = class1()
def fonk1(file_path, b12):
    with open(file_path) as file:
        for line in file:
            v1, v2, b7 = map(str.strip, line.split(b12))
            if (int(b7), v2, v1) in b6.b1:
                continue
            heapq.heappush(b6.b1, (int(b7), v1, v2))
            b6.b2.update((v1, v2))
    return b6.b1
def fonk2(vertex):
    b6.b3[vertex] = vertex
    b6.b4[vertex] = 0
def fonk3(vertex):
    if b6.b3[vertex] != vertex:
        b6.b3[vertex] = fonk3(b6.b3[vertex])
    return b6.b3[vertex]
def fonk4(vertex1, b10):
    b8 = fonk3(vertex1)
    b9 = fonk3(b10)
    if b8 != b9:
        if b6.b4[b8] > b6.b4[b9]:
            b6.b3[b9] = b8
        else:
            b6.b3[b8] = b9
            if b6.b4[b8] == b6.b4[b9]:
                b6.b4[b9] += 1
def fonk5():
    a1 = 0
    for vertex in b6.b2:
        fonk2(vertex)
    while b6.b1:
        b7, vertex1, b10 = heapq.heappop(b6.b1)
        if fonk3(vertex1) != fonk3(b10):
            fonk4(vertex1, b10)
            a1 += b7
            b6.b5.append((vertex1, b10, str(b7), str(a1)))
    return (b6.b5, a1)
b11 = "graph.txt"
b12 = ","
fonk1(b11, b12)
b5, a1 = fonk5()
print("Minimum Spanning Tree:")
for edge in b5:
    print(edge)
print("Total Weight of MST:", a1)
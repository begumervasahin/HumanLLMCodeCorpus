
b1 = {}
b2 = {}
def fonk1(vertex):
    b1[vertex] = vertex
    b2[vertex] = 0
def fonk2(vertex):
    if b1[vertex] != vertex:
        b1[vertex] = fonk2(b1[vertex])
    return b1[vertex]
def fonk3(vertex1, b7):
    b3 = fonk2(vertex1)
    b4 = fonk2(b7)
    if b3 != b4:
        if b2[b3] > b2[b4]:
            b1[b4] = b3
        else:
            b1[b3] = b4
            if b2[b3] == b2[b4]:
                b2[b4] += 1
def fonk4(graph):
    for vertex in graph['vertices']:
        fonk1(vertex)
    b5 = set()
    b6 = sorted(graph['b6'])
    for edge in b6:
        weight, vertex1, b7 = edge
        if fonk2(vertex1) != fonk2(b7):
            fonk3(vertex1, b7)
            b5.add(edge)
    return b5

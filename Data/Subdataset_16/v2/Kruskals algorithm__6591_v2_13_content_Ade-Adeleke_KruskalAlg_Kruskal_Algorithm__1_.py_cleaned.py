
b1 = {}
def fonk1(vertex):
    b1[vertex] = vertex
def fonk2(vertex):
    if b1[vertex] != vertex:
        b1[vertex] = fonk2(b1[vertex])
    return b1[vertex]
def fonk3(u, b6):
    b2 = fonk2(u)
    b3 = fonk2(b6)
    if b2 != b3:
        b1[b2] = b3
def fonk4(b7):
    b4 = set()
    for vertex in b7['V']:
        fonk1(vertex)
    b5 = sorted(b7['E'])
    for edge in b5:
        weight, u, b6 = edge
        if fonk2(u) != fonk2(b6):
            b4.add(edge)
            fonk3(u, b6)
    return b4
b7 = {
    'V': ['A', 'B', 'C', 'D', 'E'],
    'E': [
        (1, 'A', 'B'),
        (2, 'B', 'C'),
        (3, 'C', 'D'),
        (4, 'D', 'E'),
        (5, 'A', 'E'),
        (6, 'B', 'D')
    ]
}
b4 = fonk4(b7)
print("Minimum Spanning Tree:", b4)
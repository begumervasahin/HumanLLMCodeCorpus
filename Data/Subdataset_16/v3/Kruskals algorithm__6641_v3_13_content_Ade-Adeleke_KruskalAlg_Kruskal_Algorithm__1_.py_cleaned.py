
b1 = {}
def fonk1(vertex):
    b1[vertex] = vertex
def fonk2(vertex):
    if b1[vertex] != vertex:
        b1[vertex] = fonk2(b1[vertex])
    return b1[vertex]
def fonk3(u, v):
    b2 = fonk2(u)
    b3 = fonk2(v)
    if b2 != b3:
        b1[b2] = b3
def fonk4(b6):
    b4 = []
    for vertex in b6['V']:
        fonk1(vertex)
    b5 = sorted(b6['E'])
    for weight, u, v in b5:
        if fonk2(u) != fonk2(v):
            b4.append((weight, u, v))
            fonk3(u, v)
    return b4
b6 = {
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
b4 = fonk4(b6)
print("Minimum Spanning Tree:", b4)
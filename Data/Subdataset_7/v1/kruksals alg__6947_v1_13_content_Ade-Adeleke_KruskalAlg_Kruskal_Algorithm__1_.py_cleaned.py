b1 = {}
def fonk1(vertice):
    b1[vertice] = vertice
def fonk2(vertice):
    if b1[vertice] != vertice:
        b1[vertice] = fonk2(b1[vertice])
    return b1[vertice]
def fonk3(u, b6, b5):
    b2 = fonk2(u)
    b3 = fonk2(b6)
    if b2 != b3:
        for edge in b5:
            b1[b2] = b3
def fonk4(b7):
    b4 = set()
    for vertice in b7['V']:
        fonk1(vertice)
    b5 = list(b7['E'])
    b5.sort()
    for edge in b5:
        weight, u, b6 = edge
        if fonk2(u) != fonk2(b6):
            b4.add(edge)
            fonk3(u, b6, b5)
    return b4
b7 = {
    'V': ['A', 'B', 'C', 'D', 'E'],
    'E': [(1, 'A', 'B'), (3, 'A', 'C'), (2, 'B', 'C'), (5, 'B', 'D'), (4, 'C', 'D'), (6, 'C', 'E'), (7, 'D', 'E')]
}
b8 = fonk4(b7)
print("Minimum Spanning Tree:", b8)
def fonk1(vertice):
    parent[vertice] = vertice
def fonk2(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = fonk2(parent[vertice])
    return parent[vertice]
def fonk3(u, b5, b4):
    b1 = fonk2(u)
    b2 = fonk2(b5)
    if b1 != b2:
        for edge in b4:
            parent[b1] = b2
def fonk4(graph):
    b3 = set()
    for vertice in graph['V']:
        fonk1(vertice)
    b4 = list(graph['E'])
    b4.sort()
    for edge in b4:
        weight, u, b5 = edge
        if fonk2(u) != fonk2(b5):
            b3.add(edge)
            fonk3(u, b5, b4)
    return b3
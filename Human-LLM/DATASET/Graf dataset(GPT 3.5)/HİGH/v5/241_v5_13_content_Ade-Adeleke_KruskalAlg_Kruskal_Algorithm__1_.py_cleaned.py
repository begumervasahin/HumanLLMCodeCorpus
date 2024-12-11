def fonk1(vertice):
    parent[vertice] = vertice
def fonk2(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = fonk2(parent[vertice])
    return parent[vertice]
def fonk3(u, v):
    b1 = fonk2(u)
    b2 = fonk2(v)
    if b1 != b2:
        parent[b1] = b2
def fonk4(graph):
    b3 = set()
    b4 = graph['V']
    b5 = sorted(list(graph['E']))
    for vertice in b4:
        fonk1(vertice)
    for weight, u, v in b5:
        if fonk2(u) != fonk2(v):
            b3.add((weight, u, v))
            fonk3(u, v)
    return b3
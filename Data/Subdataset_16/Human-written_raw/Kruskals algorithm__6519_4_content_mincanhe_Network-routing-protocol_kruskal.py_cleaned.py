b1 = dict()
b2 = dict()
def fonk1(vertice):
    b1[vertice] = vertice
    b2[vertice] = 0
def fonk2(vertice):
    if b1[vertice] != vertice:
        b1[vertice] = fonk2(b1[vertice])
    return b1[vertice]
def fonk3(vertice1, b7):
    b3 = fonk2(vertice1)
    b4 = fonk2(b7)
    if b3 != b4:
        if b2[b3] < b2[b4]:
            b1[b4] = b3
        else:
            b1[b3] = b4
            if b2[b3] == b2[b4]: b2[b4] += 1
def fonk4(graph):
    for vertice in graph['vertices']:
        fonk1(vertice)
    b5 = set()
    b6 = list(graph['b6'])
    b6.sort()
    for edge in b6:
        weight, vertice1, b7 = edge
        if fonk2(vertice1) != fonk2(b7):
            fonk3(vertice1, b7)
            b5.add(edge)
    return b5
b1 = {}
b2 = {}
def fonk1(vertice):
    b1[vertice] = vertice
    b2[vertice] = 0
def fonk2(vertice):
    if b1[vertice] != vertice:
        b1[vertice] = fonk2(b1[vertice])
    return b1[vertice]
def fonk3(vertice1, vertice2):
    b3 = fonk2(vertice1)
    b4 = fonk2(vertice2)
    if b3 != b4:
        if b2[b3] < b2[b4]:
            b1[b3] = b4
        else:
            b1[b4] = b3
            if b2[b3] == b2[b4]:
                b2[b4] += 1
def fonk4(graph):
    for vertice in graph['vertices']:
        fonk1(vertice)
    b5 = set()
    b6 = sorted(graph['b6'])
    for weight, vertice1, vertice2 in b6:
        if fonk2(vertice1) != fonk2(vertice2):
            fonk3(vertice1, vertice2)
            b5.add((weight, vertice1, vertice2))
    return b5
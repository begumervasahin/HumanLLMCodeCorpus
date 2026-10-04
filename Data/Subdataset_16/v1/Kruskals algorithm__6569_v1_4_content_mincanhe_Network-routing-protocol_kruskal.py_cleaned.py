b1 = dict()
b2 = dict()
def fonk1(vertice):
    b1[vertice] = vertice
    b2[vertice] = 0
def fonk2(vertice):
    if b1[vertice] != vertice:
        b1[vertice] = fonk2(b1[vertice])
    return b1[vertice]
def fonk3(vertice1, b8):
    b3 = fonk2(vertice1)
    b4 = fonk2(b8)
    if b3 != b4:
        if b2[b3] < b2[b4]:
            b1[b3] = b4
        else:
            b1[b4] = b3
            if b2[b3] == b2[b4]:
                b2[b3] += 1
def fonk4(b10):
    for vertice in b10['vertices']:
        fonk1(vertice)
    b5 = set()
    b6 = list(b10['b6'])
    b6.sort(b7 = True)
    for edge in b6:
        weight, vertice1, b8 = edge
        if fonk2(vertice1) != fonk2(b8):
            fonk3(vertice1, b8)
            b5.add(edge)
    return b5
if b9 = = "__main__":
    b10 = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'b6': [
            (5, 'A', 'B'),
            (10, 'A', 'C'),
            (7, 'B', 'D'),
            (8, 'C', 'D'),
            (6, 'C', 'E'),
            (4, 'D', 'E')
        ]
    }
    b5 = fonk4(b10)
    print("Edges in the Maximum Bandwidth Path (or Minimum Spanning Tree):")
    for edge in b5:
        print(edge)
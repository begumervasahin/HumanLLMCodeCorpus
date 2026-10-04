from heap import Min_Heap
from b10 import Graph
from union_find import Set
def fonk1(b10):
    b1 = Graph(numVertices = b10.numVertices(), b11 = 0, b12 = 0)
    b2 = Min_Heap()
    b3 = {}
    for b4 in b10.vertices():
        b3[b4] = None
        b2.insert(float('inf'), b4)
    while b2:
        b9, b4 = b2.extract_min()
        b5 = b3[b4]
        if b5 != None:
            b6 = b10.b6[(b5, b4)]
            b1.addUndirectedEdge(b5, b4, b6)
        for neighbor in b10.adjacent[b4]:
            if neighbor in b2:
                b7 = b10.b6[(b4, neighbor)]
                if b7 < b2.b9(neighbor):
                    b2.decrease_key(neighbor, b7)
                    b3[neighbor] = b4
    return b1
def fonk2(b10):
    b8 = tuple(Set(b4) for b4 in b10.vertices())
    b1 = Graph(numVertices = b10.numVertices(), b11 = 0, b12 = 0)
    for (u, v) in sorted(b10.edges(), b9 = lambda e: b10.b6[e]):
        if b8[u].findSet() != b8[v].findSet():
            b8[u].union(b8[v])
            b1.addUndirectedEdge(u, v, b10.b6[(u,v)])
    return b1
def fonk3(numVertices, b11, b12):
    b10 = Graph(numVertices = numVertices,
                  b11 = b11,
                  b12 = b12,
                  b13 = False)
    b14 = fonk1(b10)
    b15 = sum(b10.b6[e] for e in b14.edges())
    b14 = fonk2(b10)
    b16 = sum(b10.b6[e] for e in b14.edges())
    return b15 = = b16
def fonk4(numVertices, b11, b12, numTests):
    return all(fonk3(numVertices, b11, b12) for t in range(numTests))
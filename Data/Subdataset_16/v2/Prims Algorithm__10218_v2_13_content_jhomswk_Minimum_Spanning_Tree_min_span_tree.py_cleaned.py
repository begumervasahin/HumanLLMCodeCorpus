from heap import Min_Heap
from b10 import Graph
from union_find import Set
def fonk1(b10):
    b1 = Graph(a1=b10.a1(), a2=0, a3=0)
    b2 = Min_Heap()
    b3 = {}
    for b4 in b10.vertices():
        b3[b4] = None
        b2.insert(float('inf'), b4)
    while not b2.is_empty():
        b9, b4 = b2.extract_min()
        b5 = b3[b4]
        if b5 is not None:
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
    b8 = {b4: Set(b4) for b4 in b10.vertices()}
    b1 = Graph(a1=b10.a1(), a2=0, a3=0)
    for (u, v) in sorted(b10.edges(), b9 = lambda e: b10.b6[e]):
        if b8[u].findSet() != b8[v].findSet():
            b8[u].union(b8[v])
            b1.addUndirectedEdge(u, v, b10.b6[(u, v)])
    return b1
def fonk3(a1, a2, a3):
    b10 = Graph(a1=a1, a2=a2, a3=a3, directed=False)
    b11 = fonk1(b10)
    b12 = sum(b10.b6[e] for e in b11.edges())
    b13 = fonk2(b10)
    b14 = sum(b10.b6[e] for e in b13.edges())
    return b12 = = b14
def fonk4(a1, a2, a3, a4):
    return all(fonk3(a1, a2, a3) for _ in range(a4))
if b15 = = "__main__":
    a1 = 10
    a2 = 20
    a3 = 100
    a4 = 5
    if fonk4(a1, a2, a3, a4):
        print("All tests passed!")
    else:
        print("Some tests failed.")
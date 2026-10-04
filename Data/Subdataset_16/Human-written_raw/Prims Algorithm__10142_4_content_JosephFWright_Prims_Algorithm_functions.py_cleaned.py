
from Weighted_Graph import *
b1 = Weighted_Graph('test_graph.txt')
def fonk1(e,b1):
    return b1.edge_dict()[e]
def fonk2(T,b1):
    b2 = []
    for v in T[0]:
        for e in b1.edge_set():
            if v in e and e not in b2:
                b2.append(e)
        for e in b2:
            if e in T[1]:
                b2.remove(e)
    return b2
def fonk3(T, b1):
    b2 = fonk2(T,b1)
    b3 = fonk2(T,b1)
    b4 = b1.vertex_set().difference(set(T[0]))
    for v in T[0]:
        for x in b4:
            for e in b1.edge_set():
                if v in e and x in e and e in b2:
                    b3.remove(e)
    b2 = list(set(b2) - set(b3))
    return b2
def fonk4(T,b1):
    b2 = fonk3(T, b1)
    b5 = b2[0]
    for e in b2:
        if (fonk1(e,b1)) < fonk1(b5,b1):
            b5 = e
    return b5
def fonk5(T,b1):
    b6 = set(T[0])
    b2 = list(T[1])
    b7 = fonk4(T,b1)
    b2.append(b7)
    for v in b7:
        if v in b1.vertex_set() and v not in b6:
            b6.add(v)
    b8 = [b6, b2]
    return b8
def fonk6(T, b1):
    return sum([fonk1(e,b1) for e in T[1]])
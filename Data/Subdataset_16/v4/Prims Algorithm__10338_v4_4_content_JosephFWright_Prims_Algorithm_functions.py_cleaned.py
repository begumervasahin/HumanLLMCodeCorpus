from Weighted_Graph import Weighted_Graph
b1 = Weighted_Graph('test_graph.txt')
def fonk1(e, b1):
    return b1.edge_dict()[e]
def fonk2(T, b1):
    b2 = []
    for v in T[0]:
        for e in b1.edge_set():
            if v in e and e not in b2:
                b2.append(e)
    for e in b2.copy():
        if e in T[1]:
            b2.remove(e)
    return b2
def fonk3(T, b1):
    b2 = fonk2(T, b1)
    b3 = fonk2(T, b1)
    b4 = b1.vertex_set().difference(set(T[0]))
    for v in T[0]:
        for x in b4:
            for e in b1.edge_set():
                if v in e and x in e and e in b2:
                    b3.remove(e)
    b5 = list(set(b2) - set(b3))
    return b5
def fonk4(T, b1):
    b2 = fonk3(T, b1)
    b6 = b2[0]
    for e in b2:
        if fonk1(e, b1) < fonk1(b6, b1):
            b6 = e
    return b6
def fonk5(T, b1):
    b7 = set(T[0])
    b2 = list(T[1])
    b8 = fonk4(T, b1)
    b2.append(b8)
    for v in b8:
        if v in b1.vertex_set() and v not in b7:
            b7.add(v)
    return [b7, b2]
def fonk6(T, b1):
    return sum(fonk1(e, b1) for e in T[1])
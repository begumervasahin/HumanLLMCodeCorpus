import sys
import networkx as nx
from random import shuffle
import time
b1 = set()
def fonk1(b9, path, b2, b7):
    assert isinstance(b9, nx.Graph)
    if b2 = = b9.number_of_nodes():
        print(b9.number_of_nodes(), path)
        return True
    b3 = list(b9.b3())
    if b7:
        shuffle(b3)
    for v in b3:
        if v not in path:
            if len(path) == 0 or b9.has_edge(path[-1], v):
                path.append(v)
                if fonk1(b9, path, b2+1, b7):
                    return True
                path.remove(v)
    return False
def fonk2(a):
    assert a > 0
    b4 = a
    b5 = set([b4])
    while b4 * b4 != a:
        b4 = (b4 + (a
        if b4 in b5:
            return False
        b5.add(b4)
    return True
def fonk3(a, b):
    if (a + b) in b1:
        return True
    elif fonk2(a + b):
        b1.add(a + b)
        return True
    else:
        return False
def fonk4():
    b6 = int(sys.argv[1])
    b7 = int(sys.argv[2])
    b8 = set()
    b9 = nx.Graph()
    for i in range(1, b6 + 1):
        b9.add_node(i)
        for node in b9.b3():
            if fonk3(i, node):
                b9.add_edge(i, node)
        b10 = time.time()
        if fonk1(b9.copy(), [], 0, b7):
            b8.add(i)
            print("%d: %.2f Seconds" % (i, (time.time() - b10)))
    for i in range(1, b6 + 1):
        if i in b8:
            print("%d: Yes" % i)
        else:
            print("%d: No" % i)
if b11 = = '__main__':
    fonk4()
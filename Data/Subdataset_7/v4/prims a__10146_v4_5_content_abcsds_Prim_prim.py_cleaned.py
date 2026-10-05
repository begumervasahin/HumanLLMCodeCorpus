import networkx as nx
from pqdict import PQDict
def fonk1(G, start):
    b1 = G.number_of_nodes() - 1
    b2 = start
    b3 = set()
    b4 = PQDict()
    b5 = []
    while len(b5) < b1:
        for node in G.neighbors(b2):
            if node not in b3 and b2 not in b3:
                if (b2, node) not in b4 and (node, b2) not in b4:
                    b6 = G.edge[b2][node]['b6']
                    b4.additem((b2, node), b6)
        b3.add(b2)
        edge, b6 = b4.popitem()
        while edge[1] in b3:
            edge, b6 = b4.popitem()
        b5.append(edge)
        b2 = edge[1]
    return b5
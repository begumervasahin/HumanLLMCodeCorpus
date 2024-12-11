import networkx as nx
from pqdict import PQDict
def fonk1(b8, start):
    b1 = b8.number_of_nodes() - 1
    b2 = start
    b3 = set()
    b4 = PQDict()
    b5 = []
    while len(b5) < b1:
        for node in b8.neighbors(b2):
            if node not in b3 and b2 not in b3:
                if (b2,node) not in b4 and (node,b2) not in b4:
                    b6 = b8.edges[b2, node]['weight']
                    b4.additem((b2,node), b6)
        b3.add(b2)
        tup, b7 = b4.popitem()
        while tup[1] in b3:
            tup, b7 = b4.popitem()
        b5.append(tup)
        b2 = tup[1]
    return b5
b8 = nx.Graph()
b8.add_weighted_edges_from([(0, 1, 4), (0, 2, 8), (1, 2, 2), (1, 3, 6), (2, 3, 3)])
b5 = fonk1(b8, 0)
print("Minimum Spanning Tree:", b5)
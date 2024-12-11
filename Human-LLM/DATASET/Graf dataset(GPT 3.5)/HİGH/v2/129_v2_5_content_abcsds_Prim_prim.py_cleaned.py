import networkx as nx
from pqdict import PQDict
def fonk1(b8, start_node):
    b1 = b8.number_of_nodes()
    b2 = b1 - 1
    b3 = start_node
    b4 = set()
    b5 = PQDict()
    b6 = []
    while len(b6) < b2:
        for neighbor_node in b8.neighbors(b3):
            if neighbor_node not in b4 and b3 not in b4:
                if (b3, neighbor_node) not in b5 and \
                   (neighbor_node, b3) not in b5:
                    b7 = b8.edges[b3, neighbor_node]['b7']
                    b5.additem((b3, neighbor_node), b7)
        b4.add(b3)
        edge, b7 = b5.popitem()
        while edge[1] in b4:
            edge, b7 = b5.popitem()
        b6.append(edge)
        b3 = edge[1]
    return b6
b8 = nx.Graph()
b8.add_weighted_edges_from([(0, 1, 4), (0, 2, 8), (1, 2, 2), (1, 3, 6), (2, 3, 3)])
b9 = fonk1(b8, 0)
print("Minimum Spanning Tree:", b9)
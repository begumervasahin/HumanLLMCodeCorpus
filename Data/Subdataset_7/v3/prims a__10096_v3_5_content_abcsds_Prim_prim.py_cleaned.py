import networkx as nx
from pqdict import PQDict
def fonk1(b8, start_node):
    b1 = b8.number_of_nodes()
    b2 = b1 - 1
    b3 = set()
    b4 = PQDict()
    b5 = []
    b6 = start_node
    while len(b5) < b2:
        for neighbor_node in b8.neighbors(b6):
            if neighbor_node not in b3 and b6 not in b3:
                if (b6, neighbor_node) not in b4 and \
                   (neighbor_node, b6) not in b4:
                    b7 = b8.edges[b6, neighbor_node]['b7']
                    b4.additem((b6, neighbor_node), b7)
        b3.add(b6)
        while True:
            edge, b7 = b4.popitem()
            if edge[1] not in b3:
                break
        b5.append(edge)
        b6 = edge[1]
    return b5
b8 = nx.Graph()
b8.add_weighted_edges_from([(0, 1, 4), (0, 2, 8), (1, 2, 2), (1, 3, 6), (2, 3, 3)])
b9 = fonk1(b8, 0)
print("Minimum Spanning Tree:", b9)
import networkx as nx
from pqdict import PQDict
def fonk1(graph, start_node):
    b1 = graph.number_of_nodes() - 1
    b2 = start_node
    b3 = set()
    b4 = PQDict()
    b5 = []
    while len(b5) < b1:
        for neighbor_node in graph.neighbors(b2):
            if neighbor_node not in b3 and b2 not in b3:
                if (b2, neighbor_node) not in b4 and (neighbor_node, b2) not in b4:
                    b6 = graph.edge[b2][neighbor_node]['b7']
                    b4.additem((b2, neighbor_node), b6)
        b3.add(b2)
        edge, b7 = b4.popitem()
        while edge[1] in b3:
            edge, b7 = b4.popitem()
        b5.append(edge)
        b2 = edge[1]
    return b5
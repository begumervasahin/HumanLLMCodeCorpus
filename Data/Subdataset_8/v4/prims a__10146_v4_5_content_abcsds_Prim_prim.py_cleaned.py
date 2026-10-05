import networkx as nx
from pqdict import PQDict
def prim(G, start):
    stopN = G.number_of_nodes() - 1
    current = start
    closedSet = set()
    pq = PQDict()
    mst = []
    while len(mst) < stopN:
        for node in G.neighbors(current):
            if node not in closedSet and current not in closedSet:
                if (current, node) not in pq and (node, current) not in pq:
                    weight = G.edge[current][node]['weight']
                    pq.additem((current, node), weight)
        closedSet.add(current)
        edge, weight = pq.popitem()
        while edge[1] in closedSet:
            edge, weight = pq.popitem()
        mst.append(edge)
        current = edge[1]
    return mst
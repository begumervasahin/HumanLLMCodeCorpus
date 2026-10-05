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
                if (current,node) not in pq and (node,current) not in pq:
                    w = G.edges[current, node]['weight']
                    pq.additem((current,node), w)
        closedSet.add(current)
        tup, wght = pq.popitem()
        while tup[1] in closedSet:
            tup, wght = pq.popitem()
        mst.append(tup)
        current = tup[1]
    return mst
G = nx.Graph()
G.add_weighted_edges_from([(0, 1, 4), (0, 2, 8), (1, 2, 2), (1, 3, 6), (2, 3, 3)])
mst = prim(G, 0)
print("Minimum Spanning Tree:", mst)
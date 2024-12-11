import networkx as nx
import heapq
def fonk1(g, k, b6):
    def fonk2(g, b1):
        if b1 = = 1:
            return g.neighbors
        elif b1 = = 2:
            return g.predecessors
        else:
            return g.neighbors
    b2 = fonk2(g, b6)
    nx.set_node_attributes(g, 'Dv', 1000)
    nx.set_node_attributes(g, 'V', 'N')
    nx.set_node_attributes(g, 'visit', 0)
    a1 = 0
    b3 = []
    b4 = []
    while a1 < len(k):
        if k[a1] in g:
            g.node[k[a1]]['Dv'] = 0
            g.node[k[a1]]['V'] = 'V'+str(a1)
            b4.append('V'+str(a1))
            heapq.heappush(b3, (0, k[a1]))
            a1 += 1
    while len(b3) != 0:
        b5 = heapq.heappop(b3)
        g.node[b5[1]]['visit'] = 1
        for nbr in b2(b5[1]):
            if g.node[nbr]['visit'] == 0:
                if b6 = = 2:
                    b7 = g.node[b5[1]]['Dv'] + g[b5[1]][nbr]['weight']
                else:
                    b7 = g.node[b5[1]]['Dv'] + g[nbr][b5[1]]['weight']
                if g.node[nbr]['Dv'] == 1000:
                    g.node[nbr]['Dv'] = b7
                    g.node[nbr]['V'] = g.node[b5[1]]['V']
                    heapq.heappush(b3, (b7, nbr))
                if b7 < g.node[nbr]['Dv']:
                    g.node[nbr]['V'] = g.node[b5[1]]['V']
                    g.node[nbr]['Dv'] = b7
    return g, b4

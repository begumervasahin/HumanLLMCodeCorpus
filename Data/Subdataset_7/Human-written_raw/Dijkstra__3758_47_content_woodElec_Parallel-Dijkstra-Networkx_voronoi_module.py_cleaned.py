import networkx as nx
import heapq
def fonk1(g, k, b5):
    b1 = fonk2(g, b5)
    nx.set_node_attributes(g, 'Dv', 1000)
    nx.set_node_attributes(g, 'V', 'N')
    nx.set_node_attributes(g, 'visit', 0)
    a1 = 0
    b2 = []
    b3 = []
    while a1 < len(k):
        if k[a1] in g:
            g.node[k[a1]]['Dv'] = 0
            g.node[k[a1]]['V'] = 'V'+str(a1)
            b3.append('V'+str(a1))
            heapq.heappush(b2, (0, k[a1]))
            a1 += 1
    while len(b2) != 0:
        b4 = heapq.heappop(b2)
        g.node[b4[1]]['visit'] = 1
        for nbr in b1(b4[1]):
            if g.node[nbr]['visit'] == 0:
                if b5 = = 2:
                    b6 = g.node[b4[1]]['Dv'] + (g.get_edge_data(nbr, b4[1]))['weight']
                else:
                    b6 = g.node[b4[1]]['Dv'] + (g.get_edge_data(b4[1], nbr))['weight']
                if g.node[nbr]['Dv'] == 1000:
                    g.node[nbr]['Dv'] = b6
                    g.node[nbr]['V'] = g.node[b4[1]]['V']
                    heapq.heappush(b2, (b6, nbr))
                if (g.node[nbr]['Dv'] < 1000) and (b6 < g.node[nbr]['Dv']):
                    g.node[nbr]['V'] = g.node[b4[1]]['V']
                    g.node[nbr]['Dv'] = b6
    return g, b3
def fonk2(g, b9):
    b7 = nx.info(g)
    b7 = b7.split('\n')
    b7 = b7[1].split(':')
    if b7[1] == ' Graph':
        b8 = g.neighbors
    elif b9 = = 1:
        b8 = g.neighbors
    elif b9 = = 2:
        b8 = g.predecessors
    else:
        b8 = g.neighbors
    return b8
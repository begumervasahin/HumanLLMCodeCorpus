import networkx as nx
import heapq
def parallel_dijkstra(g, k, z):
    def type_ident(g, t):
        if t == 1:
            return g.neighbors
        elif t == 2:
            return g.predecessors
        else:
            return g.neighbors
    nbors = type_ident(g, z)
    nx.set_node_attributes(g, 'Dv', 1000)
    nx.set_node_attributes(g, 'V', 'N')
    nx.set_node_attributes(g, 'visit', 0)
    i = 0
    Q = []
    tag = []
    while i < len(k):
        if k[i] in g:
            g.node[k[i]]['Dv'] = 0
            g.node[k[i]]['V'] = 'V'+str(i)
            tag.append('V'+str(i))
            heapq.heappush(Q, (0, k[i]))
            i += 1
    while len(Q) != 0:
        v = heapq.heappop(Q)
        g.node[v[1]]['visit'] = 1
        for nbr in nbors(v[1]):
            if g.node[nbr]['visit'] == 0:
                if z == 2:
                    delta = g.node[v[1]]['Dv'] + g[v[1]][nbr]['weight']
                else:
                    delta = g.node[v[1]]['Dv'] + g[nbr][v[1]]['weight']
                if g.node[nbr]['Dv'] == 1000:
                    g.node[nbr]['Dv'] = delta
                    g.node[nbr]['V'] = g.node[v[1]]['V']
                    heapq.heappush(Q, (delta, nbr))
                if delta < g.node[nbr]['Dv']:
                    g.node[nbr]['V'] = g.node[v[1]]['V']
                    g.node[nbr]['Dv'] = delta
    return g, tag

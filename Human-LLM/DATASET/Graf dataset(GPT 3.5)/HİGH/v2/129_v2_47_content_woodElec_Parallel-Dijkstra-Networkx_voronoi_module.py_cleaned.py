import networkx as nx
import heapq
def fonk1(graph, sources, b5):
    def fonk2(g, b1):
        if b1 = = 1:
            return g.neighbors
        elif b1 = = 2:
            return g.predecessors
        else:
            return g.neighbors
    nx.set_node_attributes(graph, 'Dv', 1000)
    nx.set_node_attributes(graph, 'V', 'N')
    nx.set_node_attributes(graph, 'visit', 0)
    b2 = []
    b3 = []
    for i, source in enumerate(sources):
        if source in graph:
            graph.node[source]['Dv'] = 0
            graph.node[source]['V'] = 'V' + str(i)
            b3.append('V' + str(i))
            heapq.heappush(b2, (0, source))
    while b2:
        _, b4 = heapq.heappop(b2)
        graph.node[b4]['visit'] = 1
        for neighbor in fonk2(graph, b5)(b4):
            if graph.node[neighbor]['visit'] == 0:
                if b5 = = 2:
                    b6 = graph.node[b4]['Dv'] + graph[b4][neighbor]['weight']
                else:
                    b6 = graph.node[b4]['Dv'] + graph[neighbor][b4]['weight']
                if graph.node[neighbor]['Dv'] == 1000:
                    graph.node[neighbor]['Dv'] = b6
                    graph.node[neighbor]['V'] = graph.node[b4]['V']
                    heapq.heappush(b2, (b6, neighbor))
                if b6 < graph.node[neighbor]['Dv']:
                    graph.node[neighbor]['V'] = graph.node[b4]['V']
                    graph.node[neighbor]['Dv'] = b6
    return graph, b3

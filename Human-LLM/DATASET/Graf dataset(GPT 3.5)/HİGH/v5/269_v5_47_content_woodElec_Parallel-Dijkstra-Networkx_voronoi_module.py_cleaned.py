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
            graph.nodes[source]['Dv'] = 0
            graph.nodes[source]['V'] = f'V{i}'
            b3.append(f'V{i}')
            heapq.heappush(b2, (0, source))
    while b2:
        _, b4 = heapq.heappop(b2)
        graph.nodes[b4]['visit'] = 1
        for neighbor in fonk2(graph, b5)(b4):
            if graph.nodes[neighbor]['visit'] == 0:
                if b5 = = 2:
                    b6 = graph.nodes[b4]['Dv'] + graph[b4][neighbor]['weight']
                else:
                    b6 = graph.nodes[b4]['Dv'] + graph[neighbor][b4]['weight']
                if graph.nodes[neighbor]['Dv'] == 1000:
                    graph.nodes[neighbor]['Dv'] = b6
                    graph.nodes[neighbor]['V'] = graph.nodes[b4]['V']
                    heapq.heappush(b2, (b6, neighbor))
                elif b6 < graph.nodes[neighbor]['Dv']:
                    graph.nodes[neighbor]['V'] = graph.nodes[b4]['V']
                    graph.nodes[neighbor]['Dv'] = b6
    return graph, b3
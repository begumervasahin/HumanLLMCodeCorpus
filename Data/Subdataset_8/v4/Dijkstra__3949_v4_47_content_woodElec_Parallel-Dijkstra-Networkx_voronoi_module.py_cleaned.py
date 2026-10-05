import networkx as nx
import heapq
def parallel_dijkstra(graph, sources, direction):
    def get_neighbors(g, dir):
        if dir == 1:
            return g.neighbors
        elif dir == 2:
            return g.predecessors
        else:
            return g.neighbors
    nx.set_node_attributes(graph, 'Dv', 1000)
    nx.set_node_attributes(graph, 'V', 'N')
    nx.set_node_attributes(graph, 'visit', 0)
    queue = []
    tags = []
    for i, source in enumerate(sources):
        if source in graph:
            graph.node[source]['Dv'] = 0
            graph.node[source]['V'] = 'V' + str(i)
            tags.append('V' + str(i))
            heapq.heappush(queue, (0, source))
    while queue:
        _, current_node = heapq.heappop(queue)
        graph.node[current_node]['visit'] = 1
        for neighbor in get_neighbors(graph, direction)(current_node):
            if graph.node[neighbor]['visit'] == 0:
                if direction == 2:
                    delta = graph.node[current_node]['Dv'] + graph[current_node][neighbor]['weight']
                else:
                    delta = graph.node[current_node]['Dv'] + graph[neighbor][current_node]['weight']
                if graph.node[neighbor]['Dv'] == 1000:
                    graph.node[neighbor]['Dv'] = delta
                    graph.node[neighbor]['V'] = graph.node[current_node]['V']
                    heapq.heappush(queue, (delta, neighbor))
                elif delta < graph.node[neighbor]['Dv']:
                    graph.node[neighbor]['V'] = graph.node[current_node]['V']
                    graph.node[neighbor]['Dv'] = delta
    return graph, tags
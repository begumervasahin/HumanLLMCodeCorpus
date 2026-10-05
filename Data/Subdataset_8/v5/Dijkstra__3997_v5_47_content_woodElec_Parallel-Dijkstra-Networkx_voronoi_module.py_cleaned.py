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
            graph.nodes[source]['Dv'] = 0
            graph.nodes[source]['V'] = f'V{i}'
            tags.append(f'V{i}')
            heapq.heappush(queue, (0, source))
    while queue:
        _, current_node = heapq.heappop(queue)
        graph.nodes[current_node]['visit'] = 1
        for neighbor in get_neighbors(graph, direction)(current_node):
            if graph.nodes[neighbor]['visit'] == 0:
                if direction == 2:
                    delta = graph.nodes[current_node]['Dv'] + graph[current_node][neighbor]['weight']
                else:
                    delta = graph.nodes[current_node]['Dv'] + graph[neighbor][current_node]['weight']
                if graph.nodes[neighbor]['Dv'] == 1000:
                    graph.nodes[neighbor]['Dv'] = delta
                    graph.nodes[neighbor]['V'] = graph.nodes[current_node]['V']
                    heapq.heappush(queue, (delta, neighbor))
                elif delta < graph.nodes[neighbor]['Dv']:
                    graph.nodes[neighbor]['V'] = graph.nodes[current_node]['V']
                    graph.nodes[neighbor]['Dv'] = delta
    return graph, tags
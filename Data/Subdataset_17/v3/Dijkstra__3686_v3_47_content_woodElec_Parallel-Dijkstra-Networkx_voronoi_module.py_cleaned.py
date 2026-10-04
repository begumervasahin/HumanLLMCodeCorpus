import networkx as nx
import heapq
def parallel_dijkstra(graph, sources, mode):
    nx.set_node_attributes(graph, float('inf'), 'Dv')
    nx.set_node_attributes(graph, 'N', 'V')
    nx.set_node_attributes(graph, 0, 'visit')
    priority_queue = []
    tags = []
    for i, source in enumerate(sources):
        if source in graph:
            graph.nodes[source]['Dv'] = 0
            graph.nodes[source]['V'] = f'V{i}'
            tags.append(f'V{i}')
            heapq.heappush(priority_queue, (0, source))
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        graph.nodes[current_node]['visit'] = 1
        neighbors = get_neighbors(graph, current_node, mode)
        for neighbor in neighbors:
            edge_data = graph.get_edge_data(current_node, neighbor)
            weight = edge_data.get('weight', float('inf'))
            new_distance = current_distance + weight
            if new_distance < graph.nodes[neighbor]['Dv']:
                graph.nodes[neighbor]['Dv'] = new_distance
                graph.nodes[neighbor]['V'] = graph.nodes[current_node]['V']
                heapq.heappush(priority_queue, (new_distance, neighbor))
    return graph, tags
def get_neighbors(graph, node, mode):
    if mode == 1:
        return list(graph.neighbors(node))
    elif mode == 2:
        return list(graph.predecessors(node))
    else:
        raise ValueError("Invalid mode. Use 1 for undirected or 2 for directed.")
if __name__ == "__main__":
    G = nx.DiGraph()
    G.add_weighted_edges_from([(1, 2, 4), (1, 3, 1), (2, 3, 2), (3, 4, 5)])
    sources = [1]
    mode = 2
    updated_graph, tags = parallel_dijkstra(G, sources, mode)
    print("Node labels and distances:")
    for node, data in updated_graph.nodes(data=True):
        print(f"Node {node}: {data}")
    print("Tags:", tags)
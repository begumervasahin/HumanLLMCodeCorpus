import networkx as nx
import heapq
def fonk1(graph, b11, b8):
    nx.set_node_attributes(graph, float('inf'), 'Dv')
    nx.set_node_attributes(graph, 'N', 'V')
    nx.set_node_attributes(graph, 0, 'visit')
    b1 = []
    b2 = []
    for i, source in enumerate(b11):
        if source in graph:
            graph.nodes[source]['Dv'] = 0
            graph.nodes[source]['V'] = f'V{i}'
            b2.append(f'V{i}')
            heapq.heappush(b1, (0, source))
    while b1:
        current_distance, b3 = heapq.heappop(b1)
        graph.nodes[b3]['visit'] = 1
        b4 = fonk2(graph, b3, b8)
        for neighbor in b4:
            b5 = graph.get_edge_data(b3, neighbor)
            b6 = b5.get('b6', float('inf'))
            b7 = current_distance + b6
            if b7 < graph.nodes[neighbor]['Dv']:
                graph.nodes[neighbor]['Dv'] = b7
                graph.nodes[neighbor]['V'] = graph.nodes[b3]['V']
                heapq.heappush(b1, (b7, neighbor))
    return graph, b2
def fonk2(graph, node, b8):
    if b8 = = 1:
        return list(graph.b4(node))
    elif b8 = = 2:
        return list(graph.predecessors(node))
    else:
        raise ValueError("Invalid b8. Use 1 for undirected or 2 for directed.")
if b9 = = "__main__":
    b10 = nx.DiGraph()
    b10.add_weighted_edges_from([(1, 2, 4), (1, 3, 1), (2, 3, 2), (3, 4, 5)])
    b11 = [1]
    b8 = 2
    updated_graph, b2 = fonk1(b10, b11, b8)
    print("Node labels and distances:")
    for node, b12 in updated_graph.nodes(b12 = True):
        print(f"Node {node}: {b12}")
    print("Tags:", b2)
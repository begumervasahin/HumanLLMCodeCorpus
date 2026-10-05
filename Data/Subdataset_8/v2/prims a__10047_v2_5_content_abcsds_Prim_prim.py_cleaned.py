import networkx as nx
from pqdict import PQDict
def prim_minimum_spanning_tree(graph, start_node):
    num_nodes = graph.number_of_nodes()
    num_edges_to_visit = num_nodes - 1
    current_node = start_node
    visited_nodes = set()
    edge_priority_queue = PQDict()
    mst_edges = []
    while len(mst_edges) < num_edges_to_visit:
        for neighbor_node in graph.neighbors(current_node):
            if neighbor_node not in visited_nodes and current_node not in visited_nodes:
                if (current_node, neighbor_node) not in edge_priority_queue and \
                   (neighbor_node, current_node) not in edge_priority_queue:
                    weight = graph.edges[current_node, neighbor_node]['weight']
                    edge_priority_queue.additem((current_node, neighbor_node), weight)
        visited_nodes.add(current_node)
        edge, weight = edge_priority_queue.popitem()
        while edge[1] in visited_nodes:
            edge, weight = edge_priority_queue.popitem()
        mst_edges.append(edge)
        current_node = edge[1]
    return mst_edges
graph = nx.Graph()
graph.add_weighted_edges_from([(0, 1, 4), (0, 2, 8), (1, 2, 2), (1, 3, 6), (2, 3, 3)])
mst = prim_minimum_spanning_tree(graph, 0)
print("Minimum Spanning Tree:", mst)
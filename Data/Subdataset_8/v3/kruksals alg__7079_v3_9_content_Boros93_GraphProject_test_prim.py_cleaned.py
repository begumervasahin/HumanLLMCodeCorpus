import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim
def build_priority_queue(vertices, keys, heap):
    nodes_heap = {}
    for vertex in vertices:
        nodes_heap[vertex] = heap.insert(keys[vertex], vertex)
    return nodes_heap
graph = nx.Graph()
node_set = ('a', 'b', 'c', 'd')
nodes_info = {
    'a': {'pos': (0, 1), 'key': 0},
    'b': {'pos': (2, 1), 'key': 0},
    'c': {'pos': (1, 0), 'key': 0},
    'd': {'pos': (1, 2), 'key': 0}
}
edges_info = {
    ('a', 'b'): {'weight': 2},
    ('a', 'c'): {'weight': 30},
    ('b', 'c'): {'weight': 90},
    ('d', 'b'): {'weight': 1},
    ('d', 'a'): {'weight': 3}
}
graph.add_nodes_from(nodes_info.keys())
graph.add_edges_from(edges_info.keys())
nx.set_node_attributes(graph, nodes_info)
nx.set_edge_attributes(graph, edges_info, 'weight')
weights = nx.get_edge_attributes(graph, 'weight')
positions = nx.get_node_attributes(graph, 'pos')
edges = graph.edges
source_node = 'a'
minimum_spanning_tree = prim(graph, weights, source_node, node_set)
mst_edges = minimum_spanning_tree.edges()
mst_weights = nx.get_edge_attributes(minimum_spanning_tree, 'weight')
plt.subplot(121)
nx.draw(graph, positions, with_labels=True, edge_labels=weights)
plt.title('Original Graph')
plt.subplot(122)
nx.draw(minimum_spanning_tree, positions, with_labels=True, edge_labels=mst_weights)
plt.title('Minimum Spanning Tree (MST)')
plt.tight_layout()
plt.show()
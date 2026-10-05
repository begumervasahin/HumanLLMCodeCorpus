import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim
def build_heap(vertices, keys, heap):
    node_heap = {}
    for vertex in vertices:
        node_heap[vertex] = heap.insert(keys[vertex], vertex)
    return node_heap
G = nx.Graph()
node_set = ('a', 'b', 'c', 'd')
node_positions = {
    'a': (0, 1),
    'b': (2, 1),
    'c': (1, 0),
    'd': (1, 2)
}
for node, pos in node_positions.items():
    G.add_node(node, pos=pos, key=0)
edges_data = [('a', 'b', 2), ('a', 'c', 30), ('b', 'c', 90), ('d', 'b', 1), ('d', 'a', 3)]
G.add_weighted_edges_from(edges_data)
edge_weights = nx.get_edge_attributes(G, 'weight')
node_positions = nx.get_node_attributes(G, 'pos')
edges = G.edges
start_node = 'a'
MST = prim(G, edge_weights, start_node, node_set)
edges_MST = MST.edges()
weights_MST = nx.get_edge_attributes(MST, 'weight')
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
nx.draw(G, node_positions, with_labels=True, ax=axes[0])
nx.draw_networkx_edge_labels(G, node_positions, edge_labels=edge_weights, ax=axes[0])
nx.draw(G, node_positions, edges=edges, ax=axes[0])
axes[0].set_title('Original Graph')
nx.draw(MST, node_positions, with_labels=True, ax=axes[1])
nx.draw_networkx_edge_labels(MST, node_positions, edge_labels=weights_MST, ax=axes[1])
nx.draw(MST, node_positions, edges=edges_MST, ax=axes[1])
axes[1].set_title('Minimum Spanning Tree (MST)')
plt.tight_layout()
plt.show()
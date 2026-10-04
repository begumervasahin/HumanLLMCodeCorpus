import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim
def build_heap(vertices, keys, heap):
    nodes_heap = {}
    for vertex in vertices:
        nodes_heap[vertex] = heap.insert(keys[vertex], vertex)
    return nodes_heap
G = nx.Graph()
nodes = {
    'a': (0, 1),
    'b': (2, 1),
    'c': (1, 0),
    'd': (1, 2)
}
for node, position in nodes.items():
    G.add_node(node, pos=position, key=0)
edges = [
    ('a', 'b', 2),
    ('a', 'c', 30),
    ('b', 'c', 90),
    ('d', 'b', 1),
    ('d', 'a', 3)
]
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])
edge_weights = nx.get_edge_attributes(G, 'weight')
node_positions = nx.get_node_attributes(G, 'pos')
start_node = 'a'
node_set = set(nodes.keys())
MST = prim(G, edge_weights, start_node, node_set)
mst_edges = MST.edges()
mst_edge_weights = nx.get_edge_attributes(MST, 'weight')
plt.figure(figsize=(12, 6))
plt.subplot(121)
nx.draw(G, pos=node_positions, with_labels=True)
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_weights)
plt.title("Original Graph")
plt.subplot(122)
nx.draw(MST, pos=node_positions, with_labels=True)
nx.draw_networkx_edge_labels(MST, pos=node_positions, edge_labels=mst_edge_weights)
plt.title("Minimum Spanning Tree (MST)")
plt.show()
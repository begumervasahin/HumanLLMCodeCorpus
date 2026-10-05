import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim
def build_heap(V, k, heap):
    nodes_heap = {}
    for v in V:
        nodes_heap[v] = heap.insert(k[v], v)
    return nodes_heap
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
G.add_edge('a', 'b', weight=2)
G.add_edge('a', 'c', weight=30)
G.add_edge('b', 'c', weight=90)
G.add_edge('d', 'b', weight=1)
G.add_edge('d', 'a', weight=3)
edge_weights = nx.get_edge_attributes(G, 'weight')
node_positions = nx.get_node_attributes(G, 'pos')
edges = G.edges
start_node = 'a'
MST = prim(G, edge_weights, start_node, node_set)
edges_MST = MST.edges()
weights_MST = nx.get_edge_attributes(MST, 'weight')
plt.subplot(121)
nx.draw(G, node_positions, with_labels=True)
nx.draw_networkx_edge_labels(G, node_positions, edge_labels=edge_weights)
nx.draw(G, node_positions, edges=edges)
plt.subplot(122)
nx.draw(MST, node_positions, with_labels=True)
nx.draw_networkx_edge_labels(MST, node_positions, edge_labels=weights_MST)
nx.draw(MST, node_positions, edges=edges_MST)
plt.show()
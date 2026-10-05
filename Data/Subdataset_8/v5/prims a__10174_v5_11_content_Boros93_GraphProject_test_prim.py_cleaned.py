import networkx as nx
import matplotlib.pyplot as plt
from prim_algorithm import prim
def build_heap(V, k, heap):
    nodes_heap = {}
    for v in V:
        nodes_heap[v] = heap.insert(k[v], v)
    return nodes_heap
G = nx.Graph()
node_set = ('a', 'b', 'c', 'd')
nodes_info = {
    'a': {'pos': (0, 1), 'key': 0},
    'b': {'pos': (2, 1), 'key': 0},
    'c': {'pos': (1, 0), 'key': 0},
    'd': {'pos': (1, 2), 'key': 0}
}
G.add_nodes_from(nodes_info.items())
edge_info = {
    ('a', 'b'): {'weight': 2},
    ('a', 'c'): {'weight': 30},
    ('b', 'c'): {'weight': 90},
    ('d', 'b'): {'weight': 1},
    ('d', 'a'): {'weight': 3}
}
G.add_edges_from(edge_info.items())
weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
edges = G.edges
start_node = 'a'
MST = prim(G, weight, start_node, node_set)
edges_MST = MST.edges()
weight_MST = nx.get_edge_attributes(MST, 'weight')
plt.subplot(121)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
nx.draw(G, pos, edges=edges)
plt.subplot(122)
nx.draw(MST, pos, with_labels=True)
nx.draw_networkx_edge_labels(MST, pos, edge_labels=weight_MST)
nx.draw(MST, pos, edges=edges_MST)
plt.show()
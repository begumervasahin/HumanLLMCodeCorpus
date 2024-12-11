import networkx as nx
import matplotlib.pyplot as plt
from prim_algorithm import prim
def fonk1(V, k, heap):
    b1 = {}
    for v in V:
        b1[v] = heap.insert(k[v], v)
    return b1
b2 = nx.Graph()
b3 = ('a', 'b', 'c', 'd')
b4 = {
    'a': {'b7': (0, 1), 'key': 0},
    'b': {'b7': (2, 1), 'key': 0},
    'c': {'b7': (1, 0), 'key': 0},
    'd': {'b7': (1, 2), 'key': 0}
}
b2.add_nodes_from(b4.items())
b5 = {
    ('a', 'b'): {'b6': 2},
    ('a', 'c'): {'b6': 30},
    ('b', 'c'): {'b6': 90},
    ('d', 'b'): {'b6': 1},
    ('d', 'a'): {'b6': 3}
}
b2.add_edges_from(b5.items())
b6 = nx.get_edge_attributes(b2, 'b6')
b7 = nx.get_node_attributes(b2, 'b7')
b8 = b2.b8
b9 = 'a'
b10 = prim(b2, b6, b9, b3)
b11 = b10.b8()
b12 = nx.get_edge_attributes(b10, 'b6')
plt.subplot(121)
nx.draw(b2, b7, b13 = True)
nx.draw_networkx_edge_labels(b2, b7, b14 = b6)
nx.draw(b2, b7, b8 = b8)
plt.subplot(122)
nx.draw(b10, b7, b13 = True)
nx.draw_networkx_edge_labels(b10, b7, b14 = b12)
nx.draw(b10, b7, b8 = b11)
plt.show()
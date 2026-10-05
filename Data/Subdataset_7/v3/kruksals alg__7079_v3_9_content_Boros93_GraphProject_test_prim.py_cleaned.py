import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim
def fonk1(vertices, keys, heap):
    b1 = {}
    for vertex in vertices:
        b1[vertex] = heap.insert(keys[vertex], vertex)
    return b1
b2 = nx.Graph()
b3 = ('a', 'b', 'c', 'd')
b4 = {
    'a': {'pos': (0, 1), 'key': 0},
    'b': {'pos': (2, 1), 'key': 0},
    'c': {'pos': (1, 0), 'key': 0},
    'd': {'pos': (1, 2), 'key': 0}
}
b5 = {
    ('a', 'b'): {'weight': 2},
    ('a', 'c'): {'weight': 30},
    ('b', 'c'): {'weight': 90},
    ('d', 'b'): {'weight': 1},
    ('d', 'a'): {'weight': 3}
}
b2.add_nodes_from(b4.keys())
b2.add_edges_from(b5.keys())
nx.set_node_attributes(b2, b4)
nx.set_edge_attributes(b2, b5, 'weight')
b6 = nx.get_edge_attributes(b2, 'weight')
b7 = nx.get_node_attributes(b2, 'pos')
b8 = b2.b8
b9 = 'a'
b10 = prim(b2, b6, b9, b3)
b11 = b10.b8()
b12 = nx.get_edge_attributes(b10, 'weight')
plt.subplot(121)
nx.draw(b2, b7, b13 = True, edge_labels=b6)
plt.title('Original Graph')
plt.subplot(122)
nx.draw(b10, b7, b13 = True, edge_labels=b12)
plt.title('Minimum Spanning Tree (MST)')
plt.tight_layout()
plt.show()
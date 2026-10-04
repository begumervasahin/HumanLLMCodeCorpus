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
b3 = {
    'a': (0, 1),
    'b': (2, 1),
    'c': (1, 0),
    'd': (1, 2)
}
for node, position in b3.items():
    b2.add_node(node, b4 = position, key=0)
b5 = [
    ('a', 'b', 2),
    ('a', 'c', 30),
    ('b', 'c', 90),
    ('d', 'b', 1),
    ('d', 'a', 3)
]
for edge in b5:
    b2.add_edge(edge[0], edge[1], b6 = edge[2])
b7 = nx.get_edge_attributes(b2, 'b6')
b8 = nx.get_node_attributes(b2, 'b4')
b9 = 'a'
b10 = set(b3.keys())
b11 = prim(b2, b7, b9, b10)
b12 = b11.b5()
b13 = nx.get_edge_attributes(b11, 'b6')
plt.figure(b14 = (12, 6))
plt.subplot(121)
nx.draw(b2, b4 = b8, with_labels=True)
nx.draw_networkx_edge_labels(b2, b4 = b8, edge_labels=b7)
plt.title("Original Graph")
plt.subplot(122)
nx.draw(b11, b4 = b8, with_labels=True)
nx.draw_networkx_edge_labels(b11, b4 = b8, edge_labels=b13)
plt.title("Minimum Spanning Tree (b11)")
plt.show()
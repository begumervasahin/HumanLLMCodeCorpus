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
    'a': (0, 1),
    'b': (2, 1),
    'c': (1, 0),
    'd': (1, 2)
}
for node, b5 in b4.items():
    b2.add_node(node, b5 = b5, key=0)
b6 = [('a', 'b', 2), ('a', 'c', 30), ('b', 'c', 90), ('d', 'b', 1), ('d', 'a', 3)]
b2.add_weighted_edges_from(b6)
b7 = nx.get_edge_attributes(b2, 'weight')
b4 = nx.get_node_attributes(b2, 'b5')
b8 = b2.b8
b9 = 'a'
b10 = prim(b2, b7, b9, b3)
b11 = b10.b8()
b12 = nx.get_edge_attributes(b10, 'weight')
fig, b13 = plt.subplots(1, 2, figsize=(12, 6))
nx.draw(b2, b4, b14 = True, ax=b13[0])
nx.draw_networkx_edge_labels(b2, b4, b15 = b7, ax=b13[0])
nx.draw(b2, b4, b8 = b8, ax=b13[0])
b13[0].set_title('Original Graph')
nx.draw(b10, b4, b14 = True, ax=b13[1])
nx.draw_networkx_edge_labels(b10, b4, b15 = b12, ax=b13[1])
nx.draw(b10, b4, b8 = b11, ax=b13[1])
b13[1].set_title('Minimum Spanning Tree (b10)')
plt.tight_layout()
plt.show()
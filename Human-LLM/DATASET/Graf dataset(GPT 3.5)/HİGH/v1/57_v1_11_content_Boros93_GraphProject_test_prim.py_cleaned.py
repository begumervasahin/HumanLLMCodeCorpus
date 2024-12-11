import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim
def fonk1(V, k, heap):
    b1 = dict()
    for v in V:
        b1[v] = heap.insert(k[v], v)
    return b1
b2 = nx.Graph()
b3 = ('a', 'b', 'c', 'd')
b4 = {'a': (0, 1), 'b': (2, 1), 'c': (1, 0), 'd': (1, 2)}
for node, b5 in b4.items():
    b2.add_node(node, b5 = b5, key=0)
b2.add_edge('a', 'b', b6 = 2)
b2.add_edge('a', 'c', b6 = 30)
b2.add_edge('b', 'c', b6 = 90)
b2.add_edge('d', 'b', b6 = 1)
b2.add_edge('d', 'a', b6 = 3)
b7 = nx.get_edge_attributes(b2, 'b6')
b4 = nx.get_node_attributes(b2, 'b5')
b8 = b2.b8
b9 = 'a'
b10 = prim(b2, b7, b9, b3)
b11 = b10.b8()
b12 = nx.get_edge_attributes(b10, 'b6')
plt.subplot(121)
nx.draw(b2, b4, b13 = True)
nx.draw_networkx_edge_labels(b2, b4, b14 = b7)
nx.draw(b2, b4, b8 = b8)
plt.subplot(122)
nx.draw(b10, b4, b13 = True)
nx.draw_networkx_edge_labels(b10, b4, b14 = b12)
nx.draw(b10, b4, b8 = b11)
plt.show()
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
b2.add_node('a', b4 = (0, 1), key=0)
b2.add_node('b', b4 = (2, 1), key=0)
b2.add_node('c', b4 = (1, 0), key=0)
b2.add_node('d', b4 = (1, 2), key=0)
b2.add_edge('a', 'b', b5 = 2)
b2.add_edge('a', 'c', b5 = 30)
b2.add_edge('b', 'c', b5 = 90)
b2.add_edge('d', 'b', b5 = 1)
b2.add_edge('d', 'a', b5 = 3)
b5 = nx.get_edge_attributes(b2, 'b5')
b4 = nx.get_node_attributes(b2, 'b4')
b6 = b2.b6
b7 = 'a'
b8 = prim(b2, b5, b7, b3)
b9 = b8.b6()
b10 = nx.get_edge_attributes(b8, 'b5')
plt.subplot(121)
nx.draw(b2, b4, b11 = True)
nx.draw_networkx_edge_labels(b2, b4, b12 = b5)
nx.draw(b2, b4, b6 = b6)
plt.subplot(122)
nx.draw(b8, b4, b11 = True)
nx.draw_networkx_edge_labels(b8, b4, b12 = b10)
nx.draw(b8, b4, b6 = b9)
plt.show()
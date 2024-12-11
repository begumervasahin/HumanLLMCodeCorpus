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
b2.add_node('a', b4 = (0, 1), key=0)
b2.add_node('b', b4 = (2, 1), key=0)
b2.add_node('c', b4 = (1, 0), key=0)
b2.add_node('d', b4 = (1, 2), key=0)
b2.add_edge('a', 'b', b5 = 2)
b2.add_edge('a', 'c', b5 = 30)
b2.add_edge('b', 'c', b5 = 90)
b2.add_edge('d', 'b', b5 = 1)
b2.add_edge('d', 'a', b5 = 3)
b6 = nx.get_edge_attributes(b2, 'b5')
b7 = nx.get_node_attributes(b2, 'b4')
b8 = b2.b8
b9 = 'a'
b10 = prim(b2, b6, b9, b3)
b11 = b10.b8()
b12 = nx.get_edge_attributes(b10, 'b5')
plt.subplot(121)
nx.draw(b2, b7, b13 = True)
nx.draw_networkx_edge_labels(b2, b7, b14 = b6)
nx.draw(b2, b7, b8 = b8)
plt.subplot(122)
nx.draw(b10, b7, b13 = True)
nx.draw_networkx_edge_labels(b10, b7, b14 = b12)
nx.draw(b10, b7, b8 = b11)
plt.show()
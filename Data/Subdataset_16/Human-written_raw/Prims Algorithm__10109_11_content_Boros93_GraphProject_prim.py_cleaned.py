import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
def fonk1(V, k, heap):
    b1 = dict()
    for b14 in V:
        b1[b14] = heap.insert(k[b14], b14)
    return b1
b2 = nx.Graph()
b3 = ('a', 'b', 'c', 'd')
a1 = 0
a2 = 2
for n in b3:
    b2.add_node(n[0], b4 = (a1, a2), key= 0)
    a2 = a2-a1
    a1 = a1+1
b2.add_edge('a', 'b', b5 = 2)
b2.add_edge('a', 'c', b5 = 10)
b2.add_edge('b', 'c', b5 = 9)
b2.add_edge('b', 'd', b5 = 1)
b2.add_edge('d', 'a', b5 = 3)
b5 = nx.get_edge_attributes(b2, 'b5')
b4 = nx.get_node_attributes(b2, 'b4')
b6 = b2.b6
nx.draw(b2, b4, b6 = b6, b17='true')
nx.draw_networkx_edge_labels(b2, b4, b7 = b6)
b8 = 'a'
for b14 in b3:
    b2.node[b14]['key'] = math.inf
    b2.node[b14]['pred'] = ''
    b2.node[b14]['flag'] = False
b2.node[b8]['key'] = 0
b9 = FibonacciHeap()
b10 = nx.get_node_attributes(b2, 'key')
b1 = fonk1(b3, b10, b9)
while b9.total_nodes != 0:
    b11 = b9.extract_min().value
    b12 = nx.all_neighbors(b2, b11)
    for b14 in b12:
        if not(b2.node[b14]['flag']) and b5[b11, b14] < b2.node[b14]['key']:
            b9.decrease_key(b1[b14], b5[b11, b14])
            b2.node[b14]['pred'] = b11
    b2.node[b11]['flag'] = True
b13 = nx.Graph()
for b14 in b3:
    if(b14 = = b8):
        b13.add_node(b14)
        continue
    b13.add_edge(b2.node[b14]['pred'], b14, b5 = b5[b2.node[b14]['pred'], b14])
b15 = b13.b6()
b16 = b5 = nx.get_edge_attributes(b13, 'b5')
plt.subplot(121)
nx.draw(b2, b4, b17 = True)
nx.draw_networkx_edge_labels(b2, b4, b7 = b5)
plt.subplot(122)
nx.draw(b13, b4, b17 = True)
nx.draw_networkx_edge_labels(b13, b4, b7 = b16)
nx.draw(b13, b4, b6 = b15)
plt.show()
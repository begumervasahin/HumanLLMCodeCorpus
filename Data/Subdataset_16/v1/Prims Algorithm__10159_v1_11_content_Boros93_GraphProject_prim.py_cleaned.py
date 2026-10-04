import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
def fonk1(V, k, heap):
    b1 = dict()
    for b15 in V:
        b1[b15] = heap.insert(k[b15], b15)
    return b1
b2 = nx.Graph()
b3 = ('a', 'b', 'c', 'd')
a1 = 0
a2 = 2
for n in b3:
    b2.add_node(n, b4 = (a1, a2), key=0)
    a2 = a2 - a1
    a1 = a1 + 1
b2.add_edge('a', 'b', b5 = 2)
b2.add_edge('a', 'c', b5 = 10)
b2.add_edge('b', 'c', b5 = 9)
b2.add_edge('b', 'd', b5 = 1)
b2.add_edge('d', 'a', b5 = 3)
b5 = nx.get_edge_attributes(b2, 'b5')
b4 = nx.get_node_attributes(b2, 'b4')
b6 = b2.b6
plt.figure(b7 = (12, 6))
plt.subplot(121)
nx.draw(b2, b4, b6 = b6, b18=True)
nx.draw_networkx_edge_labels(b2, b4, b8 = b5)
b9 = 'a'
for b15 in b3:
    b2.nodes[b15]['key'] = math.inf
    b2.nodes[b15]['pred'] = ''
    b2.nodes[b15]['flag'] = False
b2.nodes[b9]['key'] = 0
b10 = FibonacciHeap()
b11 = nx.get_node_attributes(b2, 'key')
b1 = fonk1(b3, b11, b10)
while b10.total_nodes != 0:
    b12 = b10.extract_min().value
    b13 = nx.all_neighbors(b2, b12)
    for b15 in b13:
        if not b2.nodes[b15]['flag'] and b5[b12, b15] < b2.nodes[b15]['key']:
            b10.decrease_key(b1[b15], b5[b12, b15])
            b2.nodes[b15]['pred'] = b12
    b2.nodes[b12]['flag'] = True
b14 = nx.Graph()
for b15 in b3:
    if b15 = = b9:
        b14.add_node(b15)
        continue
    b14.add_edge(b2.nodes[b15]['pred'], b15, b5 = b5[b2.nodes[b15]['pred'], b15])
b16 = b14.b6()
b17 = nx.get_edge_attributes(b14, 'b5')
plt.subplot(122)
nx.draw(b14, b4, b18 = True)
nx.draw_networkx_edge_labels(b14, b4, b8 = b17)
nx.draw(b14, b4, b6 = b16)
plt.show()
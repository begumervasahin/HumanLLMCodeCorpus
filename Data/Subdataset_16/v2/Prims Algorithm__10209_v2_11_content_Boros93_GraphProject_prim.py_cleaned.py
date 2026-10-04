import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
def fonk1(V, k, heap):
    b1 = {v: heap.insert(k[v], v) for v in V}
    return b1
b2 = nx.Graph()
b3 = ['a', 'b', 'c', 'd']
b4 = [(0, 2), (1, 2), (2, 0), (3, -2)]
for n, b5 in zip(b3, b4):
    b2.add_node(n, b5 = b5, key=0)
b6 = [('a', 'b', 2), ('a', 'c', 10), ('b', 'c', 9), ('b', 'd', 1), ('d', 'a', 3)]
b2.add_weighted_edges_from(b6)
b7 = nx.get_edge_attributes(b2, 'b7')
b5 = nx.get_node_attributes(b2, 'b5')
plt.figure(b8 = (12, 6))
plt.subplot(121)
nx.draw(b2, b5, b9 = True)
nx.draw_networkx_edge_labels(b2, b5, b10 = b7)
b11 = 'a'
for v in b3:
    b2.nodes[v]['key'] = math.inf
    b2.nodes[v]['pred'] = None
    b2.nodes[v]['flag'] = False
b2.nodes[b11]['key'] = 0
b12 = FibonacciHeap()
b13 = nx.get_node_attributes(b2, 'key')
b1 = fonk1(b3, b13, b12)
while b12.total_nodes != 0:
    b14 = b12.extract_min().value
    b2.nodes[b14]['flag'] = True
    for v in b2.neighbors(b14):
        if not b2.nodes[v]['flag'] and b2[b14][v]['b7'] < b2.nodes[v]['key']:
            b2.nodes[v]['key'] = b2[b14][v]['b7']
            b2.nodes[v]['pred'] = b14
            b12.decrease_key(b1[v], b2[b14][v]['b7'])
b15 = nx.Graph()
for v in b3:
    if b2.nodes[v]['pred'] is not None:
        b15.add_edge(b2.nodes[v]['pred'], v, b7 = b2.nodes[v]['key'])
b16 = nx.get_edge_attributes(b15, 'b7')
plt.subplot(122)
nx.draw(b15, b5, b9 = True)
nx.draw_networkx_edge_labels(b15, b5, b10 = b16)
plt.show()
import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
def fonk1(V, k, heap):
    b1 = dict()
    for v in V:
        b1[v] = heap.insert(k[v], v)
    return b1
b2 = nx.Graph()
b3 = ('a', 'b', 'c', 'd')
b4 = {'a': (0, 2), 'b': (1, 0), 'c': (2, 2), 'd': (3, 0)}
for node in b3:
    b2.add_node(node, b5 = b4[node], key=math.inf, pred=None, flag=False)
b6 = [
    ('a', 'b', 2),
    ('a', 'c', 10),
    ('b', 'c', 9),
    ('b', 'd', 1),
    ('d', 'a', 3)
]
b2.add_weighted_edges_from(b6)
b7 = nx.get_edge_attributes(b2, 'b16')
b4 = nx.get_node_attributes(b2, 'b5')
plt.figure(b8 = (12, 6))
plt.subplot(121)
nx.draw(b2, b4, b9 = True, node_color='lightblue', node_size=500)
nx.draw_networkx_edge_labels(b2, b4, b10 = b7)
b11 = 'a'
b2.nodes[b11]['key'] = 0
b12 = FibonacciHeap()
b13 = nx.get_node_attributes(b2, 'key')
b1 = fonk1(b3, b13, b12)
while b12.total_nodes != 0:
    b14 = b12.extract_min().value
    b2.nodes[b14]['flag'] = True
    for v in b2.neighbors(b14):
        if not b2.nodes[v]['flag'] and b2[b14][v]['b16'] < b2.nodes[v]['key']:
            b2.nodes[v]['key'] = b2[b14][v]['b16']
            b2.nodes[v]['pred'] = b14
            b12.decrease_key(b1[v], b2[b14][v]['b16'])
b15 = nx.Graph()
for v in b3:
    if b2.nodes[v]['pred'] is not None:
        b15.add_edge(b2.nodes[v]['pred'], v, b16 = b2[v][b2.nodes[v]['pred']]['b16'])
b17 = nx.get_edge_attributes(b15, 'b16')
plt.subplot(122)
nx.draw(b15, b4, b9 = True, node_color='lightgreen', node_size=500)
nx.draw_networkx_edge_labels(b15, b4, b10 = b17)
plt.title('Minimum Spanning Tree')
plt.show()
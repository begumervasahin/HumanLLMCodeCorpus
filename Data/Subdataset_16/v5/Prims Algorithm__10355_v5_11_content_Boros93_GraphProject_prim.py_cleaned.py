import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
def fonk1(nodes, b9, b8):
    b1 = {}
    for node in nodes:
        b1[node] = b8.insert(b9[node], node)
    return b1
def fonk2():
    b2 = nx.Graph()
    b3 = {
        'a': (0, 2),
        'b': (1, 0),
        'c': (2, 2),
        'd': (3, 0)
    }
    for node, b4 in b3.items():
        b2.add_node(node, b4 = b4, key=math.inf, b12=None, flag=False)
    b5 = [
        ('a', 'b', 2),
        ('a', 'c', 10),
        ('b', 'c', 9),
        ('b', 'd', 1),
        ('d', 'a', 3)
    ]
    b2.add_weighted_edges_from(b5)
    return b2
def fonk3(b2, b4, subplot_index, title):
    plt.subplot(subplot_index)
    nx.draw(b2, b4, b6 = True, node_color='lightblue', node_size=500)
    b7 = nx.get_edge_attributes(b2, 'b13')
    nx.draw_networkx_edge_labels(b2, b4, b7 = b7)
    plt.title(title)
def fonk4(b2, b16):
    b2.nodes[b16]['key'] = 0
    b8 = FibonacciHeap()
    b9 = nx.get_node_attributes(b2, 'key')
    b1 = fonk1(b2.nodes, b9, b8)
    while b8.total_nodes != 0:
        b10 = b8.extract_min().value
        b2.nodes[b10]['flag'] = True
        for v in b2.neighbors(b10):
            if not b2.nodes[v]['flag'] and b2[b10][v]['b13'] < b2.nodes[v]['key']:
                b2.nodes[v]['key'] = b2[b10][v]['b13']
                b2.nodes[v]['b12'] = b10
                b8.decrease_key(b1[v], b2[b10][v]['b13'])
    b11 = nx.Graph()
    for node in b2.nodes:
        b12 = b2.nodes[node]['b12']
        if b12 is not None:
            b11.add_edge(b12, node, b13 = b2[b12][node]['b13'])
    return b11
b2 = fonk2()
b14 = nx.get_node_attributes(b2, 'b4')
plt.figure(b15 = (12, 6))
fonk3(b2, b14, 121, 'Initial Graph')
b16 = 'a'
b11 = fonk4(b2, b16)
fonk3(b11, b14, 122, 'Minimum Spanning Tree')
plt.show()
import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
def fonk1(nodes, b9, heap):
    return {node: heap.insert(b9[node], node) for node in nodes}
def fonk2():
    b1 = nx.Graph()
    b2 = ['a', 'b', 'c', 'd']
    b3 = [(0, 2), (1, 2), (2, 0), (3, -2)]
    for node, b4 in zip(b2, b3):
        b1.add_node(node, b4 = b4, key=0)
    b5 = [
        ('a', 'b', 2),
        ('a', 'c', 10),
        ('b', 'c', 9),
        ('b', 'd', 1),
        ('d', 'a', 3)
    ]
    b1.add_weighted_edges_from(b5)
    return b1, b2
def fonk3(b1, b17):
    for node in b1.nodes:
        b1.nodes[node]['key'] = math.inf
        b1.nodes[node]['pred'] = None
        b1.nodes[node]['flag'] = False
    b1.nodes[b17]['key'] = 0
def fonk4(b1, b4, subplot_index, title, b6 = None):
    plt.subplot(subplot_index)
    nx.draw(b1, b4, b7 = True)
    if b6:
        nx.draw_networkx_edge_labels(b1, b4, b6 = b6)
    plt.title(title)
def fonk5(b1, b17):
    b8 = FibonacciHeap()
    b9 = nx.get_node_attributes(b1, 'key')
    b10 = fonk1(b1.nodes, b9, b8)
    while b8.total_nodes != 0:
        b11 = b8.extract_min().value
        b1.nodes[b11]['flag'] = True
        for v in b1.neighbors(b11):
            if not b1.nodes[v]['flag'] and b1[b11][v]['b13'] < b1.nodes[v]['key']:
                b1.nodes[v]['key'] = b1[b11][v]['b13']
                b1.nodes[v]['pred'] = b11
                b8.decrease_key(b10[v], b1[b11][v]['b13'])
def fonk6(b1, b2):
    b12 = nx.Graph()
    for v in b2:
        if b1.nodes[v]['pred'] is not None:
            b12.add_edge(b1.nodes[v]['pred'], v, b13 = b1.nodes[v]['key'])
    return b12
if b14 = = "__main__":
    b1, b2 = fonk2()
    b4 = nx.get_node_attributes(b1, 'b4')
    b15 = nx.get_edge_attributes(b1, 'b13')
    plt.figure(b16 = (12, 6))
    fonk4(b1, b4, 121, "Initial Graph", b6 = b15)
    b17 = 'a'
    fonk3(b1, b17)
    fonk5(b1, b17)
    b12 = fonk6(b1, b2)
    b18 = nx.get_edge_attributes(b12, 'b13')
    fonk4(b12, b4, 122, "Minimum Spanning Tree (b12)", b6 = b18)
    plt.show()
w
import networkx as nx
import operator
import matplotlib.pyplot as plt
from b2 import DisjointSet
b1 = nx.Graph()
b2 = DisjointSet(['a', 'b', 'c', 'd'])
b3 = {
    'a': {'b6': (0, 1), 'key': 0},
    'b': {'b6': (2, 1), 'key': 0},
    'c': {'b6': (1, 0), 'key': 0},
    'd': {'b6': (1, 2), 'key': 0}
}
b1.add_nodes_from(b3.items())
b4 = {
    ('a', 'b'): {'b10': 2},
    ('a', 'c'): {'b10': 10},
    ('b', 'c'): {'b10': 90},
    ('b', 'd'): {'b10': 1},
    ('d', 'a'): {'b10': 3}
}
b1.add_edges_from(b4.items())
b5 = nx.get_edge_attributes(b1, 'b10')
b6 = nx.get_node_attributes(b1, 'b6')
b7 = nx.Graph()
b8 = sorted(b5.items(), key=operator.itemgetter(1))
for uv, b10 in b8:
    u, b9 = uv
    if b2.find(u) != b2.find(b9):
        b2.union(u, b9)
        b7.add_edge(u, b9, b10 = b10, color='b')
    else:
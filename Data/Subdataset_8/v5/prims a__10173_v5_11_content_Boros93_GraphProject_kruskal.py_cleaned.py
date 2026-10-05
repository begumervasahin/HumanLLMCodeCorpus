import networkx as nx
import operator
import matplotlib.pyplot as plt
from disjoint_set import DisjointSet
G = nx.Graph()
disjoint_set = DisjointSet(['a', 'b', 'c', 'd'])
nodes_data = {
    'a': {'pos': (0, 1), 'key': 0},
    'b': {'pos': (2, 1), 'key': 0},
    'c': {'pos': (1, 0), 'key': 0},
    'd': {'pos': (1, 2), 'key': 0}
}
G.add_nodes_from(nodes_data.items())
edges_data = {
    ('a', 'b'): {'weight': 2},
    ('a', 'c'): {'weight': 10},
    ('b', 'c'): {'weight': 90},
    ('b', 'd'): {'weight': 1},
    ('d', 'a'): {'weight': 3}
}
G.add_edges_from(edges_data.items())
edges = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
KruskalG = nx.Graph()
sorted_edges = sorted(edges.items(), key=operator.itemgetter(1))
for uv, weight in sorted_edges:
    u, v = uv
    if disjoint_set.find(u) != disjoint_set.find(v):
        disjoint_set.union(u, v)
        KruskalG.add_edge(u, v, weight=weight, color='b')
    else:
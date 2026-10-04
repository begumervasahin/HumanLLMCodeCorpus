import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
def build_heap(V, k, heap):
    nodes_heap = {v: heap.insert(k[v], v) for v in V}
    return nodes_heap
G = nx.Graph()
node_set = ['a', 'b', 'c', 'd']
positions = [(0, 2), (1, 2), (2, 0), (3, -2)]
for n, pos in zip(node_set, positions):
    G.add_node(n, pos=pos, key=0)
edges = [('a', 'b', 2), ('a', 'c', 10), ('b', 'c', 9), ('b', 'd', 1), ('d', 'a', 3)]
G.add_weighted_edges_from(edges)
weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
plt.figure(figsize=(12, 6))
plt.subplot(121)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
source = 'a'
for v in node_set:
    G.nodes[v]['key'] = math.inf
    G.nodes[v]['pred'] = None
    G.nodes[v]['flag'] = False
G.nodes[source]['key'] = 0
Q = FibonacciHeap()
keys = nx.get_node_attributes(G, 'key')
nodes_heap = build_heap(node_set, keys, Q)
while Q.total_nodes != 0:
    u = Q.extract_min().value
    G.nodes[u]['flag'] = True
    for v in G.neighbors(u):
        if not G.nodes[v]['flag'] and G[u][v]['weight'] < G.nodes[v]['key']:
            G.nodes[v]['key'] = G[u][v]['weight']
            G.nodes[v]['pred'] = u
            Q.decrease_key(nodes_heap[v], G[u][v]['weight'])
MST = nx.Graph()
for v in node_set:
    if G.nodes[v]['pred'] is not None:
        MST.add_edge(G.nodes[v]['pred'], v, weight=G.nodes[v]['key'])
weightMST = nx.get_edge_attributes(MST, 'weight')
plt.subplot(122)
nx.draw(MST, pos, with_labels=True)
nx.draw_networkx_edge_labels(MST, pos, edge_labels=weightMST)
plt.show()
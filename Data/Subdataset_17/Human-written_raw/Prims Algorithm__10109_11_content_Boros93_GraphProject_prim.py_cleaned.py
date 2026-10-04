import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
def build_heap(V, k, heap):
    nodes_heap = dict()
    for v in V:
        nodes_heap[v] = heap.insert(k[v], v)
    return nodes_heap
G = nx.Graph()
node_set = ('a', 'b', 'c', 'd')
i = 0
j = 2
for n in node_set:
    G.add_node(n[0], pos=(i, j), key= 0)
    j = j-i
    i = i+1
G.add_edge('a', 'b', weight=2)
G.add_edge('a', 'c', weight=10)
G.add_edge('b', 'c', weight=9)
G.add_edge('b', 'd', weight=1)
G.add_edge('d', 'a', weight=3)
weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
edges = G.edges
nx.draw(G, pos, edges=edges, with_labels='true')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges)
s = 'a'
for v in node_set:
    G.node[v]['key'] = math.inf
    G.node[v]['pred'] = ''
    G.node[v]['flag'] = False
G.node[s]['key'] = 0
Q = FibonacciHeap()
keys = nx.get_node_attributes(G, 'key')
nodes_heap = build_heap(node_set, keys, Q)
while Q.total_nodes != 0:
    u = Q.extract_min().value
    adj = nx.all_neighbors(G, u)
    for v in adj:
        if not(G.node[v]['flag']) and weight[u, v] < G.node[v]['key']:
            Q.decrease_key(nodes_heap[v], weight[u, v])
            G.node[v]['pred'] = u
    G.node[u]['flag'] = True
MST = nx.Graph()
for v in node_set:
    if(v == s):
        MST.add_node(v)
        continue
    MST.add_edge(G.node[v]['pred'], v, weight=weight[G.node[v]['pred'], v])
edgesMST = MST.edges()
weightMST =  weight = nx.get_edge_attributes(MST, 'weight')
plt.subplot(121)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
plt.subplot(122)
nx.draw(MST, pos, with_labels=True)
nx.draw_networkx_edge_labels(MST, pos, edge_labels=weightMST)
nx.draw(MST, pos, edges=edgesMST)
plt.show()
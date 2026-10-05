import networkx as nx
import matplotlib.pyplot as plt
import operator
class DisjointSet:
    def __init__(self, elements):
        self.parent = {x: x for x in elements}
    def find(self, element):
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]
    def union(self, element1, element2):
        self.parent[self.find(element1)] = self.find(element2)
G = nx.Graph()
nodes = ['a', 'b', 'c', 'd']
disjoint_set = DisjointSet(nodes)
node_positions = {'a': (0, 1), 'b': (2, 1), 'c': (1, 0), 'd': (1, 2)}
for node, pos in node_positions.items():
    G.add_node(node, pos=pos, key=0)
edges = [('a', 'b', 2), ('a', 'c', 10), ('b', 'c', 90), ('b', 'd', 1), ('d', 'a', 3)]
for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)
KruskalG = nx.Graph()
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
for u, v, data in sorted_edges:
    if disjoint_set.find(u) != disjoint_set.find(v):
        disjoint_set.union(u, v)
        KruskalG.add_edge(u, v, weight=data['weight'], color='b')
    else:
        KruskalG.add_edge(u, v, weight=data['weight'], color='r')
plt.figure(figsize=(12, 6))
plt.subplot(121)
nx.draw(G, pos=node_positions, with_labels=True)
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels={(u, v): data['weight'] for u, v, data in G.edges(data=True)})
plt.subplot(122)
nx.draw(G, pos=node_positions, with_labels=True)
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels={(u, v): data['weight'] for u, v, data in G.edges(data=True)})
nx.draw(KruskalG, pos=node_positions, edges=KruskalG.edges(), edge_color=[KruskalG[u][v]['color'] for u, v in KruskalG.edges()])
plt.show()
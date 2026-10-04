import networkx as nx
class Algoritimo_kruskal:
    def __init__(self):
        self.graph = None
    def kruskal(self, graph):
        mst = nx.Graph()
        sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
        disjoint_set = DisjointSet()
        for node in graph.nodes():
            disjoint_set.make_set(node)
        for edge in sorted_edges:
            weight, u, v = edge[2]['weight'], edge[0], edge[1]
            if disjoint_set.find(u) != disjoint_set.find(v):
                disjoint_set.union(u, v)
                mst.add_edge(u, v, weight=weight)
        return mst
    def peso(self, mst):
        return sum(weight for u, v, weight in mst.edges.data('weight'))
class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': set([
        (1, 'A', 'B'),
        (5, 'A', 'C'),
        (3, 'A', 'D'),
        (4, 'B', 'C'),
        (2, 'B', 'D'),
        (1, 'C', 'D'),
    ])
}
minimum_spanning_tree = set([
    (1, 'A', 'B'),
    (2, 'B', 'D'),
    (1, 'C', 'D'),
])
grafo = nx.Graph()
grafo.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
grafo.add_edges_from([
    ('A', 'B', {'weight': 1}),
    ('A', 'C', {'weight': 5}),
    ('A', 'D', {'weight': 3}),
    ('B', 'C', {'weight': 4}),
    ('B', 'D', {'weight': 2}),
    ('C', 'D', {'weight': 1}),
])
arvore_minima = nx.Graph()
arvore_minima.add_nodes_from((['A', 'B', 'C', 'D']))
arvore_minima.add_edges_from([
    ('A', 'B', {'weight': 1}),
    ('B', 'D', {'weight': 2}),
    ('C', 'D', {'weight': 1}),
])
grafo2 = nx.Graph()
grafo2.add_weighted_edges_from([
    (1, 2, 4),
    (1, 3, 8),
    (2, 3, 11),
    (2, 4, 8),
    (3, 6, 7),
    (3, 7, 1),
    (6, 4, 2),
    (6, 7, 20),
    (7, 8, 2),
    (4, 8, 4),
    (5, 8, 14),
    (5, 9, 9),
    (8, 9, 10),
    (4, 5, 7)
])
k = Algoritimo_kruskal()
mst = k.kruskal(grafo2)
print(mst.edges)
print(k.peso(mst))
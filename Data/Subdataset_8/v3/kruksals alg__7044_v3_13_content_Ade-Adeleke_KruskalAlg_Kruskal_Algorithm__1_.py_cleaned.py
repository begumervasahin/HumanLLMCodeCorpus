class DisjointSet:
    def __init__(self):
        self.parent = {}
    def make_set(self, vertice):
        self.parent[vertice] = vertice
    def find_set(self, vertice):
        if self.parent[vertice] != vertice:
            self.parent[vertice] = self.find_set(self.parent[vertice])
        return self.parent[vertice]
    def union(self, u, v):
        ancestor1 = self.find_set(u)
        ancestor2 = self.find_set(v)
        if ancestor1 != ancestor2:
            self.parent[ancestor1] = ancestor2
def kruskal(graph):
    kmst = set()
    disjoint_set = DisjointSet()
    for vertice in graph['V']:
        disjoint_set.make_set(vertice)
    edges = sorted(graph['E'])
    for edge in edges:
        weight, u, v = edge
        if disjoint_set.find_set(u) != disjoint_set.find_set(v):
            kmst.add(edge)
            disjoint_set.union(u, v)
    return kmst
graph = {
    'V': ['A', 'B', 'C', 'D', 'E'],
    'E': [(1, 'A', 'B'), (3, 'A', 'C'), (2, 'B', 'C'), (5, 'B', 'D'), (4, 'C', 'D'), (6, 'C', 'E'), (7, 'D', 'E')]
}
minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
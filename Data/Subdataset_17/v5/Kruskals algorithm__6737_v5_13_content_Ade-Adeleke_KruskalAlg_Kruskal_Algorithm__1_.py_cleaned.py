class DisjointSet:
    def __init__(self):
        self.parent = {}
    def make_set(self, vertex):
        self.parent[vertex] = vertex
    def find_set(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find_set(self.parent[vertex])
        return self.parent[vertex]
    def union(self, u, v):
        root_u = self.find_set(u)
        root_v = self.find_set(v)
        if root_u != root_v:
            self.parent[root_u] = root_v
def kruskal(graph):
    disjoint_set = DisjointSet()
    mst = set()
    for vertex in graph['V']:
        disjoint_set.make_set(vertex)
    sorted_edges = sorted(graph['E'])
    for weight, u, v in sorted_edges:
        if disjoint_set.find_set(u) != disjoint_set.find_set(v):
            mst.add((weight, u, v))
            disjoint_set.union(u, v)
    return mst
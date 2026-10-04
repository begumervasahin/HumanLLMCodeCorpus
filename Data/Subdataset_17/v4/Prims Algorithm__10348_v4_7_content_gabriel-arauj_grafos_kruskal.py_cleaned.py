import networkx as nx
class KruskalAlgorithm:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def create_set(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1
    def calculate_weight(self, graph):
        return sum(weight for _, _, weight in graph.edges.data('weight'))
    def kruskal(self, graph):
        for vertex in graph.nodes():
            self.create_set(vertex)
        mst = nx.Graph()
        edges = sorted(graph.edges.data('weight'), key=lambda x: x[2])
        for vertex1, vertex2, weight in edges:
            if self.find(vertex1) != self.find(vertex2):
                self.union(vertex1, vertex2)
                mst.add_edge(vertex1, vertex2, weight=weight)
        return mst
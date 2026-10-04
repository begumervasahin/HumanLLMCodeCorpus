class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def make_set(self, vertice):
        self.parent[vertice] = vertice
        self.rank[vertice] = 0
    def find(self, vertice):
        if self.parent[vertice] != vertice:
            self.parent[vertice] = self.find(self.parent[vertice])
        return self.parent[vertice]
    def union(self, vertice1, vertice2):
        root1 = self.find(vertice1)
        root2 = self.find(vertice2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root1] += 1
def kruskal(graph):
    disjoint_set = DisjointSet()
    for vertice in graph['vertices']:
        disjoint_set.make_set(vertice)
    max_bandwidth_path = set()
    edges = sorted(graph['edges'], reverse=True)
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if disjoint_set.find(vertice1) != disjoint_set.find(vertice2):
            disjoint_set.union(vertice1, vertice2)
            max_bandwidth_path.add(edge)
    return max_bandwidth_path
if __name__ == "__main__":
    graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': [
            (5, 'A', 'B'),
            (10, 'A', 'C'),
            (7, 'B', 'D'),
            (8, 'C', 'D'),
            (6, 'C', 'E'),
            (4, 'D', 'E')
        ]
    }
    max_bandwidth_path = kruskal(graph)
    print("Edges in the Maximum Bandwidth Path (or Maximum Spanning Tree):")
    for edge in max_bandwidth_path:
        print(edge)
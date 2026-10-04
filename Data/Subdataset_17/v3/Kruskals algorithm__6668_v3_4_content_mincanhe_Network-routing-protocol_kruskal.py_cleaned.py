class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def make_set(self, vertex):
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
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root1] += 1
def kruskal(graph):
    disjoint_set = DisjointSet()
    for vertex in graph['vertices']:
        disjoint_set.make_set(vertex)
    max_bandwidth_path = set()
    sorted_edges = sorted(graph['edges'], reverse=True)
    for weight, vertex1, vertex2 in sorted_edges:
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            disjoint_set.union(vertex1, vertex2)
            max_bandwidth_path.add((weight, vertex1, vertex2))
    return max_bandwidth_path
if __name__ == "__main__":
    graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': [
            (10, 'A', 'C'),
            (8, 'C', 'D'),
            (7, 'B', 'D'),
            (6, 'C', 'E'),
            (5, 'A', 'B'),
            (4, 'D', 'E')
        ]
    }
    max_bandwidth_path = kruskal(graph)
    print("Edges in the Maximum Bandwidth Path (Maximum Spanning Tree):")
    for edge in max_bandwidth_path:
        print(edge)
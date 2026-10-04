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
class KruskalMST:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = sorted(edges, key=lambda x: x[2])
        self.mst = []
        self.cumulative_distance = 0
        self.disjoint_set = DisjointSet()
    def run(self):
        for vertex in self.vertices:
            self.disjoint_set.make_set(vertex)
        for v1, v2, weight in self.edges:
            if self.disjoint_set.find(v1) != self.disjoint_set.find(v2):
                self.disjoint_set.union(v1, v2)
                self.cumulative_distance += weight
                self.mst.append((v1, v2, weight, self.cumulative_distance))
    def print_mst(self):
        print("******************************************************************************")
        print(f"{'Vertex 1':<15}{'Vertex 2':<15}{'Distance':<10}{'Cumulative Distance':<20}")
        print("******************************************************************************")
        for v1, v2, weight, cum_dist in self.mst:
            print(f"{v1:<15}{v2:<15}{weight:<10}{cum_dist:<20}")
if __name__ == "__main__":
    vertices = {'A', 'B', 'C', 'D', 'E'}
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 2),
        ('B', 'D', 6),
        ('C', 'D', 4),
        ('C', 'E', 2),
        ('D', 'E', 5)
    ]
    kruskal = KruskalMST(vertices, edges)
    kruskal.run()
    kruskal.print_mst()
class UnionFind:
    def __init__(self, nodes):
        self.parent = list(range(nodes))
        self.rank = [0] * nodes
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.edges = []
    def addEdge(self, u, v, weight):
        self.edges.append((u, v, weight))
def kruskal(graph):
    union_find = UnionFind(graph.V)
    graph.edges.sort(key=lambda x: x[2])
    result = []
    weight = 0
    for u, v, w in graph.edges:
        if union_find.find(u) != union_find.find(v):
            union_find.union(u, v)
            result.append((u, v, w))
            weight += w
    print("Result:")
    for u, v, w in result:
        print(f"{u} -- {v} == w: {w}")
    print(f"The MST has a weight of {weight}")
    return result
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1, 9)
    g.addEdge(0, 2, 7)
    g.addEdge(0, 3, 2)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 3, 2)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 3)
    g.addEdge(3, 4, 3)
    kruskal(g)
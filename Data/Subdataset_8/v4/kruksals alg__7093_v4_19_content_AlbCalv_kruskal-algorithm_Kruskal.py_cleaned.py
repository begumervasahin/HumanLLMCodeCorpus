class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
        self.parent = []
        self.rank = []
    def initialize_sets(self):
        for vertex in range(self.V):
            self.parent.append(vertex)
            self.rank.append(0)
    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
def kruskal(graph):
    graph.initialize_sets()
    result = []
    i = 0
    n = 0
    graph.edges = sorted(graph.edges, key=get_key)
    while n < graph.V - 1:
        u, v, w = graph.edges[i]
        i += 1
        x = graph.find(u)
        y = graph.find(v)
        if x != y:
            n += 1
            result.append([u, v, w])
            graph.merge(x, y)
    print("Result")
    weight = 0
    for u, v, w in result:
        print("%d -- %d == w: %d" % (u, v, w))
        weight += w
    print("The MST has a weight of %d" % weight)
    return result
def get_key(item):
    return item[2]
g = Graph(5)
g.add_edge(0, 1, 9)
g.add_edge(0, 2, 7)
g.add_edge(0, 3, 2)
g.add_edge(1, 2, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 4, 3)
kruskal(g)
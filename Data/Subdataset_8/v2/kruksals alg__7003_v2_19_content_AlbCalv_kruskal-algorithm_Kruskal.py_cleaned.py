class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.edges = []
        self.parent = []
        self.rank = []
    def initializeSets(self):
        for node in range(self.V):
            self.parent.append(node)
            self.rank.append(0)
    def addEdge(self, u, v, weight):
        self.edges.append([u, v, weight])
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += 1
def Kruskal(graph):
    graph.initializeSets()
    result = []
    i = 0
    n = 0
    graph.edges = sorted(graph.edges, key=lambda x: x[2])
    while n < graph.V - 1:
        u, v, w = graph.edges[i]
        i += 1
        x = graph.find(u)
        y = graph.find(v)
        if x != y:
            n += 1
            result.append([u, v, w])
            graph.union(x, y)
    print("Result")
    weight = 0
    for u, v, w in result:
        print("%d -- %d == w: %d" % (u, v, w))
        weight += w
    print("The MST has a weight of %d" % weight)
    return result
g = Graph(5)
g.addEdge(0, 1, 9)
g.addEdge(0, 2, 7)
g.addEdge(0, 3, 2)
g.addEdge(1, 2, 2)
g.addEdge(2, 3, 2)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 3)
g.addEdge(3, 4, 3)
Kruskal(g)
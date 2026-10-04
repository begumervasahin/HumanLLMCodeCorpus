class Graph:
    def __init__(self, vertices=None, edges=None, directed=False):
        self.V = vertices if vertices is not None else []
        self.E = edges if edges is not None else []
        self.directed = directed
        self.adj = {vertex.value: [] for vertex in self.V}
    def get_adj(self, v):
        return self.adj[v.value]
    def add_vertex(self, value):
        u = Vertex(value=value)
        self.V.append(u)
        self.adj[u.value] = []
    def add_edge(self, u, v, weight):
        e = Edge(u, v, weight)
        self.adj[u.value].append(e)
        self.E.append(e)
        if not self.directed:
            f = Edge(v, u, weight)
            self.adj[v.value].append(f)
class Vertex:
    def __init__(self, value=None, d=None, pre=None):
        self.value = value
        self.d = d
        self.pre = pre
class Edge:
    def __init__(self, u=None, v=None, weight=None):
        self.u = u
        self.v = v
        self.weight = weight
    def equals(self, other):
        return self.u == other.u and self.v == other.v
def main():
    g = Graph(directed=False)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    v1 = g.V[0]
    v2 = g.V[1]
    v3 = g.V[2]
    g.add_edge(v1, v2, 10)
    g.add_edge(v2, v3, 20)
    g.add_edge(v3, v1, 30)
    print("Vertices in the graph:")
    for v in g.V:
        print(f"Vertex {v.value}")
    print("\nEdges in the graph:")
    for e in g.E:
        print(f"Edge from {e.u.value} to {e.v.value} with weight {e.weight}")
if __name__ == "__main__":
    main()
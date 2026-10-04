import math
import random
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight
class AdjacencyList:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
    def get_vertices(self):
        return self.vertices
    def get_number_of_vertices(self):
        return len(self.vertices)
    def get_edges(self):
        return self.edges
    def add_edge(self, edge):
        self.edges.append(edge)
    def print_me(self):
        for edge in self.edges:
            print(f"({edge.u}, {edge.v}) - Weight: {edge.weight}")
class Node:
    def __init__(self, vertex, parent):
        self.vertex = vertex
        self.parent = parent
        self.rank = 1
    def make_child_of(self, parent):
        self.parent = parent
    def get_root(self, path):
        if self.parent is None:
            return self
        else:
            path.append(self)
            root = self.parent.get_root(path)
            return root
class UnionFind:
    def __init__(self, num_vertices):
        self.trees = [Node(i, None) for i in range(num_vertices)]
    def find(self, i):
        path = []
        root = self.trees[i].get_root(path)
        for node in path:
            node.parent = root
        return root
    def union(self, root_x, root_y, edge, mst):
        mst.add_edge(edge)
        if root_x.rank <= root_y.rank:
            root_y.make_child_of(root_x)
            root_y.rank += 1
        else:
            root_x.make_child_of(root_y)
            root_x.rank += 1
def sollins(adj):
    mst = AdjacencyList(adj.get_vertices(), [])
    uf = UnionFind(adj.get_number_of_vertices())
    number_of_components = adj.get_number_of_vertices()
    while number_of_components > 1:
        cheap_edge = [Edge(-1, -1, math.inf) for _ in range(adj.get_number_of_vertices())]
        for edge in adj.get_edges():
            set_x = uf.find(edge.u)
            set_y = uf.find(edge.v)
            if set_x != set_y:
                if cheap_edge[set_x.vertex].weight >= edge.weight:
                    cheap_edge[set_x.vertex] = edge
                if cheap_edge[set_y.vertex].weight >= edge.weight:
                    cheap_edge[set_y.vertex] = edge
        for edge in cheap_edge:
            if edge.weight != math.inf:
                set_x = uf.find(edge.u)
                set_y = uf.find(edge.v)
                if set_x != set_y:
                    uf.union(set_x, set_y, edge, mst)
                    number_of_components -= 1
    return mst
class DataGenerator:
    def __init__(self, num_vertices, edge_probability, method=2):
        self.num_vertices = num_vertices
        self.edge_probability = edge_probability
        self.method = method
    def generate_data(self):
        vertices = list(range(self.num_vertices))
        edges = []
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if random.random() < self.edge_probability:
                    weight = random.randint(1, 100)
                    edges.append(Edge(i, j, weight))
        return AdjacencyList(vertices, edges)
if __name__ == '__main__':
    print("Original Adjacency List")
    dg = DataGenerator(100, 0.1)
    graph = dg.generate_data()
    graph.print_me()
    mst = sollins(graph)
    print("\nMST: Sollin's Algorithm")
    mst.print_me()
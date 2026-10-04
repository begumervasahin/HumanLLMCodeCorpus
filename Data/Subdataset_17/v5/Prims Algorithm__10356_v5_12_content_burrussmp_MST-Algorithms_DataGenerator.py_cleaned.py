import random
import math
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight
    def __str__(self):
        return f"edge:({self.u}--{self.v}) with weight {self.weight}"
class AdjacencyList:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adj = [[] for _ in range(len(vertices))]
        for edge in edges:
            self._add_edge_to_adjacency_list(edge)
    def _add_edge_to_adjacency_list(self, edge):
        self.adj[edge.u].append((edge.v, edge.weight))
        self.adj[edge.v].append((edge.u, edge.weight))
    def add_edge(self, edge):
        self.edges.append(edge)
        self._add_edge_to_adjacency_list(edge)
    def __str__(self):
        result = []
        for node, edges in enumerate(self.adj):
            edges_str = " ".join(f"({v}:{w:.2f})" for v, w in edges)
            result.append(f"{node}: {edges_str}")
        return "\n".join(result)
    def adjacent_to(self, u, index):
        return self.adj[u][index]
    def number_of_neighbors_to(self, u):
        return len(self.adj[u])
    def number_of_vertices(self):
        return len(self.vertices)
    def get_edges(self):
        return self.edges
    def get_vertices(self):
        return self.vertices
class DataGenerator:
    def __init__(self, n, p, method=1, weight_max=30, xlim=100, ylim=100, seed=3141):
        self.n = n
        self.p = p
        self.method = method
        self.weight_max = weight_max
        self.xlim = xlim
        self.ylim = ylim
        random.seed(seed)
    def generate_data(self):
        if self.method == 1:
            return self._method1()
        elif self.method == 2:
            return self._method2()
        else:
            print("Method not defined")
            return AdjacencyList([], [])
    def _method1(self):
        vertices = list(range(self.n))
        edges = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if random.randint(1, 10000) <= self.p * 10000:
                    weight = random.randint(1, self.weight_max + 1)
                    edges.append(Edge(i, j, weight))
        return AdjacencyList(vertices, edges)
    def _method2(self):
        vertices = list(range(self.n))
        points = [(random.randint(1, self.xlim + 1), random.randint(1, self.ylim + 1)) for _ in range(self.n)]
        edges = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if random.randint(1, 10000) <= self.p * 10000:
                    weight = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
                    edges.append(Edge(i, j, weight))
        return AdjacencyList(vertices, edges)

import random
import math
class AdjacencyList:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adj = [[] for _ in vertices]
        for edge in edges:
            self.adj[edge.u].append((edge.v, edge.weight))
            self.adj[edge.v].append((edge.u, edge.weight))
    def add_edge(self, edge):
        self.edges.append(edge)
        self.adj[edge.u].append((edge.v, edge.weight))
        self.adj[edge.v].append((edge.u, edge.weight))
    def print_graph(self):
        for node, neighbors in enumerate(self.adj):
            print(f"{node}:", end='')
            for neighbor in neighbors:
                print(f" ({neighbor[0]}:{neighbor[1]:0.2f})", end='')
            print('')
    def adjacent_to(self, u, index):
        return self.adj[u][index]
    def number_of_neighbors(self, u):
        return len(self.adj[u])
    def get_number_of_vertices(self):
        return len(self.vertices)
    def get_edges(self):
        return self.edges
    def get_vertices(self):
        return self.vertices
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight
    def print_edge(self):
        print(f"edge:({self.u}--{self.v}) with weight {self.weight}")
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
                if random.randint(1, 10001) <= self.p * 10000:
                    weight = random.randint(1, self.weight_max + 1)
                    edges.append(Edge(i, j, weight))
        return AdjacencyList(vertices, edges)
    def _method2(self):
        vertices = list(range(self.n))
        coords = [(random.randint(1, self.xlim + 1), random.randint(1, self.ylim + 1)) for _ in range(self.n)]
        edges = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if random.randint(1, 10001) <= self.p * 10000:
                    x1, y1 = coords[i]
                    x2, y2 = coords[j]
                    weight = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    edges.append(Edge(i, j, weight))
        return AdjacencyList(vertices, edges)
if __name__ == "__main__":
    n = 10
    p = 0.2
    method = 1
    data_gen = DataGenerator(n, p, method)
    graph = data_gen.generate_data()
    graph.print_graph()
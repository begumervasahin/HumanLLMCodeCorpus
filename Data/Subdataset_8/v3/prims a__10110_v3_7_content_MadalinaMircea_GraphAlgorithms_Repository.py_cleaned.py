class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]
    def add_edge(self, v1, v2, weight=1):
        self.adjacency_list[v1].append((v2, weight))
    def num_vertices(self):
        return self.num_vertices
    def num_edges(self):
        total_edges = sum(len(edges) for edges in self.adjacency_list)
        return total_edges
    def has_edge(self, v1, v2):
        return any(v2 in neighbors for neighbors in self.adjacency_list[v1])
    def degree(self, v):
        return len(self.adjacency_list[v])
    def neighbors(self, v):
        return [neighbor[0] for neighbor in self.adjacency_list[v]]
    def edges(self):
        all_edges = []
        for v in range(self.num_vertices):
            for neighbor, _ in self.adjacency_list[v]:
                all_edges.append((v, neighbor))
        return all_edges
class GraphRepository:
    def __init__(self, filename="graph1.txt"):
        self.load_from_file(filename)
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                num_vertices = int(file.readline().strip())
                self.graph = Graph(num_vertices)
                for line in file:
                    v1, v2 = map(int, line.split())
                    self.graph.add_edge(v1, v2)
                    self.graph.add_edge(v2, v1)
        except FileNotFoundError:
            print("File not found.")
    def num_vertices(self):
        return self.graph.num_vertices()
    def num_edges(self):
        return self.graph.num_edges()
    def has_edge(self, v1, v2):
        return self.graph.has_edge(v1, v2)
    def degree(self, v):
        return self.graph.degree(v)
    def neighbors(self, v):
        return self.graph.neighbors(v)
    def all_edges(self):
        return self.graph.edges()
    def add_edge(self, v1, v2, weight=1):
        return self.graph.add_edge(v1, v2, weight)
repo = GraphRepository("graph1.txt")
print("Number of vertices:", repo.num_vertices())
print("Number of edges:", repo.num_edges())
print("Is there an edge between vertices 1 and 2?", repo.has_edge(1, 2))
print("Degree of vertex 1:", repo.degree(1))
print("Neighbours of vertex 1:", repo.neighbors(1))
print("All edges in the graph:", repo.all_edges())
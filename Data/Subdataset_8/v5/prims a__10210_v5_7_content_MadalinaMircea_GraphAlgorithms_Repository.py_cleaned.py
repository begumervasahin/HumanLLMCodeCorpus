
from Graph import Graph
class Repository:
    def __init__(self, filename="graph1.txt"):
        self._load_from_file(filename)
    def _load_from_file(self, filename):
        with open(filename, 'r') as file:
            num_vertices = int(file.readline().split()[0])
            self.graph = Graph(num_vertices)
            for line in file:
                v1, v2 = map(int, line.split())
                self.graph.add_edge(v1, v2)
                self.graph.add_edge(v2, v1)
    def get_number_of_vertices(self):
        return self.graph.get_number_of_vertices()
    def get_number_of_edges(self):
        return self.graph.get_number_of_edges()
    def is_edge(self, v1, v2):
        return self.graph.is_edge(v1, v2)
    def get_degree(self, v):
        return self.graph.get_degree(v)
    def get_neighbours(self, v):
        return self.graph.get_neighbours(v)
    def show_all(self):
        return self.graph.get_all_vertices()
    def add_edge(self, v1, v2, c=None):
        return self.graph.add_edge(v1, v2, c)
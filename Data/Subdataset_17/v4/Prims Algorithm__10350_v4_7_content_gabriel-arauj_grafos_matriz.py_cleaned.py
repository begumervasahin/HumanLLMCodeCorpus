import networkx as nx
from random import randint
class GraphManager:
    def __init__(self):
        self.num_vertices = 0
        self.adjacency_matrix = []
    def load_from_matrix(self, matrix):
        self.num_vertices = len(matrix)
        self.adjacency_matrix = matrix
    def to_graph(self):
        G = nx.Graph()
        for node in range(self.num_vertices):
            G.add_node(node)
        for i in range(self.num_vertices):
            for j in range(i, self.num_vertices):
                if self.adjacency_matrix[i][j] > 0:
                    weight = self.adjacency_matrix[i][j]
                    G.add_edge(i, j, weight=weight)
        return G
    def generate_random_graph(self):
        G = nx.connected_watts_strogatz_graph(self.num_vertices, randint(self.num_vertices
        edges = G.edges()
        self.adjacency_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for v1, v2 in edges:
            weight = randint(1, 50)
            self.adjacency_matrix[v1][v2] = weight
            self.adjacency_matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        self.num_vertices = G.number_of_nodes()
        return G
    def get_adjacency_matrix(self):
        return self.adjacency_matrix
    def clear_matrix(self):
        self.num_vertices = 0
        self.adjacency_matrix = []
    def generate_complete_graph(self):
        num_vertices = int(input("Enter the number of vertices to generate a complete graph: "))
        G = nx.complete_graph(num_vertices)
        self.num_vertices = G.number_of_nodes()
        edges = G.edges()
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in edges:
            weight = randint(1, 50)
            self.adjacency_matrix[v1][v2] = weight
            self.adjacency_matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        return G
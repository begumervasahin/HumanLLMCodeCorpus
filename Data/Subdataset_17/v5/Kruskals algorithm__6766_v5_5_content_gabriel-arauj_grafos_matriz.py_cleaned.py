import networkx as nx
from random import randint
class AdjacencyMatrix:
    def __init__(self):
        self.num_vertices = 0
        self.matrix = []
    def populate_matrix(self, num_vertices, matrix_data):
        self.num_vertices = num_vertices
        self.matrix = matrix_data
    def to_graph(self):
        G = nx.Graph()
        G.add_nodes_from(range(self.num_vertices))
        for i in range(self.num_vertices):
            for j in range(i, self.num_vertices):
                weight = self.matrix[i][j]
                if weight > 0:
                    G.add_edge(i, j, weight=weight)
        return G
    def generate_random_graph(self, num_vertices):
        self.num_vertices = num_vertices
        G = nx.connected_watts_strogatz_graph(num_vertices, randint(num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        for u, v in G.edges():
            weight = randint(1, 50)
            self.matrix[u][v] = weight
            self.matrix[v][u] = weight
            G.edges[u, v]['weight'] = weight
        return G
    def clear_matrix(self):
        self.num_vertices = 0
        self.matrix = []
    def generate_complete_graph(self, num_vertices):
        self.num_vertices = num_vertices
        G = nx.complete_graph(num_vertices)
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        for u, v in G.edges():
            weight = randint(1, 50)
            self.matrix[u][v] = weight
            self.matrix[v][u] = weight
            G.edges[u, v]['weight'] = weight
        return G
    def get_adjacency_matrix(self):
        return self.matrix

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
        G.add_nodes_from(range(self.num_vertices))
        for i in range(self.num_vertices):
            for j in range(i, self.num_vertices):
                weight = self.adjacency_matrix[i][j]
                if weight > 0:
                    G.add_edge(i, j, weight=weight)
        return G
    def generate_random_graph(self):
        k = randint(self.num_vertices
        seed = randint(1, 100)
        G = nx.connected_watts_strogatz_graph(self.num_vertices, k, 0.5, tries=100, seed=seed)
        self.adjacency_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for v1, v2 in G.edges():
            weight = randint(1, 50)
            self.adjacency_matrix[v1][v2] = weight
            self.adjacency_matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        return G
    def get_adjacency_matrix(self):
        return self.adjacency_matrix
    def clear_matrix(self):
        self.num_vertices = 0
        self.adjacency_matrix = []
    def generate_complete_graph(self):
        num_vertices = int(input("Enter the number of vertices to generate a complete graph: "))
        G = nx.complete_graph(num_vertices)
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in G.edges():
            weight = randint(1, 50)
            self.adjacency_matrix[v1][v2] = weight
            self.adjacency_matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        return G
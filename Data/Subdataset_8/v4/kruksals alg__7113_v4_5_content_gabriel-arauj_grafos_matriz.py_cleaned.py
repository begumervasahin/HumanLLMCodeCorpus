import networkx as nx
from random import randint
class InputMatrix:
    def __init__(self):
        self.num_vertices = 0
        self.matrix = []
    def input_to_matrix(self, filename):
        with open(filename, 'r') as file:
            self.num_vertices = int(file.readline().strip())
            for line in file:
                row = list(map(int, line.split()))
                self.matrix.append(row)
    def matrix_to_graph(self):
        G = nx.Graph()
        for vertex in range(self.num_vertices):
            G.add_node(vertex)
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if i <= j and self.matrix[i][j] > 0:
                    weight = self.matrix[i][j]
                    G.add_edge(i, j, weight=weight)
        return G
    def random_graph(self, num_vertices):
        G = nx.connected_watts_strogatz_graph(num_vertices, randint(num_vertices
        edges = G.edges()
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in edges:
            weight = randint(1, 50)
            self.matrix[v1][v2] = weight
            self.matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        self.num_vertices = G.number_of_nodes()
        return G
    def get_adjacency_matrix(self):
        return self.matrix
    def clear_matrix(self):
        self.num_vertices = 0
        self.matrix = []
    def complete_graph(self, num_vertices):
        G = nx.complete_graph(num_vertices)
        self.num_vertices = G.number_of_nodes()
        edges = G.edges()
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in edges:
            weight = randint(1, 50)
            self.matrix[v1][v2] = weight
            self.matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        return G
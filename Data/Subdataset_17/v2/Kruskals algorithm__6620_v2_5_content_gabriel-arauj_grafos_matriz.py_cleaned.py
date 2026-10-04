import networkx as nx
from random import randint
class GraphManager:
    def __init__(self):
        self.vertex_count = 0
        self.adjacency_matrix = []
    def load_from_matrix(self, matrix):
        self.adjacency_matrix = matrix
        self.vertex_count = len(matrix)
    def to_graph(self):
        G = nx.Graph()
        for i in range(self.vertex_count):
            G.add_node(i)
        for i in range(self.vertex_count):
            for j in range(i, self.vertex_count):
                if self.adjacency_matrix[i][j] > 0:
                    weight = self.adjacency_matrix[i][j]
                    G.add_edge(i, j, weight=weight)
        return G
    def generate_random_graph(self):
        n = self.vertex_count
        k = randint(int(n / 2), n - 1)
        G = nx.connected_watts_strogatz_graph(n, k, 0.5, tries=100)
        self.adjacency_matrix = [[0] * n for _ in range(n)]
        for v1, v2 in G.edges():
            weight = randint(1, 50)
            self.adjacency_matrix[v1][v2] = weight
            self.adjacency_matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        return G
    def get_adjacency_matrix(self):
        return self.adjacency_matrix
    def clear_matrix(self):
        self.vertex_count = 0
        self.adjacency_matrix = []
    def generate_complete_graph(self, num_vertices):
        G = nx.complete_graph(num_vertices)
        self.vertex_count = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in G.edges():
            weight = randint(1, 50)
            self.adjacency_matrix[v1][v2] = weight
            self.adjacency_matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        return G
if __name__ == "__main__":
    gm = GraphManager()
    matrix = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    gm.load_from_matrix(matrix)
    graph_from_matrix = gm.to_graph()
    print("Edges from loaded matrix:", graph_from_matrix.edges(data=True))
    gm.vertex_count = 10
    random_graph = gm.generate_random_graph()
    print("Random graph edges:", random_graph.edges(data=True))
    complete_graph = gm.generate_complete_graph(5)
    print("Complete graph edges:", complete_graph.edges(data=True))
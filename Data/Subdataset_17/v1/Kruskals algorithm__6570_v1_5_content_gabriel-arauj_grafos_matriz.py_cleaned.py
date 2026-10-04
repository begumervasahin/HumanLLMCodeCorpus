import networkx as nx
from random import randint
class GraphManager:
    def __init__(self):
        self.quant_vert = 0
        self.matriz = []
    def load_from_matrix(self, matrix):
        self.matriz = matrix
        self.quant_vert = len(matrix)
    def to_graph(self):
        G = nx.Graph()
        for i in range(self.quant_vert):
            G.add_node(i)
        for i in range(self.quant_vert):
            for j in range(i, self.quant_vert):
                if self.matriz[i][j] > 0:
                    weight = self.matriz[i][j]
                    G.add_edge(i, j, weight=weight)
        return G
    def generate_random_graph(self):
        n = self.quant_vert
        G = nx.connected_watts_strogatz_graph(n, randint(int(n / 2), n - 1), 0.5, 100)
        self.matriz = [[0] * n for _ in range(n)]
        for v1, v2 in G.edges():
            weight = randint(1, 50)
            self.matriz[v1][v2] = weight
            self.matriz[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        return G
    def get_adjacency_matrix(self):
        return self.matriz
    def clear_matrix(self):
        self.quant_vert = 0
        self.matriz = []
    def generate_complete_graph(self, v):
        G = nx.complete_graph(v)
        self.quant_vert = v
        self.matriz = [[0] * v for _ in range(v)]
        for v1, v2 in G.edges():
            weight = randint(1, 50)
            self.matriz[v1][v2] = weight
            self.matriz[v2][v1] = weight
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
    G = gm.to_graph()
    print("Edges from matrix:", G.edges(data=True))
    gm.quant_vert = 10
    random_graph = gm.generate_random_graph()
    print("Random graph edges:", random_graph.edges(data=True))
    complete_graph = gm.generate_complete_graph(5)
    print("Complete graph edges:", complete_graph.edges(data=True))
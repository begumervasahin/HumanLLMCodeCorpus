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
        graph = nx.Graph()
        for i in range(self.vertex_count):
            graph.add_node(i)
        for i in range(self.vertex_count):
            for j in range(i, self.vertex_count):
                weight = self.adjacency_matrix[i][j]
                if weight > 0:
                    graph.add_edge(i, j, weight=weight)
        return graph
    def generate_random_graph(self):
        graph = self._generate_connected_watts_strogatz_graph()
        self._initialize_adjacency_matrix(graph)
        return graph
    def get_adjacency_matrix(self):
        return self.adjacency_matrix
    def clear_matrix(self):
        self.vertex_count = 0
        self.adjacency_matrix = []
    def generate_complete_graph(self, num_vertices):
        self.vertex_count = num_vertices
        graph = nx.complete_graph(num_vertices)
        self._initialize_adjacency_matrix(graph)
        return graph
    def _generate_connected_watts_strogatz_graph(self):
        num_nodes = self.vertex_count
        k = randint(int(num_nodes / 2), num_nodes - 1)
        return nx.connected_watts_strogatz_graph(num_nodes, k, 0.5, tries=100)
    def _initialize_adjacency_matrix(self, graph):
        self.adjacency_matrix = [[0] * self.vertex_count for _ in range(self.vertex_count)]
        for v1, v2 in graph.edges():
            weight = randint(1, 50)
            self.adjacency_matrix[v1][v2] = weight
            self.adjacency_matrix[v2][v1] = weight
            graph.edges[v1, v2]['weight'] = weight
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
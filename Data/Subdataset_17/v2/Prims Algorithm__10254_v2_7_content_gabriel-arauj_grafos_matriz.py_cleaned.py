import networkx as nx
from random import randint
class GraphManager:
    def __init__(self):
        self.num_vertices = 0
        self.adj_matrix = []
    def load_adjacency_matrix(self, matrix):
        self.adj_matrix = matrix
        self.num_vertices = len(matrix)
    def to_graph(self):
        G = nx.Graph()
        for z in range(self.num_vertices):
            G.add_node(z)
        for x in range(self.num_vertices):
            for y in range(x, self.num_vertices):
                if self.adj_matrix[x][y] > 0:
                    G.add_edge(x, y, weight=self.adj_matrix[x][y])
        return G
    def random_graph(self):
        n = self.num_vertices
        G = nx.connected_watts_strogatz_graph(n, randint(n
        self.adj_matrix = [[0] * n for _ in range(n)]
        for v1, v2 in G.edges():
            weight = randint(1, 50)
            self.adj_matrix[v1][v2] = weight
            self.adj_matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        self.num_vertices = G.number_of_nodes()
        return G
    def get_adjacency_matrix(self):
        return self.adj_matrix
    def clear_matrix(self):
        self.num_vertices = 0
        self.adj_matrix = []
    def complete_graph(self, vertices):
        G = nx.complete_graph(vertices)
        self.num_vertices = G.number_of_nodes()
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
        for v1, v2 in G.edges():
            weight = randint(1, 50)
            self.adj_matrix[v1][v2] = weight
            self.adj_matrix[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        return G
if __name__ == "__main__":
    graph_manager = GraphManager()
    adjacency_matrix = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
    graph_manager.load_adjacency_matrix(adjacency_matrix)
    graph = graph_manager.to_graph()
    print("Graph from loaded adjacency matrix:")
    print(graph.edges(data=True))
    graph_manager.num_vertices = 5
    random_graph = graph_manager.random_graph()
    print("Randomly generated graph:")
    print(random_graph.edges(data=True))
    graph_manager.clear_matrix()
    print("Adjacency matrix after clearing:")
    print(graph_manager.get_adjacency_matrix())
    complete_graph = graph_manager.complete_graph(4)
    print("Complete graph:")
    print(complete_graph.edges(data=True))
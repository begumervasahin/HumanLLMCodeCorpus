import networkx as nx
from random import randint
class InputMatrix:
    def __init__(self):
        self.quant_vert = 0
        self.matriz = []
    def to_graph(self):
        G = nx.Graph()
        for z in range(self.quant_vert):
            G.add_node(z)
        for x in range(self.quant_vert):
            for y in range(self.quant_vert):
                if x <= y:
                    if self.matriz[x][y] > 0:
                        n = self.matriz[x][y]
                        G.add_edge(x, y, weight=n)
        return G
    def random_graph(self):
        n = self.quant_vert
        G = nx.connected_watts_strogatz_graph(n, randint(int(n / 2), n - 1), 0.5, 100, randint(1, 100))
        a = G.edges()
        self.matriz = [[0] * n for _ in range(n)]
        for v1, v2 in a:
            weight = randint(1, 50)
            self.matriz[v1][v2] = weight
            self.matriz[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        self.quant_vert = G.number_of_nodes()
        return G
    def get_adjacency_matrix(self):
        return self.matriz
    def clear_matrix(self):
        self.quant_vert = 0
        self.matriz = []
    def complete_graph(self):
        v = int(input("Enter the number of vertices to generate a complete graph: "))
        G = nx.complete_graph(v)
        self.quant_vert = G.number_of_nodes()
        a = G.edges()
        self.matriz = [[0] * v for _ in range(v)]
        for v1, v2 in a:
            weight = randint(1, 50)
            self.matriz[v1][v2] = weight
            self.matriz[v2][v1] = weight
            G.edges[v1, v2]['weight'] = weight
        return G
if __name__ == "__main__":
    input_matrix = InputMatrix()
    input_matrix.quant_vert = int(input("Enter the number of vertices: "))
    print("1. Convert matrix to graph")
    print("2. Generate a random graph")
    print("3. Generate a complete graph")
    option = int(input("Choose an option: "))
    if option == 1:
        input_matrix.to_mat()
        graph = input_matrix.to_graph()
        print("Graph generated from the matrix:")
        print("Nodes:", graph.nodes())
        print("Edges:", graph.edges())
    elif option == 2:
        graph = input_matrix.random_graph()
        print("Random graph generated:")
        print("Nodes:", graph.nodes())
        print("Edges:", graph.edges(data=True))
        print("Adjacency matrix:")
        for row in input_matrix.get_adjacency_matrix():
            print(row)
    elif option == 3:
        graph = input_matrix.complete_graph()
        print("Complete graph generated:")
        print("Nodes:", graph.nodes())
        print("Edges:", graph.edges(data=True))
        print("Adjacency matrix:")
        for row in input_matrix.get_adjacency_matrix():
            print(row)
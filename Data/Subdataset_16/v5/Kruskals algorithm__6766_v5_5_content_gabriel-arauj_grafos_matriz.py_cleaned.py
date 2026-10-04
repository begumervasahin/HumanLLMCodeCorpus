import networkx as nx
from random import randint
class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self, a1, matrix_data):
        self.a1 = a1
        self.b1 = matrix_data
    def fonk3(self):
        b2 = nx.Graph()
        b2.add_nodes_from(range(self.a1))
        for i in range(self.a1):
            for j in range(i, self.a1):
                b3 = self.b1[i][j]
                if b3 > 0:
                    b2.add_edge(i, j, b3 = b3)
        return b2
    def fonk4(self, a1):
        self.a1 = a1
        b2 = nx.connected_watts_strogatz_graph(a1, randint(a1
        self.b1 = [[0] * a1 for _ in range(a1)]
        for u, v in b2.edges():
            b3 = randint(1, 50)
            self.b1[u][v] = b3
            self.b1[v][u] = b3
            b2.edges[u, v]['b3'] = b3
        return b2
    def fonk5(self):
        self.a1 = 0
        self.b1 = []
    def fonk6(self, a1):
        self.a1 = a1
        b2 = nx.complete_graph(a1)
        self.b1 = [[0] * a1 for _ in range(a1)]
        for u, v in b2.edges():
            b3 = randint(1, 50)
            self.b1[u][v] = b3
            self.b1[v][u] = b3
            b2.edges[u, v]['b3'] = b3
        return b2
    def fonk7(self):
        return self.b1

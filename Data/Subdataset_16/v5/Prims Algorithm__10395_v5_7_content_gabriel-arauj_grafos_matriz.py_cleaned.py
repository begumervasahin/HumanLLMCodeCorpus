import networkx as nx
from random import randint
class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self, matrix):
        self.a1 = len(matrix)
        self.b1 = matrix
    def fonk3(self):
        b2 = nx.Graph()
        b2.add_nodes_from(range(self.a1))
        for i in range(self.a1):
            for j in range(i, self.a1):
                b3 = self.b1[i][j]
                if b3 > 0:
                    b2.add_edge(i, j, b3 = b3)
        return b2
    def fonk4(self):
        b4 = randint(self.a1
        b5 = randint(1, 100)
        b2 = nx.connected_watts_strogatz_graph(self.a1, b4, 0.5, tries=100, b5=b5)
        self.b1 = [[0] * self.a1 for _ in range(self.a1)]
        for v1, v2 in b2.edges():
            b3 = randint(1, 50)
            self.b1[v1][v2] = b3
            self.b1[v2][v1] = b3
            b2.edges[v1, v2]['b3'] = b3
        return b2
    def fonk5(self):
        return self.b1
    def fonk6(self):
        self.a1 = 0
        self.b1 = []
    def fonk7(self):
        a1 = int(input("Enter the number of vertices to generate a complete graph: "))
        b2 = nx.complete_graph(a1)
        self.a1 = a1
        self.b1 = [[0] * a1 for _ in range(a1)]
        for v1, v2 in b2.edges():
            b3 = randint(1, 50)
            self.b1[v1][v2] = b3
            self.b1[v2][v1] = b3
            b2.edges[v1, v2]['b3'] = b3
        return b2
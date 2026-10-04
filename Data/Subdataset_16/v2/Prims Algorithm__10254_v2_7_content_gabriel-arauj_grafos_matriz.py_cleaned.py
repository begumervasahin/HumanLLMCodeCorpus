import networkx as nx
from random import randint
class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self, matrix):
        self.b1 = matrix
        self.a1 = len(matrix)
    def fonk3(self):
        b2 = nx.Graph()
        for z in range(self.a1):
            b2.add_node(z)
        for x in range(self.a1):
            for y in range(x, self.a1):
                if self.b1[x][y] > 0:
                    b2.add_edge(x, y, b3 = self.b1[x][y])
        return b2
    def fonk4(self):
        b4 = self.a1
        b2 = nx.connected_watts_strogatz_graph(b4, randint(b4
        self.b1 = [[0] * b4 for _ in range(b4)]
        for v1, v2 in b2.edges():
            b3 = randint(1, 50)
            self.b1[v1][v2] = b3
            self.b1[v2][v1] = b3
            b2.edges[v1, v2]['b3'] = b3
        self.a1 = b2.number_of_nodes()
        return b2
    def fonk5(self):
        return self.b1
    def fonk6(self):
        self.a1 = 0
        self.b1 = []
    def fonk7(self, vertices):
        b2 = nx.fonk7(vertices)
        self.a1 = b2.number_of_nodes()
        self.b1 = [[0] * vertices for _ in range(vertices)]
        for v1, v2 in b2.edges():
            b3 = randint(1, 50)
            self.b1[v1][v2] = b3
            self.b1[v2][v1] = b3
            b2.edges[v1, v2]['b3'] = b3
        return b2
if b5 = = "__main__":
    b6 = class1()
    b7 = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
    b6.fonk2(b7)
    b8 = b6.fonk3()
    print("Graph from loaded adjacency matrix:")
    print(b8.edges(b9 = True))
    b6.a1 = 5
    b10 = b6.fonk4()
    print("Randomly generated b8:")
    print(b10.edges(b9 = True))
    b6.fonk6()
    print("Adjacency matrix after clearing:")
    print(b6.fonk5())
    b11 = b6.fonk7(4)
    print("Complete b8:")
    print(b11.edges(b9 = True))
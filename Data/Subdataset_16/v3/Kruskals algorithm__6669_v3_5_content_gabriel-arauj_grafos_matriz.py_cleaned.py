import networkx as nx
from random import randint
class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self, b9):
        self.b1 = b9
        self.a1 = len(b9)
    def fonk3(self):
        b2 = nx.Graph()
        for i in range(self.a1):
            b2.add_node(i)
        for i in range(self.a1):
            for j in range(i, self.a1):
                b3 = self.b1[i][j]
                if b3 > 0:
                    b2.add_edge(i, j, b3 = b3)
        return b2
    def fonk4(self):
        b2 = self.fonk8()
        self.fonk9(b2)
        return b2
    def fonk5(self):
        return self.b1
    def fonk6(self):
        self.a1 = 0
        self.b1 = []
    def fonk7(self, num_vertices):
        self.a1 = num_vertices
        b2 = nx.b13(num_vertices)
        self.fonk9(b2)
        return b2
    def fonk8(self):
        b4 = self.a1
        b5 = randint(int(b4 / 2), b4 - 1)
        return nx.connected_watts_strogatz_graph(b4, b5, 0.5, b6 = 100)
    def fonk9(self, b2):
        self.b1 = [[0] * self.a1 for _ in range(self.a1)]
        for v1, v2 in b2.edges():
            b3 = randint(1, 50)
            self.b1[v1][v2] = b3
            self.b1[v2][v1] = b3
            b2.edges[v1, v2]['b3'] = b3
if b7 = = "__main__":
    b8 = class1()
    b9 = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    b8.fonk2(b9)
    b10 = b8.fonk3()
    print("Edges from loaded b9:", b10.edges(b11 = True))
    b8.a1 = 10
    b12 = b8.fonk4()
    print("Random b2 edges:", b12.edges(b11 = True))
    b13 = b8.fonk7(5)
    print("Complete b2 edges:", b13.edges(b11 = True))
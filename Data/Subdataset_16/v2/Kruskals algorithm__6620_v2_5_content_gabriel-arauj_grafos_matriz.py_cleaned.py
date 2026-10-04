import networkx as nx
from random import randint
class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self, b8):
        self.b1 = b8
        self.a1 = len(b8)
    def fonk3(self):
        b2 = nx.Graph()
        for i in range(self.a1):
            b2.add_node(i)
        for i in range(self.a1):
            for j in range(i, self.a1):
                if self.b1[i][j] > 0:
                    b3 = self.b1[i][j]
                    b2.add_edge(i, j, b3 = b3)
        return b2
    def fonk4(self):
        b4 = self.a1
        b5 = randint(int(b4 / 2), b4 - 1)
        b2 = nx.connected_watts_strogatz_graph(b4, b5, 0.5, tries=100)
        self.b1 = [[0] * b4 for _ in range(b4)]
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
    def fonk7(self, num_vertices):
        b2 = nx.b12(num_vertices)
        self.a1 = num_vertices
        self.b1 = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in b2.edges():
            b3 = randint(1, 50)
            self.b1[v1][v2] = b3
            self.b1[v2][v1] = b3
            b2.edges[v1, v2]['b3'] = b3
        return b2
if b6 = = "__main__":
    b7 = class1()
    b8 = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    b7.fonk2(b8)
    b9 = b7.fonk3()
    print("Edges from loaded b8:", b9.edges(b10 = True))
    b7.a1 = 10
    b11 = b7.fonk4()
    print("Random graph edges:", b11.edges(b10 = True))
    b12 = b7.fonk7(5)
    print("Complete graph edges:", b12.edges(b10 = True))
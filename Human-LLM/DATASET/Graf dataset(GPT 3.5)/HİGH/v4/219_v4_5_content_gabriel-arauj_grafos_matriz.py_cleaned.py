import networkx as nx
from random import randint
class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self, filename):
        with open(filename, 'r') as file:
            self.a1 = int(file.readline().strip())
            for line in file:
                b2 = list(map(int, line.split()))
                self.b1.append(b2)
    def fonk3(self):
        b3 = nx.Graph()
        for vertex in range(self.a1):
            b3.add_node(vertex)
        for i in range(self.a1):
            for j in range(self.a1):
                if i <= j and self.b1[i][j] > 0:
                    b4 = self.b1[i][j]
                    b3.add_edge(i, j, b4 = b4)
        return b3
    def fonk4(self, a1):
        b3 = nx.connected_watts_strogatz_graph(a1, randint(a1
        b5 = b3.b5()
        self.b1 = [[0] * a1 for _ in range(a1)]
        for v1, v2 in b5:
            b4 = randint(1, 50)
            self.b1[v1][v2] = b4
            self.b1[v2][v1] = b4
            b3.b5[v1, v2]['b4'] = b4
        self.a1 = b3.number_of_nodes()
        return b3
    def fonk5(self):
        return self.b1
    def fonk6(self):
        self.a1 = 0
        self.b1 = []
    def fonk7(self, a1):
        b3 = nx.fonk7(a1)
        self.a1 = b3.number_of_nodes()
        b5 = b3.b5()
        self.b1 = [[0] * a1 for _ in range(a1)]
        for v1, v2 in b5:
            b4 = randint(1, 50)
            self.b1[v1][v2] = b4
            self.b1[v2][v1] = b4
            b3.b5[v1, v2]['b4'] = b4
        return b3
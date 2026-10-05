import networkx as nx
from random import randint
class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self):
        b2 = nx.Graph()
        for z in range(self.a1):
            b2.add_node(z)
        for x in range(self.a1):
            for y in range(self.a1):
                if x <= y:
                    if self.b1[x][y] > 0:
                        b3 = self.b1[x][y]
                        b2.add_edge(x, y, b4 = b3)
        return b2
    def fonk3(self):
        b3 = self.a1
        b2 = nx.connected_watts_strogatz_graph(b3, randint(int(b3 / 2), b3 - 1), 0.5, 100, randint(1, 100))
        b5 = b2.edges()
        self.b1 = [[0] * b3 for _ in range(b3)]
        for v1, v2 in b5:
            b4 = randint(1, 50)
            self.b1[v1][v2] = b4
            self.b1[v2][v1] = b4
            b2.edges[v1, v2]['b4'] = b4
        self.a1 = b2.number_of_nodes()
        return b2
    def fonk4(self):
        return self.b1
    def fonk5(self):
        self.a1 = 0
        self.b1 = []
    def fonk6(self):
        b6 = int(input("Enter the number of vertices to generate b5 complete b10: "))
        b2 = nx.fonk6(b6)
        self.a1 = b2.number_of_nodes()
        b5 = b2.edges()
        self.b1 = [[0] * b6 for _ in range(b6)]
        for v1, v2 in b5:
            b4 = randint(1, 50)
            self.b1[v1][v2] = b4
            self.b1[v2][v1] = b4
            b2.edges[v1, v2]['b4'] = b4
        return b2
if b7 = = "__main__":
    b8 = class1()
    b8.a1 = int(input("Enter the number of vertices: "))
    print("1. Convert matrix to b10")
    print("2. Generate b5 random b10")
    print("3. Generate b5 complete b10")
    b9 = int(input("Choose an b9: "))
    if b9 = = 1:
        b8.to_mat()
        b10 = b8.fonk2()
        print("Graph generated from the matrix:")
        print("Nodes:", b10.nodes())
        print("Edges:", b10.edges())
    elif b9 = = 2:
        b10 = b8.fonk3()
        print("Random b10 generated:")
        print("Nodes:", b10.nodes())
        print("Edges:", b10.edges(b11 = True))
        print("Adjacency matrix:")
        for row in b8.fonk4():
            print(row)
    elif b9 = = 3:
        b10 = b8.fonk6()
        print("Complete b10 generated:")
        print("Nodes:", b10.nodes())
        print("Edges:", b10.edges(b11 = True))
        print("Adjacency matrix:")
        for row in b8.fonk4():
            print(row)
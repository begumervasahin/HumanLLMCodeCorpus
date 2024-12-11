import networkx as nx
from random import randint
class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self):
        b2 = nx.Graph()
        for vertex in range(self.a1):
            b2.add_node(vertex)
        for vertex1 in range(self.a1):
            for vertex2 in range(self.a1):
                if vertex1 <= vertex2:
                    b3 = self.b1[vertex1][vertex2]
                    if b3 > 0:
                        b2.add_edge(vertex1, vertex2, b3 = b3)
        return b2
    def fonk3(self):
        b4 = self.a1
        b2 = nx.connected_watts_strogatz_graph(b4, randint(int(b4 / 2), b4 - 1), 0.5, 100, randint(1, 100))
        b5 = b2.b5()
        self.b1 = [[0] * b4 for _ in range(b4)]
        for v1, v2 in b5:
            b3 = randint(1, 50)
            self.b1[v1][v2] = b3
            self.b1[v2][v1] = b3
            b2.b5[v1, v2]['b3'] = b3
        self.a1 = b2.number_of_nodes()
        return b2
    def fonk4(self):
        return self.b1
    def fonk5(self):
        self.a1 = 0
        self.b1 = []
    def fonk6(self):
        b6 = int(input("Enter the number of vertices to generate a complete b10: "))
        b2 = nx.complete_graph(b6)
        self.a1 = b2.number_of_nodes()
        b5 = b2.b5()
        self.b1 = [[0] * b6 for _ in range(b6)]
        for v1, v2 in b5:
            b3 = randint(1, 50)
            self.b1[v1][v2] = b3
            self.b1[v2][v1] = b3
            b2.b5[v1, v2]['b3'] = b3
        return b2
if b7 = = "__main__":
    b8 = class1()
    b8.a1 = int(input("Enter the number of vertices: "))
    print("1. Convert adjacency matrix to b10")
    print("2. Generate a random b10")
    print("3. Generate a complete b10")
    b9 = int(input("Choose an b9: "))
    if b9 = = 1:
        b10 = b8.fonk2()
        print("Graph generated from the adjacency matrix:")
        print("Nodes:", b10.nodes())
        print("Edges:", b10.b5())
    elif b9 = = 2:
        b10 = b8.fonk3()
        print("Random b10 generated:")
        print("Nodes:", b10.nodes())
        print("Edges:", b10.b5(b11 = True))
        print("Adjacency matrix:")
        for row in b8.fonk4():
            print(row)
    elif b9 = = 3:
        b10 = b8.fonk6()
        print("Complete b10 generated:")
        print("Nodes:", b10.nodes())
        print("Edges:", b10.b5(b11 = True))
        print("Adjacency matrix:")
        for row in b8.fonk4():
            print(row)
import networkx as nx
class class1:
    def fonk1(self, b10):
        b1 = nx.Graph()
        b2 = sorted(b10.b11(b15=True), key=lambda x: x[2]['b5'])
        b3 = class2()
        for node in b10.nodes():
            b3.fonk4(node)
        for edge in b2:
            b5, u, b4 = edge[2]['b5'], edge[0], edge[1]
            if b3.fonk5(u) != b3.fonk5(b4):
                b3.fonk6(u, b4)
                b1.add_edge(u, b4, b5 = b5)
        return b1
    def fonk2(self, b1):
        return sum(b5 for _, _, b5 in b1.b11.b15('b5'))
class class2:
    def fonk3(self):
        self.b6 = {}
        self.b7 = {}
    def fonk4(self, x):
        self.b6[x] = x
        self.b7[x] = 0
    def fonk5(self, x):
        if self.b6[x] != x:
            self.b6[x] = self.fonk5(self.b6[x])
        return self.b6[x]
    def fonk6(self, x, y):
        b8 = self.fonk5(x)
        b9 = self.fonk5(y)
        if b8 != b9:
            if self.b7[b8] > self.b7[b9]:
                self.b6[b9] = b8
            else:
                self.b6[b8] = b9
                if self.b7[b8] == self.b7[b9]:
                    self.b7[b9] += 1
def fonk7(b11):
    b10 = nx.Graph()
    for edge in b11:
        b10.add_edge(edge[1], edge[2], b5 = edge[0])
    return b10
def fonk8():
    b11 = [
        (1, 'A', 'B'),
        (5, 'A', 'C'),
        (3, 'A', 'D'),
        (4, 'B', 'C'),
        (2, 'B', 'D'),
        (1, 'C', 'D'),
    ]
    b10 = fonk7(b11)
    b12 = [
        (4, 1, 2),
        (8, 1, 3),
        (11, 2, 3),
        (8, 2, 4),
        (7, 3, 6),
        (1, 3, 7),
        (2, 6, 4),
        (20, 6, 7),
        (2, 7, 8),
        (4, 4, 8),
        (14, 5, 8),
        (9, 5, 9),
        (10, 8, 9),
        (7, 4, 5),
    ]
    b13 = fonk7(b12)
    b14 = class1()
    b1 = b14.fonk1(b13)
    print("Edges of the Minimum Spanning Tree (MST):", b1.b11(b15 = True))
    print("Total b5 of the MST:", b14.fonk2(b1))
if b16 = = "__main__":
    fonk8()
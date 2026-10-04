import networkx as nx
class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
    def fonk2(self, vertice):
        self.b1[vertice] = vertice
        self.b2[vertice] = 0
    def fonk3(self, vertice):
        if self.b1[vertice] != vertice:
            self.b1[vertice] = self.fonk3(self.b1[vertice])
        return self.b1[vertice]
    def fonk4(self, vertice1, vertice2):
        b3 = self.fonk3(vertice1)
        b4 = self.fonk3(vertice2)
        if b3 != b4:
            if self.b2[b3] > self.b2[b4]:
                self.b1[b4] = b3
            else:
                self.b1[b3] = b4
                if self.b2[b3] == self.b2[b4]:
                    self.b2[b4] += 1
    def fonk5(self, grafo):
        return sum(b7 for _, _, b7 in grafo.b10.b12('b7'))
    def fonk6(self, grafo):
        for vertice in grafo.nodes():
            self.fonk2(vertice)
        b5 = nx.Graph()
        b6 = sorted(grafo.b10.b12('b7'), key=lambda x: x[2])
        for vertice1, vertice2, b7 in b6:
            if self.fonk3(vertice1) != self.fonk3(vertice2):
                self.fonk4(vertice1, vertice2)
                b5.add_edge(vertice1, vertice2, b7 = b7)
        return b5
if b8 = = "__main__":
    b9 = nx.Graph()
    b10 = [
        ('A', 'B', 4), ('A', 'C', 3), ('B', 'C', 1),
        ('B', 'D', 2), ('C', 'D', 4), ('C', 'E', 2), ('D', 'E', 3)
    ]
    b9.add_weighted_edges_from(b10)
    b11 = class1()
    b5 = b11.fonk6(b9)
    print("Minimum Spanning Tree:")
    for edge in b5.b10(b12 = True):
        print(edge)
    print("Total Weight:", b11.fonk5(b5))
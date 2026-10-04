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
        b5 = list(grafo.edges.b14('b10'))
        b6 = sum(b10 for _, _, b10 in b5)
        return b6
    def fonk6(self, grafo):
        b7 = list(grafo.nodes())
        for vertice in b7:
            self.fonk2(vertice)
        b8 = nx.Graph()
        b5 = list(grafo.edges.b14('b10'))
        b5.sort(b9 = lambda x: x[2])
        for vertice1, vertice2, b10 in b5:
            if self.fonk3(vertice1) != self.fonk3(vertice2):
                self.fonk4(vertice1, vertice2)
                b8.add_edge(vertice1, vertice2, b10 = b10)
        return b8
if b11 = = "__main__":
    b12 = nx.Graph()
    b12.add_edge('A', 'B', b10 = 4)
    b12.add_edge('A', 'C', b10 = 3)
    b12.add_edge('B', 'C', b10 = 1)
    b12.add_edge('B', 'D', b10 = 2)
    b12.add_edge('C', 'D', b10 = 4)
    b12.add_edge('C', 'E', b10 = 2)
    b12.add_edge('D', 'E', b10 = 3)
    b13 = class1()
    b8 = b13.fonk6(b12)
    print("Minimum Spanning Tree:")
    print(b8.edges(b14 = True))
    print("Total Weight:", b13.fonk5(b8))
import networkx as nx
class class1():
    b1 = dict()
    b2 = dict()
    def fonk1(self, b4):
        self.b1[b4] = b4
        self.b2[b4] = 0
    def fonk2(self, b4):
        b3 = b4
        while self.b1[b4] != b4:
            b4 = self.b1[b4]
        self.b1[b3] = self.b1[b4]
        return self.b1[b4]
    def fonk3(self, vertice1, vertice2):
        b5 = self.fonk2(vertice1)
        b6 = self.fonk2(vertice2)
        if b5 != b6:
            if self.b2[b5] > self.b2[b6]:
                self.b1[b6] = b5
            else:
                self.b1[b5] = b6
                if self.b2[b5] == self.b2[b6]: self.b2[b6] += 1
    def fonk4(self, grafo):
        b7 = list(grafo.edges.data('b8'))
        a1 = 0
        for aresta in b7:
            vertice1, vertice2, b8 = aresta
            a1 += b8
        return a1
    def fonk5(self, grafo):
        b9 = list(grafo.nodes())
        for b4 in b9:
            self.fonk1(b4)
        b10 = nx.Graph()
        b7 = list(grafo.edges.data('b8'))
        b7.sort(b11 = lambda x: x[2])
        for aresta in b7:
            vertice1, vertice2, b8 = aresta
            if self.fonk2(vertice1) != self.fonk2(vertice2):
                self.fonk3(vertice1, vertice2)
                b10.add_edge(aresta[0], aresta[1], b8 = aresta[2])
        return b10
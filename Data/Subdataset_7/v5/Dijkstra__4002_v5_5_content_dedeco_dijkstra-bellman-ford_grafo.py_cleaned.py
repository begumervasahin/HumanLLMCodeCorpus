from vertice import Vertice
class class1:
    def fonk1(self, b1 = False):
        self.b2 = {}
        self.b1 = b1
    def fonk2(self, id):
        b3 = Vertice(id)
        self.b2[id] = b3
        return b3
    def fonk3(self, de, para, b4 = 0):
        if de not in self.b2:
            self.fonk2(de)
        if para not in self.b2:
            self.fonk2(para)
        b5 = self.b2[de]
        b6 = self.b2[para]
        b5.inserir_vertice_adjacente(b6, b4)
        if not self.b1:
            b6.inserir_vertice_adjacente(b5, b4)
    def fonk4(self):
        return list(self.b2.values())
    def fonk5(self, id):
        return self.b2.get(id, None)
    def fonk6(self):
        b7 = set()
        for id, vertice in self.b2.items():
            for adjacente in vertice._vertices_adjacentes:
                b7.add((vertice, adjacente))
        return b7
    def fonk7(self):
        return iter(self.b2.values())
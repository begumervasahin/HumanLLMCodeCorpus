from b3 import Vertice
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
        self.b2[de].inserir_vertice_adjacente(self.b2[para], b4)
        if not self.b1:
            self.b2[para].inserir_vertice_adjacente(self.b2[de], b4)
    def fonk4(self):
        return list(self.b2.values())
    def fonk5(self, id):
        return self.b2.get(id)
    def fonk6(self):
        b5 = set()
        for b3 in self.b2.values():
            for adjacente in b3.vertices_adjacentes:
                b5.add((b3, adjacente))
        return b5
    def fonk7(self):
        return iter(self.b2.values())
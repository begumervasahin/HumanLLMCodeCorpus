class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self, vertice_adjacente, b3 = 0):
        self.b2[vertice_adjacente] = b3
class class2:
    def fonk3(self, b4 = False):
        self.b5 = {}
        self.b4 = b4
    def fonk4(self, b1):
        b6 = class1(b1)
        self.b5[b1] = b6
        return b6
    def fonk5(self, de, para, b3 = 0):
        if de not in self.b5:
            self.fonk4(de)
        if para not in self.b5:
            self.fonk4(para)
        self.b5[de].fonk2(self.b5[para], b3)
        if not self.b4:
            self.b5[para].fonk2(self.b5[de], b3)
    def fonk6(self):
        return list(self.b5.values())
    def fonk7(self, b1):
        return self.b5.get(b1)
    def fonk8(self):
        b7 = set()
        for vertice in self.b5.values():
            for adjacente, b3 in vertice.b2.items():
                b7.add((vertice, adjacente, b3))
        return b7
    def fonk9(self):
        return iter(self.b5.values())
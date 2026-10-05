from Enlace import Enlace
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = -1
        self.b2 = []
    def fonk2(self):
        return self.b2
    def fonk3(self):
        return self.a1
    def fonk4(self):
        return self.b1
    def fonk5(self, enlazar, peso):
        if self.a1 = = -1:
            self.b2.append(Enlace(enlazar, peso))
            self.a1 += 1
        else:
            b3 = self.fonk6(enlazar)
            if b3 = = -1:
                self.b2.append(Enlace(enlazar, peso))
                self.a1 += 1
    def fonk6(self, enlazar):
        a2 = 0
        for b2 in self.b2:
            if b2.getDestino() == enlazar:
                return a2
            a2 += 1
        return -1
    def fonk7(self, b3):
        b4 = self.b2[b3]
        return b4.getPeso()
    def fonk8(self, b3):
        b4 = self.b2[b3]
        return b4.getDestino()
    def fonk9(self, b3):
        if 0 <= b3 < len(self.b2):
            del self.b2[b3]
            self.a1 -= 1
            return True
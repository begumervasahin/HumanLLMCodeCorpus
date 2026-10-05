
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
    def fonk5(self, destino, peso):
        if self.a1 = = -1:
            self.b2.append(Enlace(destino, peso))
            self.a1 = 0
        else:
            b3 = self.fonk6(destino)
            if b3 = = -1:
                self.b2.append(Enlace(destino, peso))
                self.a1 += 1
    def fonk6(self, destino):
        for i, enlace in enumerate(self.b2):
            if enlace.get_destino() == destino:
                return i
        return -1
    def fonk7(self, b3):
        if 0 <= b3 < len(self.b2):
            return self.b2[b3].get_peso()
        return None
    def fonk8(self, b3):
        if 0 <= b3 < len(self.b2):
            return self.b2[b3].get_destino()
        return None
    def fonk9(self, b3):
        if 0 <= b3 < len(self.b2):
            del self.b2[b3]
            self.a1 -= 1
            return True
        return False
from Enlace import Enlace
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self):
        return self.b2
    def fonk3(self):
        return len(self.b2)
    def fonk4(self):
        return self.b1
    def fonk5(self, destino, peso):
        for enlace in self.b2:
            if enlace.get_destino() == destino:
                return
        self.b2.append(Enlace(destino, peso))
    def fonk6(self, destino):
        for i, enlace in enumerate(self.b2):
            if enlace.get_destino() == destino:
                del self.b2[i]
                return True
        return False
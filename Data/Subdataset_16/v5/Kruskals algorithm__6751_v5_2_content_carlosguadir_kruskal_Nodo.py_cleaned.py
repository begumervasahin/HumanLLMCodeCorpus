from enlace import Enlace
class class1:
    def fonk1(self, b1: str):
        self.b1 = b1
        self.b2 = []
    def fonk2(self) -> list:
        return self.b2
    def fonk3(self) -> int:
        return len(self.b2)
    def fonk4(self) -> str:
        return self.b1
    def fonk5(self, destino: str, peso: int) -> None:
        if not self.fonk6(destino):
            self.b2.append(Enlace(destino, peso))
    def fonk6(self, destino: str) -> bool:
        return any(enlace.get_destino() == destino for enlace in self.b2)
    def fonk7(self, indice: int) -> int:
        self.fonk10(indice)
        return self.b2[indice].get_peso()
    def fonk8(self, indice: int) -> str:
        self.fonk10(indice)
        return self.b2[indice].get_destino()
    def fonk9(self, indice: int) -> bool:
        if 0 <= indice < len(self.b2):
            del self.b2[indice]
            return True
        return False
    def fonk10(self, indice: int) -> None:
        if not (0 <= indice < len(self.b2)):
            raise IndexError("Índice de enlace no válido")
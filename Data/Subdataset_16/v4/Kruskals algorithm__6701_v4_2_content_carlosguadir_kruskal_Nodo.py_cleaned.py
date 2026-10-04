from Enlace import Enlace
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
    def fonk5(self, enlazar: str, peso: int) -> None:
        if not self.fonk6(enlazar):
            self.b2.append(Enlace(enlazar, peso))
    def fonk6(self, enlazar: str) -> bool:
        return any(enlace.get_destino() == enlazar for enlace in self.b2)
    def fonk7(self, posicion: int) -> int:
        if 0 <= posicion < len(self.b2):
            return self.b2[posicion].get_peso()
        raise IndexError("Posición de enlace no válida")
    def fonk8(self, posicion: int) -> str:
        if 0 <= posicion < len(self.b2):
            return self.b2[posicion].get_destino()
        raise IndexError("Posición de enlace no válida")
    def fonk9(self, posicion: int) -> bool:
        if 0 <= posicion < len(self.b2):
            del self.b2[posicion]
            return True
        return False
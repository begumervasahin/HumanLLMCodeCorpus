from enlace import Enlace
class Nodo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.enlaces = []
    def get_enlaces(self) -> list:
        return self.enlaces
    def get_enlaces_existentes(self) -> int:
        return len(self.enlaces)
    def get_nombre(self) -> str:
        return self.nombre
    def agregar_enlace(self, destino: str, peso: int) -> None:
        if not self.enlace_existe(destino):
            self.enlaces.append(Enlace(destino, peso))
    def enlace_existe(self, destino: str) -> bool:
        return any(enlace.get_destino() == destino for enlace in self.enlaces)
    def obtener_peso_enlace(self, indice: int) -> int:
        self._validar_indice(indice)
        return self.enlaces[indice].get_peso()
    def obtener_nodo_enlace(self, indice: int) -> str:
        self._validar_indice(indice)
        return self.enlaces[indice].get_destino()
    def eliminar_enlace(self, indice: int) -> bool:
        if 0 <= indice < len(self.enlaces):
            del self.enlaces[indice]
            return True
        return False
    def _validar_indice(self, indice: int) -> None:
        if not (0 <= indice < len(self.enlaces)):
            raise IndexError("Índice de enlace no válido")
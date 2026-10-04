from Enlace import Enlace
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
    def agregar_enlace(self, enlazar: str, peso: int) -> None:
        if not self.enlace_existe(enlazar):
            self.enlaces.append(Enlace(enlazar, peso))
    def enlace_existe(self, enlazar: str) -> bool:
        return any(enlace.get_destino() == enlazar for enlace in self.enlaces)
    def obtener_peso_enlace(self, posicion: int) -> int:
        if 0 <= posicion < len(self.enlaces):
            return self.enlaces[posicion].get_peso()
        raise IndexError("Posición de enlace no válida")
    def obtener_nodo_enlace(self, posicion: int) -> str:
        if 0 <= posicion < len(self.enlaces):
            return self.enlaces[posicion].get_destino()
        raise IndexError("Posición de enlace no válida")
    def eliminar_enlace(self, posicion: int) -> bool:
        if 0 <= posicion < len(self.enlaces):
            del self.enlaces[posicion]
            return True
        return False
class Enlace:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso
    def obtener_destino(self):
        return self.destino
    def obtener_peso(self):
        return self.peso
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.enlaces = []
    def agregar_enlace(self, destino, peso):
        if not self._enlace_existe(destino):
            self.enlaces.append(Enlace(destino, peso))
    def _enlace_existe(self, destino):
        return any(enlace.obtener_destino() == destino for enlace in self.enlaces)
    def obtener_enlaces(self):
        return self.enlaces
    def contar_enlaces(self):
        return len(self.enlaces)
    def obtener_nombre(self):
        return self.nombre
    def obtener_peso_enlace_por_posicion(self, posicion):
        return self.enlaces[posicion].obtener_peso() if 0 <= posicion < len(self.enlaces) else None
    def obtener_destino_enlace_por_posicion(self, posicion):
        return self.enlaces[posicion].obtener_destino() if 0 <= posicion < len(self.enlaces) else None
    def eliminar_enlace(self, posicion):
        if 0 <= posicion < len(self.enlaces):
            del self.enlaces[posicion]
            return True
        return False

from Enlace import Enlace
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.num_enlaces = -1
        self.enlaces = []
    def get_enlaces(self):
        return self.enlaces
    def get_num_enlaces(self):
        return self.num_enlaces
    def get_nombre(self):
        return self.nombre
    def agregar_enlace(self, destino, peso):
        if self.num_enlaces == -1:
            self.enlaces.append(Enlace(destino, peso))
            self.num_enlaces = 0
        else:
            position = self.existe_enlace(destino)
            if position == -1:
                self.enlaces.append(Enlace(destino, peso))
                self.num_enlaces += 1
    def existe_enlace(self, destino):
        for i, enlace in enumerate(self.enlaces):
            if enlace.get_destino() == destino:
                return i
        return -1
    def obtener_peso_enlace(self, position):
        if 0 <= position < len(self.enlaces):
            return self.enlaces[position].get_peso()
        return None
    def obtener_destino_enlace(self, position):
        if 0 <= position < len(self.enlaces):
            return self.enlaces[position].get_destino()
        return None
    def eliminar_enlace(self, position):
        if 0 <= position < len(self.enlaces):
            del self.enlaces[position]
            self.num_enlaces -= 1
            return True
        return False
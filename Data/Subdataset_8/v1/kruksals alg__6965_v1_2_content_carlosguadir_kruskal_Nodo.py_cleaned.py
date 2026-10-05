
from Enlace import Enlace
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.enlacesExistentes = -1
        self.enlaces = []
    def getEnlaces(self):
        return self.enlaces
    def getEnlacesExistentes(self):
        return self.enlacesExistentes
    def getNombre(self):
        return self.nombre
    def agregarEnlace(self, enlazar, peso):
        if self.enlacesExistentes == -1:
            self.enlaces.append(Enlace(enlazar, peso))
            self.enlacesExistentes = 0
        else:
            posicion = self.existeEnlace(enlazar)
            if posicion == -1:
                self.enlaces.append(Enlace(enlazar, peso))
                self.enlacesExistentes += 1
    def existeEnlace(self, enlazar):
        for i, enlace in enumerate(self.enlaces):
            if enlace.getDestino() == enlazar:
                return i
        return -1
    def enlacePosicion(self, posicion):
        if 0 <= posicion < len(self.enlaces):
            return self.enlaces[posicion].getPeso()
        return None
    def nodoPosicion(self, posicion):
        if 0 <= posicion < len(self.enlaces):
            return self.enlaces[posicion].getDestino()
        return None
    def eliminarEnlace(self, posicion):
        if 0 <= posicion < len(self.enlaces):
            del self.enlaces[posicion]
            self.enlacesExistentes -= 1
            return True
        return False
class Enlace:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso
    def getDestino(self):
        return self.destino
    def getPeso(self):
        return self.peso
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.enlaces = []
    def getEnlaces(self):
        return self.enlaces
    def getEnlacesExistentes(self):
        return len(self.enlaces)
    def getNombre(self):
        return self.nombre
    def agregarEnlace(self, enlazar, peso):
        if not self.enlaces:
            self.enlaces.append(Enlace(enlazar, peso))
        else:
            posicion = self.existeEnlace(enlazar)
            if posicion == -1:
                self.enlaces.append(Enlace(enlazar, peso))
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
            return True
        return False
class Vertice:
    def __init__(self, id):
        self._id = id
        self._vertices_adjacentes = {}
        self._distancia = 0
        self._visitado = False
        self._anterior = None
    def get_id(self):
        return self._id
    def inserir_vertice_adjacente(self, para=None, peso=0):
        self._vertices_adjacentes[para] = peso
    def get_vertices_adjacentes(self):
        return self._vertices_adjacentes.keys()
    def get_distancia(self):
        return self._distancia
    def set_distancia(self, distancia):
        self._distancia = distancia
    def set_visitado(self, visitado=True):
        self._visitado = visitado
    def get_visitado(self):
        return self._visitado
    def get_peso(self, para):
        return self._vertices_adjacentes.get(para, None)
    def set_anterior(self, anterior):
        self._anterior = anterior
    def get_anterior(self):
        return self._anterior
    def __str__(self):
        return str(self._id)
def main():
    vertice_a = Vertice('a')
    vertice_b = Vertice('b')
    vertice_c = Vertice('c')
    vertice_a.inserir_vertice_adjacente(vertice_b, 5)
    vertice_a.inserir_vertice_adjacente(vertice_c, 10)
    vertice_b.inserir_vertice_adjacente(vertice_c, 2)
    vertice_a.set_distancia(0)
    vertice_b.set_distancia(5)
    vertice_c.set_distancia(7)
    vertice_a.set_visitado()
    vertice_b.set_anterior(vertice_a)
    vertice_c.set_anterior(vertice_b)
    print(f"Vertice {vertice_a.get_id()}: Adjacentes -> {list(vertice_a.get_vertices_adjacentes())}, Distancia -> {vertice_a.get_distancia()}")
    print(f"Vertice {vertice_b.get_id()}: Adjacentes -> {list(vertice_b.get_vertices_adjacentes())}, Distancia -> {vertice_b.get_distancia()}, Anterior -> {vertice_b.get_anterior().get_id() if vertice_b.get_anterior() else None}")
    print(f"Vertice {vertice_c.get_id()}: Adjacentes -> {list(vertice_c.get_vertices_adjacentes())}, Distancia -> {vertice_c.get_distancia()}, Anterior -> {vertice_c.get_anterior().get_id() if vertice_c.get_anterior() else None}")
if __name__ == "__main__":
    main()
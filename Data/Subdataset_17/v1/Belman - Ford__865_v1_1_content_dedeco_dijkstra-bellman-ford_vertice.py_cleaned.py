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
    def set_visitado(self):
        self._visitado = True
    def get_visitado(self):
        return self._visitado
    def get_peso(self, para):
        return self._vertices_adjacentes[para]
    def set_anterior(self, anterior):
        self._anterior = anterior
    def get_anterior(self):
        return self._anterior
    def __str__(self):
        return str(self._id)
if __name__ == "__main__":
    a = Vertice('a')
    b = Vertice('b')
    c = Vertice('c')
    a.inserir_vertice_adjacente(b, 5)
    a.inserir_vertice_adjacente(c, 10)
    b.inserir_vertice_adjacente(c, 2)
    a.set_distancia(0)
    b.set_distancia(5)
    c.set_distancia(7)
    a.set_visitado()
    b.set_anterior(a)
    c.set_anterior(b)
    print(f"Vertice {a}: Adjacentes -> {a.get_vertices_adjacentes()}, Distancia -> {a.get_distancia()}")
    print(f"Vertice {b}: Adjacentes -> {b.get_vertices_adjacentes()}, Distancia -> {b.get_distancia()}, Anterior -> {b.get_anterior()}")
    print(f"Vertice {c}: Adjacentes -> {c.get_vertices_adjacentes()}, Distancia -> {c.get_distancia()}, Anterior -> {c.get_anterior()}")
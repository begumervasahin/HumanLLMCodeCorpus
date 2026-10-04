class Vertice:
    def __init__(self, id):
        self.id = id
        self._vertices_adjacentes = {}
    def inserir_vertice_adjacente(self, vertice, peso):
        self._vertices_adjacentes[vertice] = peso
    def __repr__(self):
        return f"Vertice({self.id})"
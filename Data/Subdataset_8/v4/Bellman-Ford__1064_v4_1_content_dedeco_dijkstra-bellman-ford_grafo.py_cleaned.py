from vertice import Vertice
class Grafo:
    def __init__(self, direcionado=False):
        self.vertices = {}
        self.direcionado = direcionado
    def inserir_vertice(self, id):
        vertice = Vertice(id)
        self.vertices[id] = vertice
        return vertice
    def inserir_aresta(self, de, para, peso=0):
        if de not in self.vertices:
            self.inserir_vertice(de)
        if para not in self.vertices:
            self.inserir_vertice(para)
        self.vertices[de].inserir_vertice_adjacente(self.vertices[para], peso)
        if not self.direcionado:
            self.vertices[para].inserir_vertice_adjacente(self.vertices[de], peso)
    def get_vertices(self):
        return list(self.vertices.values())
    def get_vertice(self, id):
        return self.vertices.get(id)
    def get_arestas(self):
        arestas = set()
        for vertice in self.vertices.values():
            for adjacente in vertice.vertices_adjacentes:
                arestas.add((vertice, adjacente))
        return arestas
    def __iter__(self):
        return iter(self.vertices.values())
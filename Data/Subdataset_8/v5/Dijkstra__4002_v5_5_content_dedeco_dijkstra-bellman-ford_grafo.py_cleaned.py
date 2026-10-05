from vertice import Vertice
class Grafo:
    def __init__(self, direcionado=False):
        self.vertices = {}
        self.direcionado = direcionado
    def inserir_vertice(self, id):
        novo_vertice = Vertice(id)
        self.vertices[id] = novo_vertice
        return novo_vertice
    def inserir_aresta(self, de, para, peso=0):
        if de not in self.vertices:
            self.inserir_vertice(de)
        if para not in self.vertices:
            self.inserir_vertice(para)
        vertice_de = self.vertices[de]
        vertice_para = self.vertices[para]
        vertice_de.inserir_vertice_adjacente(vertice_para, peso)
        if not self.direcionado:
            vertice_para.inserir_vertice_adjacente(vertice_de, peso)
    def obter_vertices(self):
        return list(self.vertices.values())
    def obter_vertice(self, id):
        return self.vertices.get(id, None)
    def obter_arestas(self):
        arestas = set()
        for id, vertice in self.vertices.items():
            for adjacente in vertice._vertices_adjacentes:
                arestas.add((vertice, adjacente))
        return arestas
    def __iter__(self):
        return iter(self.vertices.values())
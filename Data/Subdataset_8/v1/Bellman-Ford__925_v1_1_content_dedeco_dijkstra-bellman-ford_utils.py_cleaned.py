import sys
class Vertice:
    def __init__(self, id):
        self._id = id
        self._distancia = sys.maxsize
        self._anterior = None
        self._adjacentes = {}
    def get_id(self):
        return self._id
    def get_distancia(self):
        return self._distancia
    def set_distancia(self, distancia):
        self._distancia = distancia
    def get_anterior(self):
        return self._anterior
    def set_anterior(self, anterior):
        self._anterior = anterior
    def get_adjacentes(self):
        return self._adjacentes
    def add_adjacente(self, vertice, peso):
        self._adjacentes[vertice] = peso
class Grafo:
    def __init__(self):
        self._vertices = {}
    def get_vertices(self):
        return self._vertices.values()
    def get_vertice(self, id):
        return self._vertices.get(id)
    def inserir_vertice(self, id):
        if id not in self._vertices:
            self._vertices[id] = Vertice(id)
    def inserir_aresta(self, start, end, peso):
        if start in self._vertices and end in self._vertices:
            self._vertices[start].add_adjacente(self._vertices[end], peso)
def initialize_single_source(g, s):
    for v in g.get_vertices():
        v.set_distancia(sys.maxsize)
    g.get_vertice(s).set_distancia(0)
def extract_min(Q):
    min_vertice = Q[0]
    for v in Q:
        if v.get_distancia() < min_vertice.get_distancia():
            min_vertice = v
    Q.remove(min_vertice)
    return min_vertice
def relax(u, v):
    if v.get_distancia() > u.get_distancia() + u.get_adjacentes()[v]:
        v.set_distancia(u.get_distancia() + u.get_adjacentes()[v])
        v.set_anterior(u)
def caminho_minino(v, caminho):
    if v.get_anterior():
        caminho.append(v.get_anterior().get_id())
        caminho_minino(v.get_anterior(), caminho)
    return caminho
if __name__ == "__main__":
    g = Grafo()
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertex in vertices:
        g.inserir_vertice(vertex)
    edges = [
        ('a', 'b', 10),
        ('a', 'c', 3),
        ('b', 'c', 1),
        ('b', 'd', 2),
        ('c', 'b', 4),
        ('c', 'd', 8),
        ('c', 'e', 2),
        ('d', 'e', 7),
        ('e', 'd', 9)
    ]
    for edge in edges:
        g.inserir_aresta(*edge)
    initialize_single_source(g, 'a')
    Q = g.get_vertices()
    while Q:
        u = extract_min(Q)
        for v in u.get_adjacentes():
            relax(u, v)
    for vertex in g.get_vertices():
        path = [vertex.get_id()]
        caminho = caminho_minino(vertex, path)
        print(f'The shortest path from a to {vertex.get_id()} is: {caminho[::-1]} with cost {vertex.get_distancia()}.')
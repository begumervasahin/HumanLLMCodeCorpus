def initialize_single_source(g, s):
    for v in g.get_vertices():
        v.set_distancia(float('inf'))
    g.get_vertice(s).set_distancia(0)
def extract_min(Q):
    min_vertice = min(Q, key=lambda v: v.get_distancia())
    Q.remove(min_vertice)
    return min_vertice
def relax(u, v):
    if v.get_distancia() > u.get_distancia() + u.get_peso(v):
        v.set_distancia(u.get_distancia() + u.get_peso(v))
        v.set_anterior(u)
def caminho_minimo(v, caminho):
    if v.get_anterior():
        caminho.append(v.get_anterior().get_id())
        caminho_minimo(v.get_anterior(), caminho)
    return
class Vertice:
    def __init__(self, id):
        self.id = id
        self.distancia = float('inf')
        self.anterior = None
        self.arestas = {}
    def set_distancia(self, distancia):
        self.distancia = distancia
    def get_distancia(self):
        return self.distancia
    def set_anterior(self, anterior):
        self.anterior = anterior
    def get_anterior(self):
        return self.anterior
    def get_id(self):
        return self.id
    def add_aresta(self, destino, peso):
        self.arestas[destino] = peso
    def get_peso(self, destino):
        return self.arestas[destino]
class Grafo:
    def __init__(self):
        self.vertices = {}
    def inserir_vertice(self, id):
        self.vertices[id] = Vertice(id)
    def get_vertice(self, id):
        return self.vertices[id]
    def get_vertices(self):
        return self.vertices.values()
if __name__ == "__main__":
    grafo = Grafo()
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertice in vertices:
        grafo.inserir_vertice(vertice)
    arestas = [
        ('a', 'b', 10),
        ('a', 'c', 3),
        ('b', 'd', 2),
        ('c', 'b', 4),
        ('c', 'd', 8),
        ('c', 'e', 2),
        ('d', 'e', 7),
        ('e', 'd', 9)
    ]
    for origem, destino, peso in arestas:
        grafo.get_vertice(origem).add_aresta(grafo.get_vertice(destino), peso)
    initialize_single_source(grafo, 'a')
    Q = list(grafo.get_vertices())
    while Q:
        u = extract_min(Q)
        for v in u.arestas:
            relax(u, v)
    for v in grafo.get_vertices():
        caminho = [v.get_id()]
        caminho_minimo(v, caminho)
        print(f'O menor caminho é: {caminho[::-1]} com custo {v.get_distancia()}.')
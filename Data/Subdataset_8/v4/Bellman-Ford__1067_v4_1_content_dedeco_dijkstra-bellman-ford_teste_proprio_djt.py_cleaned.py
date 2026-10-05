from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def test():
    print('Testing Dijkstra\'s algorithm on a randomly generated graph.')
    g = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for vertex in vertices:
        g.inserir_vertice(vertex)
    g.inserir_aresta('a', 'b', 10)
    g.inserir_aresta('a', 'c', 5)
    g.inserir_aresta('a', 'g', 1)
    g.inserir_aresta('a', 'f', 6)
    g.inserir_aresta('b', 'c', 2)
    g.inserir_aresta('b', 'd', 1)
    g.inserir_aresta('c', 'b', 3)
    g.inserir_aresta('c', 'd', 9)
    g.inserir_aresta('c', 'e', 2)
    g.inserir_aresta('c', 'g', 4)
    g.inserir_aresta('d', 'i', 4)
    g.inserir_aresta('e', 'i', 8)
    g.inserir_aresta('e', 'h', 4)
    g.inserir_aresta('e', 'd', 6)
    g.inserir_aresta('f', 'g', 6)
    g.inserir_aresta('g', 'h', 8)
    g.inserir_aresta('h', 'i', 9)
    g.inserir_aresta('j', 'a', 3)
    g.inserir_aresta('j', 'i', 5)
    dijkstra(g, 'a')
    for v in g.get_vertices():
        caminho = [v.get_id()]
        caminho_minino(v, caminho)
        print(f'The shortest path is: {caminho[::-1]} with cost {v.get_distancia()}.')
if __name__ == "__main__":
    test()
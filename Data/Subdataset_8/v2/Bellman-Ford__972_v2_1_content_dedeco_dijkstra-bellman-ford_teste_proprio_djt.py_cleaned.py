from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def test():
    print('Testing a randomly generated graph.')
    g = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for vertex in vertices:
        g.inserir_vertice(vertex)
    edges = [('a', 'b', 10), ('a', 'c', 5), ('a', 'g', 1), ('a', 'f', 6),
             ('b', 'c', 2), ('b', 'd', 1), ('c', 'b', 3), ('c', 'd', 9),
             ('c', 'e', 2), ('c', 'g', 4), ('d', 'i', 4), ('e', 'i', 8),
             ('e', 'h', 4), ('e', 'd', 6), ('f', 'g', 6), ('g', 'h', 8),
             ('h', 'i', 9), ('j', 'a', 3), ('j', 'i', 5)]
    for edge in edges:
        g.inserir_aresta(*edge)
    dijkstra(g, 'a')
    for v in g.get_vertices():
        caminho = [v.get_id()]
        caminho_minino(v, caminho)
        print('Shortest path: %s, Distance: %d' % (caminho[::-1], v.get_distancia()))
if __name__ == "__main__":
    test()
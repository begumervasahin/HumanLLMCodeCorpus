from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class class1(Exception):
    pass
def fonk1():
    print('Testing a randomly generated graph.')
    b1 = Grafo(direcionado=True)
    b2 = ['a', 'b', 'c', 'd', 'e', 'f', 'b1', 'h', 'i', 'j']
    for vertex in b2:
        b1.inserir_vertice(vertex)
    b3 = [('a', 'b', 10), ('a', 'c', 5), ('a', 'b1', 1), ('a', 'f', 6),
             ('b', 'c', 2), ('b', 'd', 1), ('c', 'b', 3), ('c', 'd', 9),
             ('c', 'e', 2), ('c', 'b1', 4), ('d', 'i', 4), ('e', 'i', 8),
             ('e', 'h', 4), ('e', 'd', 6), ('f', 'b1', 6), ('b1', 'h', 8),
             ('h', 'i', 9), ('j', 'a', 3), ('j', 'i', 5)]
    for edge in b3:
        b1.inserir_aresta(*edge)
    dijkstra(b1, 'a')
    for v in b1.get_vertices():
        b4 = [v.get_id()]
        caminho_minino(v, b4)
        print('Shortest path: %s, Distance: %d' % (b4[::-1], v.get_distancia()))
if b5 = = "__main__":
    fonk1()
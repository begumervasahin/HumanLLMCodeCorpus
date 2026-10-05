from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class class1(Exception):
    pass
def fonk1():
    print('Generating a randomly generated b1...')
    b1 = Grafo(direcionado=True)
    b2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for vertex in b2:
        b1.inserir_vertice(vertex)
    b3 = [('a', 'b', 10), ('a', 'c', 5), ('a', 'g', 1), ('a', 'f', 6),
             ('b', 'c', 2), ('b', 'd', 1), ('c', 'b', 3), ('c', 'd', 9),
             ('c', 'e', 2), ('c', 'g', 4), ('d', 'i', 4), ('e', 'i', 8),
             ('e', 'h', 4), ('e', 'd', 6), ('f', 'g', 6), ('g', 'h', 8),
             ('h', 'i', 9), ('j', 'a', 3), ('j', 'i', 5)]
    for edge in b3:
        b1.inserir_aresta(*edge)
    return b1
def fonk2():
    print('Testing Dijkstra\'s algorithm on a randomly generated b1...')
    b1 = fonk1()
    dijkstra(b1, 'a')
    for vertex in b1.get_vertices():
        b4 = [vertex.get_id()]
        caminho_minino(vertex, b4)
        print(f'Shortest b4 from vertex {vertex.get_id()}: {b4[::-1]}, Distance: {vertex.get_distancia()}')
if b5 = = "__main__":
    fonk2()
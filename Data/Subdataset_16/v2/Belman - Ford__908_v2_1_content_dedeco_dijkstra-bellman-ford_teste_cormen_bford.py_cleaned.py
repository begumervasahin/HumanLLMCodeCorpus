from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
import sys
class class1(Exception):
    pass
def fonk1():
    """
    Test the b1 example from the book "Algorithms 3rd Edition (Cormen)", page 480.
    """
    print('Testing b1 example from "Algorithms 3rd Edition (Cormen)", page 480.')
    b1 = Grafo(direcionado=True)
    b2 = ['a', 'b', 'c', 'd', 'e']
    for vertex in b2:
        b1.inserir_vertice(vertex)
    b3 = [
        ('a', 'b', 6),
        ('a', 'c', 7),
        ('a', 'e', 2),
        ('b', 'd', 5),
        ('b', 'c', 8),
        ('b', 'e', -4),
        ('c', 'd', -3),
        ('c', 'e', 9),
        ('d', 'b', -2),
        ('e', 'd', 7)
    ]
    for de, para, peso in b3:
        b1.inserir_aresta(de, para, peso)
    bellman_ford(b1, 'd')
    for vertex in b1.get_vertices():
        b4 = [vertex.get_id()]
        caminho_minimo(vertex, b4)
        print(f'The shortest b4 is: {b4[::-1]} with a cost of {vertex.get_distancia()}.')
if b5 = = "__main__":
    fonk1()
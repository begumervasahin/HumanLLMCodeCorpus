from grafo import Grafo
from dijkstra import dijkstra
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
        ('a', 'b', 10),
        ('a', 'c', 5),
        ('b', 'd', 1),
        ('b', 'c', 2),
        ('c', 'b', 3),
        ('c', 'e', 2),
        ('c', 'd', 9),
        ('d', 'e', 4),
        ('e', 'a', 7),
        ('e', 'd', 6)
    ]
    for origem, destino, peso in b3:
        b1.inserir_aresta(origem, destino, peso)
    dijkstra(b1, 'a')
    for vertex in b1.get_vertices():
        b4 = [vertex.get_id()]
        caminho_minimo(vertex, b4)
        print(f'The shortest b4 to vertex {vertex.get_id()} is: {b4[::-1]} with a cost of {vertex.get_distancia()}.')
if b5 = = "__main__":
    fonk1()
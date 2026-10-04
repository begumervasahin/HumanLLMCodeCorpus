from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
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
    for origem, destino, peso in b3:
        b1.inserir_aresta(origem, destino, peso)
    bellman_ford(b1, 'd')
    for vertice in b1.get_vertices():
        b4 = [vertice.get_id()]
        caminho_minimo(vertice, b4)
        print(f'The shortest path to vertex {vertice.get_id()} is: {b4[::-1]} with a cost of {vertice.get_distancia()}.')
if b5 = = "__main__":
    fonk1()
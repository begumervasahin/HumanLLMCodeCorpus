from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
class class1(Exception):
    pass
def fonk1():
    print('Testing the b1 example from the lectures of Prof. Fernando Lobo at the University of Algarve in Portugal.')
    b1 = Grafo(direcionado=True)
    b2 = ['a', 'b', 'c', 'd', 'e']
    for vertex in b2:
        b1.inserir_vertice(vertex)
    b3 = [
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
    for edge in b3:
        b1.inserir_aresta(*edge)
    if bellman_ford(b1, 'a'):
        for vertex in b1.get_vertices():
            b4 = [vertex.get_id()]
            caminho_minino(vertex, b4)
            print(f'The shortest b4 is: {b4[::-1]} with cost {vertex.get_distancia()}.')
    else:
        print('Negative cycle found.')
if b5 = = "__main__":
    fonk1()
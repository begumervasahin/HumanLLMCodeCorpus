from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
class class1(Exception):
    pass
def fonk1():
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
    for origem, destino, peso in b3:
        b1.inserir_aresta(origem, destino, peso)
    return b1
def fonk2(b1, start_vertex_id):
    if bellman_ford(b1, start_vertex_id):
        for vertex in b1.get_vertices():
            b4 = [vertex.get_id()]
            caminho_minimo(vertex, b4)
            print(f'The shortest b4 to vertex {vertex.get_id()} is: {b4[::-1]} with a cost of {vertex.get_distancia()}.')
    else:
        print('Negative weight cycle found')
def fonk3():
    print('Testing b1 example from Professor Fernando Lobo\'s lectures at the University of Algarve in Portugal.')
    b1 = fonk1()
    fonk2(b1, 'a')
if b5 = = "__main__":
    fonk3()
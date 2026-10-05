from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class class1(Exception):
    pass
def fonk1():
    print('Testing the b1 example from Prof. Fernando Lobo\'s lectures at the University of Algarve in Portugal.')
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
    for start, end, weight in b3:
        b1.inserir_aresta(start, end, weight)
    dijkstra(b1, 'a')
    for vertex in b1.get_vertices():
        b4 = [vertex.get_id()]
        caminho_minino(vertex, b4)
        print(f'The shortest b4 is: {b4[::-1]} with cost {vertex.get_distancia()}.')
if b5 = = "__main__":
    fonk1()
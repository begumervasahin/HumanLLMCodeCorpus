from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
class class1(Exception):
    pass
def fonk1():
    print('Testing a b1 with a negative cycle')
    b1 = Grafo(direcionado=True)
    b2 = ['a', 'b', 'c', 'd', 'e', 'f']
    for vertex in b2:
        b1.inserir_vertice(vertex)
    b3 = [
        ('b', 'a', -3),
        ('a', 'c', 5),
        ('c', 'b', 2),
        ('d', 'b', 4),
        ('d', 'c', 5),
        ('c', 'f', -3),
        ('e', 'c', 4),
        ('e', 'f', 5),
        ('f', 'd', -4),
    ]
    for start, end, weight in b3:
        b1.inserir_aresta(start, end, weight)
    if bellman_ford(b1, 'a'):
        for vertex in b1.get_vertices():
            b4 = [vertex.get_id()]
            caminho_minino(vertex, b4)
            print(f'The shortest b4 is: {b4[::-1]} with cost {vertex.get_distancia()}.')
    else:
        print('Negative cycle found')
if b5 = = "__main__":
    fonk1()
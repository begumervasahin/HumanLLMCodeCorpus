from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class class1(Exception):
    pass
def fonk1():
    print('Testing Dijkstra\'s algorithm on a randomly generated graph.')
    b1 = Grafo(direcionado=True)
    b2 = ['a', 'b', 'c', 'd', 'e', 'f', 'b1', 'h', 'i', 'j']
    for vertex in b2:
        b1.inserir_vertice(vertex)
    b1.inserir_aresta('a', 'b', 10)
    b1.inserir_aresta('a', 'c', 5)
    b1.inserir_aresta('a', 'b1', 1)
    b1.inserir_aresta('a', 'f', 6)
    b1.inserir_aresta('b', 'c', 2)
    b1.inserir_aresta('b', 'd', 1)
    b1.inserir_aresta('c', 'b', 3)
    b1.inserir_aresta('c', 'd', 9)
    b1.inserir_aresta('c', 'e', 2)
    b1.inserir_aresta('c', 'b1', 4)
    b1.inserir_aresta('d', 'i', 4)
    b1.inserir_aresta('e', 'i', 8)
    b1.inserir_aresta('e', 'h', 4)
    b1.inserir_aresta('e', 'd', 6)
    b1.inserir_aresta('f', 'b1', 6)
    b1.inserir_aresta('b1', 'h', 8)
    b1.inserir_aresta('h', 'i', 9)
    b1.inserir_aresta('j', 'a', 3)
    b1.inserir_aresta('j', 'i', 5)
    dijkstra(b1, 'a')
    for v in b1.get_vertices():
        b3 = [v.get_id()]
        caminho_minino(v, b3)
        print(f'The shortest path is: {b3[::-1]} with cost {v.get_distancia()}.')
if b4 = = "__main__":
    fonk1()
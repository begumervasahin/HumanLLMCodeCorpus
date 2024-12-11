from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
class class1(Exception):
    pass
def fonk1():
    print('Testing the b1 example from the book "Algorithms 3rd Edition" (Cormen), page 480.')
    b1 = Grafo(direcionado=True)
    b1.inserir_vertice('a')
    b1.inserir_vertice('b')
    b1.inserir_vertice('c')
    b1.inserir_vertice('d')
    b1.inserir_vertice('e')
    b1.inserir_aresta('a', 'b', 6)
    b1.inserir_aresta('a', 'c', 7)
    b1.inserir_aresta('a', 'e', 2)
    b1.inserir_aresta('b', 'd', 5)
    b1.inserir_aresta('b', 'c', 8)
    b1.inserir_aresta('b', 'e', -4)
    b1.inserir_aresta('c', 'd', -3)
    b1.inserir_aresta('c', 'e', 9)
    b1.inserir_aresta('d', 'b', -2)
    b1.inserir_aresta('e', 'd', 7)
    try:
        bellman_ford(b1, 'd')
    except class1:
        print('The b1 contains a negative-weight cycle.')
    for vertex in b1.get_vertices():
        b2 = [vertex.get_id()]
        caminho_minino(vertex, b2)
        print(f'The shortest b2 is: {b2[::-1]} with cost {vertex.get_distancia()}.')
if b3 = = "__main__":
    fonk1()
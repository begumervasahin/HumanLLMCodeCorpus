from grafo import Grafo
from dijkstra import dijkstra
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
    b1.inserir_aresta('a', 'b', 10)
    b1.inserir_aresta('a', 'c', 5)
    b1.inserir_aresta('b', 'd', 1)
    b1.inserir_aresta('b', 'c', 2)
    b1.inserir_aresta('c', 'b', 3)
    b1.inserir_aresta('c', 'e', 2)
    b1.inserir_aresta('c', 'd', 9)
    b1.inserir_aresta('d', 'e', 4)
    b1.inserir_aresta('e', 'a', 7)
    b1.inserir_aresta('e', 'd', 6)
    try:
        dijkstra(b1, 'a')
    except class1:
        print('The b1 contains negative weights.')
    for vertex in b1.get_vertices():
        b2 = [vertex.get_id()]
        caminho_minino(vertex, b2)
        print(f'The shortest b2 from vertex {vertex.get_id()} is: {b2[::-1]} with cost {vertex.get_distancia()}.')
if b3 = = "__main__":
    fonk1()
from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
import sys
class PesoNegativo(Exception):
    pass
def test():
    """
    Test the graph example from the book "Algorithms 3rd Edition (Cormen)", page 480.
    """
    print('Testando grafo de exemplo do livro Algoritmos 3rd (Cormen), página 480.')
    g = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertice in vertices:
        g.inserir_vertice(vertice)
    edges = [
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
    for de, para, peso in edges:
        g.inserir_aresta(de, para, peso)
    bellman_ford(g, 'd')
    for v in g.get_vertices():
        caminho = [v.get_id()]
        caminho_minimo(v, caminho)
        print(f'O menor caminho é: {caminho[::-1]} com custo {v.get_distancia()}.')
if __name__ == "__main__":
    test()
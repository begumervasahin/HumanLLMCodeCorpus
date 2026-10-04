from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
import sys
class NegativeWeightException(Exception):
    pass
def test_graph():
    """
    Test the graph example from the book "Algorithms 3rd Edition (Cormen)", page 480.
    """
    print('Testing graph example from "Algorithms 3rd Edition (Cormen)", page 480.')
    graph = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertex in vertices:
        graph.inserir_vertice(vertex)
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
        graph.inserir_aresta(de, para, peso)
    bellman_ford(graph, 'd')
    for vertex in graph.get_vertices():
        path = [vertex.get_id()]
        caminho_minimo(vertex, path)
        print(f'The shortest path is: {path[::-1]} with a cost of {vertex.get_distancia()}.')
if __name__ == "__main__":
    test_graph()
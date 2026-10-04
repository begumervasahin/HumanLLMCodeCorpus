from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
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
    for origem, destino, peso in edges:
        graph.inserir_aresta(origem, destino, peso)
    bellman_ford(graph, 'd')
    for vertice in graph.get_vertices():
        caminho = [vertice.get_id()]
        caminho_minimo(vertice, caminho)
        print(f'The shortest path to vertex {vertice.get_id()} is: {caminho[::-1]} with a cost of {vertice.get_distancia()}.')
if __name__ == "__main__":
    test_graph()
from grafo import Grafo
from dijkstra import dijkstra
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
    edges = [
        ('a', 'b', 10),
        ('a', 'c', 5),
        ('b', 'd', 1),
        ('b', 'c', 2),
        ('c', 'b', 3),
        ('c', 'e', 2),
        ('c', 'd', 9),
        ('d', 'e', 4),
        ('e', 'a', 7),
        ('e', 'd', 6)
    ]
    for vertex in vertices:
        graph.inserir_vertice(vertex)
    for origem, destino, peso in edges:
        graph.inserir_aresta(origem, destino, peso)
    dijkstra(graph, 'a')
    for vertex in graph.get_vertices():
        path = [vertex.get_id()]
        caminho_minimo(vertex, path)
        print(f'The shortest path to vertex {vertex.get_id()} is: {path[::-1]} with a cost of {vertex.get_distancia()}.')
if __name__ == "__main__":
    test_graph()
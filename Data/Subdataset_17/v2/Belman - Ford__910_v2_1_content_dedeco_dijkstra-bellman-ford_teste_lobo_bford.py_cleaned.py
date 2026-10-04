from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
class NegativeWeightException(Exception):
    pass
def test_graph():
    print('Testing graph example from Professor Fernando Lobo\'s lectures at the University of Algarve in Portugal.')
    graph = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertex in vertices:
        graph.inserir_vertice(vertex)
    edges = [
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
    for origem, destino, peso in edges:
        graph.inserir_aresta(origem, destino, peso)
    if bellman_ford(graph, 'a'):
        for vertex in graph.get_vertices():
            path = [vertex.get_id()]
            caminho_minimo(vertex, path)
            print(f'The shortest path to vertex {vertex.get_id()} is: {path[::-1]} with a cost of {vertex.get_distancia()}.')
    else:
        print('Negative weight cycle found')
if __name__ == "__main__":
    test_graph()
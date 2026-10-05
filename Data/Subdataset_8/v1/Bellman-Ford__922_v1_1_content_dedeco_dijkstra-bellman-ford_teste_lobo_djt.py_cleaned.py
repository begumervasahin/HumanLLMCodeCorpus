from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def test_graph():
    print('Testing the graph example from Prof. Fernando Lobo\'s lectures at the University of Algarve in Portugal.')
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
    for start, end, weight in edges:
        graph.inserir_aresta(start, end, weight)
    dijkstra(graph, 'a')
    for vertex in graph.get_vertices():
        path = [vertex.get_id()]
        caminho_minino(vertex, path)
        print(f'The shortest path is: {path[::-1]} with cost {vertex.get_distancia()}.')
if __name__ == "__main__":
    test_graph()
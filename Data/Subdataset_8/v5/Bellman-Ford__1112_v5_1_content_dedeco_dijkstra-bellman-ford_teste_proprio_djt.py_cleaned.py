from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def test():
    print('Testing Dijkstra\'s algorithm on a randomly generated graph.')
    graph = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for vertex in vertices:
        graph.inserir_vertice(vertex)
    edges = [('a', 'b', 10), ('a', 'c', 5), ('a', 'g', 1), ('a', 'f', 6),
             ('b', 'c', 2), ('b', 'd', 1), ('c', 'b', 3), ('c', 'd', 9),
             ('c', 'e', 2), ('c', 'g', 4), ('d', 'i', 4), ('e', 'i', 8),
             ('e', 'h', 4), ('e', 'd', 6), ('f', 'g', 6), ('g', 'h', 8),
             ('h', 'i', 9), ('j', 'a', 3), ('j', 'i', 5)]
    for source, destination, weight in edges:
        graph.inserir_aresta(source, destination, weight)
    dijkstra(graph, 'a')
    for vertex in graph.get_vertices():
        path = [vertex.get_id()]
        caminho_minino(vertex, path)
        print(f'The shortest path is: {path[::-1]} with cost {vertex.get_distancia()}.')
if __name__ == "__main__":
    test()
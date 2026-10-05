from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def test_graph_with_negative_cycle():
    print('Testing a graph with a negative cycle')
    graph = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    for vertex in vertices:
        graph.inserir_vertice(vertex)
    edges = [
        ('b', 'a', -3),
        ('a', 'c', 5),
        ('c', 'b', 2),
        ('d', 'b', 4),
        ('d', 'c', 5),
        ('c', 'f', -3),
        ('e', 'c', 4),
        ('e', 'f', 5),
        ('f', 'd', -4),
    ]
    for start, end, weight in edges:
        graph.inserir_aresta(start, end, weight)
    if bellman_ford(graph, 'a'):
        for vertex in graph.get_vertices():
            path = [vertex.get_id()]
            caminho_minino(vertex, path)
            print(f'The shortest path is: {path[::-1]} with cost {vertex.get_distancia()}.')
    else:
        print('Negative cycle found')
if __name__ == "__main__":
    test_graph_with_negative_cycle()
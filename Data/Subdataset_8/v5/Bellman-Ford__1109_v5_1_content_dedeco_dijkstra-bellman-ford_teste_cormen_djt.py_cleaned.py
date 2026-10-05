from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def run_graph_test():
    print('Testing the graph example from the book "Algorithms 3rd Edition" (Cormen), page 480.')
    graph = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertex in vertices:
        graph.inserir_vertice(vertex)
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
    for edge in edges:
        graph.inserir_aresta(*edge)
    dijkstra(graph, 'a')
    for vertex in graph.get_vertices():
        path = [vertex.get_id()]
        caminho_minino(vertex, path)
        print(f'The shortest path is: {path[::-1]} with cost {vertex.get_distancia()}.')
if __name__ == "__main__":
    run_graph_test()
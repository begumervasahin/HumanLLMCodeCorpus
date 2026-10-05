from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def run_dijkstra_test():
    graph = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertex_id in vertices:
        graph.inserir_vertice(vertex_id)
    edges = [
        ('a', 'b', 10), ('a', 'c', 5), ('b', 'd', 1), ('b', 'c', 2),
        ('c', 'b', 3), ('c', 'e', 2), ('c', 'd', 9), ('d', 'e', 4),
        ('e', 'a', 7), ('e', 'd', 6)
    ]
    for from_vertex, to_vertex, weight in edges:
        graph.inserir_aresta(from_vertex, to_vertex, weight)
    try:
        dijkstra(graph, 'a')
    except PesoNegativo:
        print('The graph contains negative weights.')
    for vertex in graph.get_vertices():
        path = [vertex.get_id()]
        caminho_minino(vertex, path)
        print(f'The shortest path from vertex {vertex.get_id()} is: {path[::-1]} with cost {vertex.get_distancia()}.')
if __name__ == "__main__":
    print('Testing the graph example from the book "Algorithms 3rd Edition" (Cormen), page 480.')
    run_dijkstra_test()
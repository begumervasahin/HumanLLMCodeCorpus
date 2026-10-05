from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def test():
    print('Testing the graph example from the book "Algorithms 3rd Edition" (Cormen), page 480.')
    graph = Grafo(direcionado=True)
    graph.inserir_vertice('a')
    graph.inserir_vertice('b')
    graph.inserir_vertice('c')
    graph.inserir_vertice('d')
    graph.inserir_vertice('e')
    graph.inserir_aresta('a', 'b', 10)
    graph.inserir_aresta('a', 'c', 5)
    graph.inserir_aresta('b', 'd', 1)
    graph.inserir_aresta('b', 'c', 2)
    graph.inserir_aresta('c', 'b', 3)
    graph.inserir_aresta('c', 'e', 2)
    graph.inserir_aresta('c', 'd', 9)
    graph.inserir_aresta('d', 'e', 4)
    graph.inserir_aresta('e', 'a', 7)
    graph.inserir_aresta('e', 'd', 6)
    try:
        dijkstra(graph, 'a')
    except PesoNegativo:
        print('The graph contains negative weights.')
    for vertex in graph.get_vertices():
        path = [vertex.get_id()]
        caminho_minino(vertex, path)
        print(f'The shortest path is: {path[::-1]} with cost {vertex.get_distancia()}.')
if __name__ == "__main__":
    test()
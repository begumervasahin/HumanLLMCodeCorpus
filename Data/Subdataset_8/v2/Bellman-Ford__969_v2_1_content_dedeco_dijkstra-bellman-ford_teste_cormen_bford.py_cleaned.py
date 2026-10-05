from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def test():
    print('Testing the graph example from the book "Algorithms 3rd Edition" (Cormen), page 480.')
    g = Grafo(direcionado=True)
    g.adicionar_vertice('a')
    g.adicionar_vertice('b')
    g.adicionar_vertice('c')
    g.adicionar_vertice('d')
    g.adicionar_vertice('e')
    g.adicionar_aresta('a', 'b', 6)
    g.adicionar_aresta('a', 'c', 7)
    g.adicionar_aresta('a', 'e', 2)
    g.adicionar_aresta('b', 'd', 5)
    g.adicionar_aresta('b', 'c', 8)
    g.adicionar_aresta('b', 'e', -4)
    g.adicionar_aresta('c', 'd', -3)
    g.adicionar_aresta('c', 'e', 9)
    g.adicionar_aresta('d', 'b', -2)
    g.adicionar_aresta('e', 'd', 7)
    try:
        bellman_ford(g, 'd')
    except PesoNegativo:
        print('The graph contains a negative-weight cycle.')
    for v in g.obter_vertices():
        caminho = [v.id]
        caminho_minino(v, caminho)
        print(f'The shortest path is: {caminho[::-1]} with cost {v.distancia}.')
if __name__ == "__main__":
    test()
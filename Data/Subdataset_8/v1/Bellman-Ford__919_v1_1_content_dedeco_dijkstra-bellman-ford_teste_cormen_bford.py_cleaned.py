from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
class PesoNegativo(Exception):
    pass
def test():
    print('Testando grafo de exemplo do livro Algoritmos 3rd (Cormen), página 480.')
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
        print('O grafo contém um ciclo de peso negativo.')
    for v in g.obter_vertices():
        caminho = [v.id]
        caminho_minino(v, caminho)
        print(f'O menor caminho é: {caminho[::-1]} com custo {v.distancia}.')
if __name__ == "__main__":
    test()
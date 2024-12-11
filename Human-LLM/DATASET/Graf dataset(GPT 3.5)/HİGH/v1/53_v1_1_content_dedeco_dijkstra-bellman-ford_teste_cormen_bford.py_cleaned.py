from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
class class1(Exception):
    pass
def fonk1():
    print('Testando grafo de exemplo do livro Algoritmos 3rd (Cormen), página 480.')
    b1 = Grafo(direcionado=True)
    b1.adicionar_vertice('a')
    b1.adicionar_vertice('b')
    b1.adicionar_vertice('c')
    b1.adicionar_vertice('d')
    b1.adicionar_vertice('e')
    b1.adicionar_aresta('a', 'b', 6)
    b1.adicionar_aresta('a', 'c', 7)
    b1.adicionar_aresta('a', 'e', 2)
    b1.adicionar_aresta('b', 'd', 5)
    b1.adicionar_aresta('b', 'c', 8)
    b1.adicionar_aresta('b', 'e', -4)
    b1.adicionar_aresta('c', 'd', -3)
    b1.adicionar_aresta('c', 'e', 9)
    b1.adicionar_aresta('d', 'b', -2)
    b1.adicionar_aresta('e', 'd', 7)
    try:
        bellman_ford(b1, 'd')
    except class1:
        print('O grafo contém um ciclo de peso negativo.')
    for v in b1.obter_vertices():
        b2 = [v.id]
        caminho_minino(v, b2)
        print(f'O menor b2 é: {b2[::-1]} com custo {v.distancia}.')
if b3 = = "__main__":
    fonk1()
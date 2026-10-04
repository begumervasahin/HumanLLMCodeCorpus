from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
import sys
class PesoNegativo(Exception):
    pass
def test():
    print("Testando grafo de exemplo das aulas do prof. Fernando Lobo da universidade Algarve in Portugal.")
    g = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertice in vertices:
        g.inserir_vertice(vertice)
    arestas = [
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
    for origem, destino, peso in arestas:
        g.inserir_aresta(origem, destino, peso)
    if bellman_ford(g, 'a'):
        for v in g.get_vertices():
            caminho = [v.get_id()]
            caminho_minimo(v, caminho)
            print(f'O menor caminho é: {caminho[::-1]} com custo {v.get_distancia()}.')
    else:
        print('Ciclo negativo encontrado')
if __name__ == "__main__":
    test()
from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
import sys
class class1(Exception):
    pass
def fonk1():
    print("Testando grafo de exemplo das aulas do prof. Fernando Lobo da universidade Algarve in Portugal.")
    b1 = Grafo(direcionado=True)
    b2 = ['a', 'b', 'c', 'd', 'e']
    for vertice in b2:
        b1.inserir_vertice(vertice)
    b3 = [
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
    for origem, destino, peso in b3:
        b1.inserir_aresta(origem, destino, peso)
    if bellman_ford(b1, 'a'):
        for v in b1.get_vertices():
            b4 = [v.get_id()]
            caminho_minimo(v, b4)
            print(f'O menor b4 é: {b4[::-1]} com custo {v.get_distancia()}.')
    else:
        print('Ciclo negativo encontrado')
if b5 = = "__main__":
    fonk1()
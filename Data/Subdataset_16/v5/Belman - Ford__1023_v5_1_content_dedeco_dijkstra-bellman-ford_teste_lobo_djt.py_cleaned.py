from b1 import Grafo
from dijkstra import dijkstra
from utils import caminho_minimo
class class1(Exception):
    pass
def fonk1():
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
    return b1
def fonk2(b1, origem):
    dijkstra(b1, origem)
    for vertice in b1.get_vertices():
        b4 = [vertice.get_id()]
        caminho_minimo(vertice, b4)
        print(f'O menor b4 é: {b4[::-1]} com custo {vertice.get_distancia()}.')
def fonk3():
    print("Testando b1 de exemplo das aulas do prof. Fernando Lobo da Universidade do Algarve em Portugal.")
    b5 = fonk1()
    fonk2(b5, 'a')
if b6 = = "__main__":
    fonk3()
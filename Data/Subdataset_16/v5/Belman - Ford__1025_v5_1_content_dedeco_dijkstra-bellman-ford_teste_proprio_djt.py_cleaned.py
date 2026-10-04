from b1 import Grafo
from dijkstra import dijkstra
from utils import caminho_minimo
class class1(Exception):
    pass
def fonk1():
    b1 = Grafo(direcionado=True)
    b2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for vertice in b2:
        b1.inserir_vertice(vertice)
    b3 = [
        ('a', 'b', 10),
        ('a', 'c', 5),
        ('a', 'g', 1),
        ('a', 'f', 6),
        ('b', 'c', 2),
        ('b', 'd', 1),
        ('c', 'b', 3),
        ('c', 'd', 9),
        ('c', 'e', 2),
        ('c', 'g', 4),
        ('d', 'i', 4),
        ('e', 'i', 8),
        ('e', 'h', 4),
        ('e', 'd', 6),
        ('f', 'g', 6),
        ('g', 'h', 8),
        ('h', 'i', 9),
        ('j', 'a', 3),
        ('j', 'i', 5)
    ]
    for origem, destino, peso in b3:
        b1.inserir_aresta(origem, destino, peso)
    return b1
def fonk2(b1, origem):
    dijkstra(b1, origem)
    for vertice in b1.get_vertices():
        b4 = [vertice.get_id()]
        caminho_minimo(vertice, b4)
        print(f"O menor b4 é: {b4[::-1]} com custo {vertice.get_distancia()}.")
def fonk3():
    print("Testando um b1 qualquer gerado aleatoriamente por mim.")
    b5 = fonk1()
    fonk2(b5, 'a')
if b6 = = "__main__":
    fonk3()
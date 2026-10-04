from b1 import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
class class1(Exception):
    pass
def fonk1():
    b1 = Grafo(direcionado=True)
    b2 = ['a', 'b', 'c', 'd', 'e', 'f']
    for vertice in b2:
        b1.inserir_vertice(vertice)
    b3 = [
        ('b', 'a', -3),
        ('a', 'c', 5),
        ('c', 'b', 2),
        ('d', 'b', 4),
        ('d', 'c', 5),
        ('c', 'f', -3),
        ('e', 'c', 4),
        ('e', 'f', 5),
        ('f', 'd', -4)
    ]
    for origem, destino, peso in b3:
        b1.inserir_aresta(origem, destino, peso)
    return b1
def fonk2(b1, origem):
    if bellman_ford(b1, origem):
        for vertice in b1.get_vertices():
            b4 = [vertice.get_id()]
            caminho_minimo(vertice, b4)
            print(f'O menor b4 é: {b4[::-1]} com custo {vertice.get_distancia()}.')
    else:
        print('Ciclo negativo encontrado')
def fonk3():
    print("Testando um b1 com ciclo negativo")
    b5 = fonk1()
    fonk2(b5, 'a')
if b6 = = "__main__":
    fonk3()
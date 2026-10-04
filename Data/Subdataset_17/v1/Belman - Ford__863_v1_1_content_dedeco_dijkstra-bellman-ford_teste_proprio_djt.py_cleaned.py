from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minimo
class PesoNegativo(Exception):
    pass
def criar_grafo_exemplo():
    grafo = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for vertice in vertices:
        grafo.inserir_vertice(vertice)
    arestas = [
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
    for origem, destino, peso in arestas:
        grafo.inserir_aresta(origem, destino, peso)
    return grafo
def imprimir_caminhos_minimos(grafo, origem):
    dijkstra(grafo, origem)
    for vertice in grafo.get_vertices():
        caminho = [vertice.get_id()]
        caminho_minimo(vertice, caminho)
        print(f'O menor caminho é: {caminho[::-1]} com custo {vertice.get_distancia()}.')
def main():
    print("Testando um grafo qualquer gerado aleatoriamente por mim.")
    grafo_exemplo = criar_grafo_exemplo()
    imprimir_caminhos_minimos(grafo_exemplo, 'a')
if __name__ == "__main__":
    main()
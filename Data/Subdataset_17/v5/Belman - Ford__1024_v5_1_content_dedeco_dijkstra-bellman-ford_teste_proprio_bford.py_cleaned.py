from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
class PesoNegativo(Exception):
    pass
def criar_grafo_com_ciclo_negativo():
    grafo = Grafo(direcionado=True)
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    for vertice in vertices:
        grafo.inserir_vertice(vertice)
    arestas = [
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
    for origem, destino, peso in arestas:
        grafo.inserir_aresta(origem, destino, peso)
    return grafo
def imprimir_caminhos_minimos(grafo, origem):
    if bellman_ford(grafo, origem):
        for vertice in grafo.get_vertices():
            caminho = [vertice.get_id()]
            caminho_minimo(vertice, caminho)
            print(f'O menor caminho é: {caminho[::-1]} com custo {vertice.get_distancia()}.')
    else:
        print('Ciclo negativo encontrado')
def main():
    print("Testando um grafo com ciclo negativo")
    grafo_exemplo = criar_grafo_com_ciclo_negativo()
    imprimir_caminhos_minimos(grafo_exemplo, 'a')
if __name__ == "__main__":
    main()
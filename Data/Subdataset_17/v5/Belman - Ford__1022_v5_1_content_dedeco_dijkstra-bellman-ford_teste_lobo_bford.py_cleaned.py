from grafo import Grafo
from bellman_ford import bellman_ford
from utils import caminho_minimo
class PesoNegativo(Exception):
    pass
def criar_grafo_exemplo():
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
    return g
def imprimir_caminhos_minimos(grafo, origem):
    if bellman_ford(grafo, origem):
        for vertice in grafo.get_vertices():
            caminho = [vertice.get_id()]
            caminho_minimo(vertice, caminho)
            print(f'O menor caminho é: {caminho[::-1]} com custo {vertice.get_distancia()}.')
    else:
        print('Ciclo negativo encontrado')
def main():
    print("Testando grafo de exemplo das aulas do prof. Fernando Lobo da Universidade do Algarve em Portugal.")
    grafo_exemplo = criar_grafo_exemplo()
    imprimir_caminhos_minimos(grafo_exemplo, 'a')
if __name__ == "__main__":
    main()
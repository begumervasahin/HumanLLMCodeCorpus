import pandas as pd
import numpy as np
from arvore import TreeNode, Heap
class Mapa:
    def __init__(self, grafo):
        self.__grafo = grafo
    def getHeuristica(self, partida, destino):
        partida_destino = self.__grafo.at[partida, destino]
        destino_partida = self.__grafo.at[destino, partida]
        if partida_destino == -1 and destino_partida == -1:
            return -1
        elif partida_destino == -1:
            return destino_partida
        elif destino_partida == -1:
            return partida_destino
        return min(partida_destino, destino_partida)
    def getDistancia(self, partida, destino):
        partida_destino = self.__grafo.at[partida, destino]
        destino_partida = self.__grafo.at[destino, partida]
        if partida_destino == -1 or destino_partida == -1:
            return -1
        return max(partida_destino, destino_partida)
    def getVizinhos(self, cidade):
        vizinhos = self.__grafo[cidade][self.__grafo[cidade] > 0].index.tolist()
        vizinhos += self.__grafo.loc[cidade][self.__grafo.loc[cidade] > 0].index.tolist()
        return vizinhos
def BuscaAEstrela(mapa, partida, destino):
    raiz = TreeNode({"key": partida, "cost": mapa.getHeuristica(partida, destino)})
    lista_aberta = Heap()
    custo_atual = 0
    while raiz.data["key"] != destino:
        vizinhos = mapa.getVizinhos(raiz.data["key"])
        filhos = [
            {
                "key": vizinho,
                "cost": custo_atual + mapa.getHeuristica(vizinho, destino) + mapa.getDistancia(raiz.Key(), vizinho)
            }
            for vizinho in vizinhos
        ]
        filhos = raiz.AddChildren(filhos)
        lista_aberta.append(filhos)
        novo_no = lista_aberta.pop(lambda x: x.Cost())
        custo_atual += mapa.getDistancia(raiz.Key(), novo_no.Key())
        raiz = novo_no
    caminho = [raiz.Key()]
    while raiz.father is not None:
        raiz = raiz.father
        caminho.append(raiz.Key())
    caminho.reverse()
    return caminho
if __name__ == "__main__":
    grafo = pd.read_csv("grafo.csv", index_col=0).fillna(-1).astype(np.float64)
    mapa = Mapa(grafo)
    partida = input("Cidade de Partida: ")
    destino = input("Cidade de Destino: ")
    caminho = BuscaAEstrela(mapa, partida, destino)
    print(" -> ".join(caminho))
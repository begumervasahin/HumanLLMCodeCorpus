import pandas as pd
import numpy as np
from arvore import TreeNode
from arvore import Heap
class Mapa:
    def __init__(self, grafo):
        self.__grafo = grafo
    def getHeuristica(self, partida, destino):
        if self.__grafo[partida][destino] == -1:
            return self.__grafo[destino][partida]
        elif self.__grafo[destino][partida] == -1:
            return self.__grafo[partida][destino]
        return min(self.__grafo[partida][destino], self.__grafo[destino][partida])
    def getDistancia(self, partida, destino):
        if self.__grafo[partida][destino] == -1:
            return -1
        elif self.__grafo[destino][partida] == -1:
            return -1
        return max(self.__grafo[partida][destino], self.__grafo[destino][partida])
    def getVizinhos(self, cidade):
        triangulo_inf = np.tril(np.ones(self.__grafo.shape)).astype(np.bool)
        vizinhos = self.__grafo.where(triangulo_inf, -1)
        return list(vizinhos[cidade][vizinhos[cidade] > 0].index) + list(vizinhos.loc[cidade][vizinhos.loc[cidade] > 0].index)
def BuscaAEstrela(mapa, partida, destino):
    '''
        Busca A* em um mapa
    '''
    t = TreeNode({"key":partida, "cost":mapa.getHeuristica(partida, destino)})
    lista = Heap()
    custoAtual = 0
    while(t.data["key"] != destino):
        vizinhos = mapa.getVizinhos(t.data["key"])
        vizinhos = [
            {
                "key":v,
                "cost": custoAtual + mapa.getHeuristica(v, destino) + mapa.getDistancia(t.Key(), v)
            }
            for v in vizinhos
        ]
        vizinhos = t.AddChildren(vizinhos)
        lista.append(vizinhos)
        newT = lista.pop(lambda x: x.Cost())
        custoAtual += mapa.getDistancia(t.Key(), newT.Key())
        t = newT
    caminho = [t.Key()]
    while t.father is not None:
        t = t.father
        caminho.append(t.Key())
    caminho.reverse()
    return caminho
if __name__ == "__main__":
    mapa = Mapa(pd.read_csv("grafo.csv", index_col=0).fillna(-1).astype(np.float64))
    partida = input("Cidade de Partida : ")
    destino = input("Cidade de Destino : ")
    caminho = BuscaAEstrela(mapa, partida, destino)
    print("->".join(caminho))
import pandas as pd
import numpy as np
from arvore import TreeNode, Heap
class Mapa:
    def __init__(self, grafo):
        self.__grafo = grafo
    def get_heuristica(self, partida, destino):
        if self.__grafo.at[partida, destino] == -1:
            return self.__grafo.at[destino, partida]
        elif self.__grafo.at[destino, partida] == -1:
            return self.__grafo.at[partida, destino]
        return min(self.__grafo.at[partida, destino], self.__grafo.at[destino, partida])
    def get_distancia(self, partida, destino):
        if self.__grafo.at[partida, destino] == -1 or self.__grafo.at[destino, partida] == -1:
            return -1
        return max(self.__grafo.at[partida, destino], self.__grafo.at[destino, partida])
    def get_vizinhos(self, cidade):
        triangulo_inf = np.tril(np.ones(self.__grafo.shape)).astype(bool)
        vizinhos = self.__grafo.where(triangulo_inf, -1)
        return list(vizinhos[cidade][vizinhos[cidade] > 0].index) + list(vizinhos.loc[cidade][vizinhos.loc[cidade] > 0].index)
def busca_a_estrela(mapa, partida, destino):
    t = TreeNode({"key": partida, "cost": mapa.get_heuristica(partida, destino)})
    lista = Heap()
    custo_atual = 0
    while t.data["key"] != destino:
        vizinhos = mapa.get_vizinhos(t.data["key"])
        vizinhos = [
            {
                "key": v,
                "cost": custo_atual + mapa.get_heuristica(v, destino) + mapa.get_distancia(t.Key(), v)
            }
            for v in vizinhos
        ]
        vizinhos = t.add_children(vizinhos)
        lista.append(vizinhos)
        new_t = lista.pop(lambda x: x.Cost())
        custo_atual += mapa.get_distancia(t.Key(), new_t.Key())
        t = new_t
    caminho = [t.Key()]
    while t.father is not None:
        t = t.father
        caminho.append(t.Key())
    caminho.reverse()
    return caminho
if __name__ == "__main__":
    mapa = Mapa(pd.read_csv("grafo.csv", index_col=0).fillna(-1).astype(np.float64))
    partida = input("Cidade de Partida: ")
    destino = input("Cidade de Destino: ")
    caminho = busca_a_estrela(mapa, partida, destino)
    print(" -> ".join(caminho))
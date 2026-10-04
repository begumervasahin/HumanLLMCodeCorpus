import networkx as nx
class AlgoritimoKruskal:
    def __init__(self):
        self.conjunto = {}
        self.rank = {}
    def criar_conjunto(self, vertice):
        self.conjunto[vertice] = vertice
        self.rank[vertice] = 0
    def procurar(self, vertice):
        if self.conjunto[vertice] != vertice:
            self.conjunto[vertice] = self.procurar(self.conjunto[vertice])
        return self.conjunto[vertice]
    def uniao(self, vertice1, vertice2):
        raiz1 = self.procurar(vertice1)
        raiz2 = self.procurar(vertice2)
        if raiz1 != raiz2:
            if self.rank[raiz1] > self.rank[raiz2]:
                self.conjunto[raiz2] = raiz1
            else:
                self.conjunto[raiz1] = raiz2
                if self.rank[raiz1] == self.rank[raiz2]:
                    self.rank[raiz2] += 1
    def peso(self, grafo):
        arestas = list(grafo.edges.data('weight'))
        soma = sum(weight for _, _, weight in arestas)
        return soma
    def kruskal(self, grafo):
        lista_de_vertice = list(grafo.nodes())
        for vertice in lista_de_vertice:
            self.criar_conjunto(vertice)
        mst = nx.Graph()
        arestas = list(grafo.edges.data('weight'))
        arestas.sort(key=lambda x: x[2])
        for vertice1, vertice2, weight in arestas:
            if self.procurar(vertice1) != self.procurar(vertice2):
                self.uniao(vertice1, vertice2)
                mst.add_edge(vertice1, vertice2, weight=weight)
        return mst
if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge('A', 'B', weight=4)
    G.add_edge('A', 'C', weight=3)
    G.add_edge('B', 'C', weight=1)
    G.add_edge('B', 'D', weight=2)
    G.add_edge('C', 'D', weight=4)
    G.add_edge('C', 'E', weight=2)
    G.add_edge('D', 'E', weight=3)
    algoritmo = AlgoritimoKruskal()
    mst = algoritmo.kruskal(G)
    print("Minimum Spanning Tree:")
    print(mst.edges(data=True))
    print("Total Weight:", algoritmo.peso(mst))
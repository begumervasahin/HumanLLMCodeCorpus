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
    def calcular_peso(self, grafo):
        return sum(weight for _, _, weight in grafo.edges.data('weight'))
    def kruskal(self, grafo):
        for vertice in grafo.nodes():
            self.criar_conjunto(vertice)
        mst = nx.Graph()
        arestas = sorted(grafo.edges.data('weight'), key=lambda x: x[2])
        for vertice1, vertice2, weight in arestas:
            if self.procurar(vertice1) != self.procurar(vertice2):
                self.uniao(vertice1, vertice2)
                mst.add_edge(vertice1, vertice2, weight=weight)
        return mst
if __name__ == "__main__":
    G = nx.Graph()
    edges = [
        ('A', 'B', 4), ('A', 'C', 3), ('B', 'C', 1),
        ('B', 'D', 2), ('C', 'D', 4), ('C', 'E', 2), ('D', 'E', 3)
    ]
    G.add_weighted_edges_from(edges)
    algoritmo = AlgoritimoKruskal()
    mst = algoritmo.kruskal(G)
    print("Minimum Spanning Tree:")
    for edge in mst.edges(data=True):
        print(edge)
    print("Total Weight:", algoritmo.calcular_peso(mst))
import networkx as nx
class Algoritimo_kruskal():
    conjunto = dict()
    rank = dict()
    def criar_conjunto(self, vertice):
        self.conjunto[vertice] = vertice
        self.rank[vertice] = 0
    def procurar(self, vertice):
        v = vertice
        while self.conjunto[vertice] != vertice:
            vertice = self.conjunto[vertice]
        self.conjunto[v] = self.conjunto[vertice]
        return self.conjunto[vertice]
    def uniao(self, vertice1, vertice2):
        raiz1 = self.procurar(vertice1)
        raiz2 = self.procurar(vertice2)
        if raiz1 != raiz2:
            if self.rank[raiz1] > self.rank[raiz2]:
                self.conjunto[raiz2] = raiz1
            else:
                self.conjunto[raiz1] = raiz2
                if self.rank[raiz1] == self.rank[raiz2]: self.rank[raiz2] += 1
    def peso(self, grafo):
        arestas = list(grafo.edges.data('weight'))
        soma = 0
        for aresta in arestas:
            vertice1, vertice2, weight = aresta
            soma += weight
        return soma
    def kruskal(self, grafo):
        lista_de_vertice = list(grafo.nodes())
        for vertice in lista_de_vertice:
            self.criar_conjunto(vertice)
        mst = nx.Graph()
        arestas = list(grafo.edges.data('weight'))
        arestas.sort(key = lambda x: x[2])
        for aresta in arestas:
            vertice1, vertice2, weight = aresta
            if self.procurar(vertice1) != self.procurar(vertice2):
                self.uniao(vertice1, vertice2)
                mst.add_edge(aresta[0], aresta[1], weight = aresta[2])
        return mst
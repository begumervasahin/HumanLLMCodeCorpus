import networkx as nx
from random import randint
class in_mat():
    def __init__(self):
        self.quant_vert = 0
        self.matriz = []
    def to_mat(self):
        """
        self.quant_vert = int(input("Digite a quantidade de vertices: "))
        >>>esse valor agora virÃ¡ da interface
        print("Digite a matriz de adjacencia: ")
        for x in range(0,self.quant_vert):
            n = input()
            m = list(map(int, n.split(" ")))
            self.matriz.append(m)
        for i in range(0,len(self.matriz)):
            [int(elem) for elem in self.matriz[i]]
        >>>esse valor agora virÃ¡ de um arquivo
        """
    def to_graph(self):
        G = nx.Graph()
        for z in range(0,int(self.quant_vert)):
            G.add_node(z)
        for x in range(0,int(self.quant_vert)):
            for y in range(0,int(self.quant_vert)):
                if x <= y:
                    if int(self.matriz[x][y]) > 0:
                        n = int(self.matriz[x][y])
                        G.add_edge (x,y,weight = n)
        return G
    def random_g(self):
        n = self.quant_vert
        print(n)
        G = nx.connected_watts_strogatz_graph(n,randint(int(n/2),n-1),0.5,100,randint(1,100))
        a = G.edges()
        self.matriz = []
        for i in range(n):
            self.matriz.append([0]*n)
        for v1,v2 in a:
            n = randint(1,50)
            self.matriz[v1][v2] = n
            self.matriz[v2][v1] = n
            G.edges[v1,v2]['weight']=n
        self.quant_vert = G.number_of_nodes()
        return G
    def get_matriz_adj(self):
        return self.matriz
    def mat_clear(self):
        self.quant_vert = 0
        self.matriz = []
    def graph_comp(self):
        v = int(input("Digite a quantidade de vertices para gerar um grafo completo: "))
        G = nx.complete_graph(v)
        self.quant_vert = G.number_of_nodes()
        a = G.edges()
        self.matriz = []
        for i in range(v):
            self.matriz.append([0]*v)
        for v1,v2 in a:
            n = randint(1,50)
            self.matriz[v1][v2] = n
            self.matriz[v2][v1] = n
            G.edges[v1,v2]['weight']=n
        return G
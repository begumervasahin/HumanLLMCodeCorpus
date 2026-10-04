import networkx as nx
from random import randint
class class1():
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self):
        """
        self.a1 = int(input("Digite b6 quantidade de vertices: "))
        >>>esse valor agora virÃ¡ da interface
        print("Digite b6 b1 de adjacencia: ")
        for x in range(0,self.a1):
            b2 = input()
            b3 = list(map(int, b2.split(" ")))
            self.b1.append(b3)
        for i in range(0,len(self.b1)):
            [int(elem) for elem in self.b1[i]]
        >>>esse valor agora virÃ¡ de um arquivo
        """
    def fonk3(self):
        b4 = nx.Graph()
        for z in range(0,int(self.a1)):
            b4.add_node(z)
        for x in range(0,int(self.a1)):
            for y in range(0,int(self.a1)):
                if x <= y:
                    if int(self.b1[x][y]) > 0:
                        b2 = int(self.b1[x][y])
                        b4.add_edge (x,y,b5 = b2)
        return b4
    def fonk4(self):
        b2 = self.a1
        print(b2)
        b4 = nx.connected_watts_strogatz_graph(b2,randint(int(b2/2),b2-1),0.5,100,randint(1,100))
        b6 = b4.edges()
        self.b1 = []
        for i in range(b2):
            self.b1.append([0]*b2)
        for v1,v2 in b6:
            b2 = randint(1,50)
            self.b1[v1][v2] = b2
            self.b1[v2][v1] = b2
            b4.edges[v1,v2]['b5']=b2
        self.a1 = b4.number_of_nodes()
        return b4
    def fonk5(self):
        return self.b1
    def fonk6(self):
        self.a1 = 0
        self.b1 = []
    def fonk7(self):
        b7 = int(input("Digite b6 quantidade de vertices para gerar um grafo completo: "))
        b4 = nx.complete_graph(b7)
        self.a1 = b4.number_of_nodes()
        b6 = b4.edges()
        self.b1 = []
        for i in range(b7):
            self.b1.append([0]*b7)
        for v1,v2 in b6:
            b2 = randint(1,50)
            self.b1[v1][v2] = b2
            self.b1[v2][v1] = b2
            b4.edges[v1,v2]['b5']=b2
        return b4
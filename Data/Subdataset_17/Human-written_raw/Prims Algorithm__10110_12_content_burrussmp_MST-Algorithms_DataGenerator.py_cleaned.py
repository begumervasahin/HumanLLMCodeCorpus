import random
import math
class Adjacency_List:
    def __init__(self,vertices,edges):
        self.adj = [[] for i in range(len(vertices))]
        self.vertices = vertices
        self.edges = edges
        for edge in edges:
            self.adj[edge.u].append((edge.v,edge.weight))
            self.adj[edge.v].append((edge.u,edge.weight))
    def addEdge(self,edge):
        self.edges.append(edge)
        self.adj[edge.u].append((edge.v,edge.weight))
        self.adj[edge.v].append((edge.u,edge.weight))
    def printMe(self):
        node = 0
        for list in self.adj:
            print("%d:" %node,end='')
            node = node + 1
            for edge in list:
                print(" (%d:%0.2f)" % (edge[0],edge[1]),end='')
            print('')
    def adjacentTo(self,u,index):
        return self.adj[u][index][0],self.adj[u][index][1]
    def numberOfNeighborsTo(self,u):
        return len(self.adj[u])
    def getNumberOfVertices(self):
        return len(self.vertices)
    def getEdges(self):
        return self.edges
    def getVertices(self):
        return self.vertices
class Edge:
    def __init__(self,u,v,weight):
        self.u = u
        self.v = v
        self.weight = weight
    def printMe(self):
        print("edge:(" + str(self.u) + "--" + str(self.v) + ") with weight " + str(self.weight))
class DataGenerator:
    def __init__(self,n,p,method=1,weightMax = 30,xlim=100,ylim=100,seed = 3141):
        self.n = n
        self.p = p
        self.method = method
        self.weightMax = 30
        self.xlim = xlim
        self.ylim = ylim
        random.seed(seed)
    def generateData(self):
        if (self.method == 1):
            return self.method1()
        elif(self.method == 2):
            return self.method2()
        else:
            print("Method not defined")
            return Adjacency_List([],[])
    def method1(self):
        vertices = []
        for i in range(self.n):
            vertices.append(i)
        edges = []
        for i in range(self.n):
            for j in range(i+1,self.n):
                randomNumber = random.randint(1,10001)
                if (randomNumber <= self.p*10000):
                    randomWeight = random.randint(1,self.weightMax+1)
                    edges.append(Edge(i,j,randomWeight))
        return Adjacency_List(vertices,edges)
    def method2(self):
        vertices = []
        x = []
        y = []
        for i in range(self.n):
            vertices.append(i)
            x.append(random.randint(1,self.xlim+1))
            y.append(random.randint(1,self.ylim+1))
        edges = []
        for i in range(self.n):
            for j in range(i+1,self.n):
                randomNumber = random.randint(1,10001)
                if (randomNumber <= self.p*10000):
                    weight = math.sqrt((x[i]-x[j])**2 +(y[i]-y[j])**2)
                    edges.append(Edge(i,j,weight))
        return Adjacency_List(vertices,edges)
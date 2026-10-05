import sys
class class1:
    def fonk1(self, v):
        self.b1 = v
        self.b2 = [{}]
        self.b2.clear()
        self.b3 = []
        self.b3.clear()
        self.b4 = []
        self.b4.clear()
        self.b5 = []
        self.b5.clear()
        for a2 in range(v):
            self.b2.append({})
        for j in range(v):
            self.b3.append(sys.maxsize)
        for k in range(v):
            self.b4.append(False)
    def fonk2(self):
        for a2 in range(0,self.b1):
            print ("For",a2,"=",self.b2[a2])
    def fonk3(self):
        for a2 in range(self.b1):
            print ("Bellman-Ford",a2,"=",self.b3[a2])
def fonk4(graph, src, dest, weight):
    graph.b2[src].__setitem__(dest,weight)
def fonk5(graph):
    while graph.b5 != list():
        fonk6(graph, graph.b5.pop())
def fonk6(graph, source):
    if graph.b4[source] == True:
        return
    b6 = []
    b6.clear()
    a1 = 0
    b7 = sys.maxsize
    for a2 in range(graph.b2[source].__len__()):
        b8 = graph.b3[source] + graph.b2[source][list(graph.b2[source].keys())[a2]]
        b6.append(b8)
        if graph.b3[list(graph.b2[source].keys())[a2]] > b8:
            graph.b3[list(graph.b2[source].keys())[a2]] = b8
            graph.b5.insert(0,list(graph.b2[source].keys())[a2])
            graph.b4[list(graph.b2[source].keys())[a2]] = False
    a2 = 0
    for a2 in range(graph.b2[source].__len__()):
        if graph.b4[list(graph.b2[source].keys())[a2]] == False and list(graph.b2[source].keys())[a2] not in graph.b5:
            graph.b5.insert(0,list(graph.b2[source].keys())[a2])
    graph.b4[source] = True
def fonk7(graph, source):
    graph.b3[source] = 0
    graph.b5.insert(0,source)
    fonk4(graph, 0, 1, 4)
    fonk4(graph, 0, 2, 2)
    fonk4(graph, 1, 2, 3)
    fonk4(graph, 1, 3, 2)
    fonk4(graph, 1, 4, 3)
    fonk4(graph, 2, 1, 1)
    fonk4(graph, 2, 3, 4)
    fonk4(graph, 2, 4, 5)
    fonk4(graph, 4, 3, -5)
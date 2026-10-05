33. Repository: gquintela/bfs
   File: graph.py
   URL: https:
   Code Content:
class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
    def fonk2(self):
        b2 = []
        for vertex in self.b1:
            b2.append(vertex)
        return b2
    def fonk3(self, v):
        b3 = []
        for neighbour in self.b1[v]:
            b3.append(neighbour)
        return b3
    def fonk4(self):
        print ("Vertices:")
        for vertex in self.b1:
            print(vertex)
        print('\n')
    def fonk5(self, v):
        print ("Neighbours of " + v)
        for neighbour in self.b1[v]:
            print (neighbour[0] + ", weight of edge: " + str(neighbour[1]))
    def fonk6(self, v):
        self.b1[v] = []
    def fonk7(self, u, v):
        if u not in self.b1:
            self.fonk6(u)
        if v not in self.b1:
            self.fonk6(v)
        self.b1[u].append(v)
    def fonk8(self, u, v):
        self.fonk7(u, v)
        self.fonk7(v, u)
   README Content:
breadth-first search algorithm written in Python

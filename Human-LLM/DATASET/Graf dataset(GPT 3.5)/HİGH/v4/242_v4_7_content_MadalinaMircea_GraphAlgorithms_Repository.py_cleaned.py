
from Graph import Graph
class class1:
    def fonk1(self, b1 = "graph1.txt"):
        self.fonk2(b1)
    def fonk2(self, b1):
        b2 = open(b1, 'r')
        b3 = b2.readline()
        b3 = b3.split()
        self.b4 = Graph(int(b3[0]))
        b3 = b2.readline()
        while b3 != '':
            b3 = b3.split()
            self.b4.fonk9(int(b3[0]), int(b3[1]))
            self.b4.fonk9(int(b3[1]), int(b3[0]))
            b3 = b2.readline()
        b2.close()
    def fonk3(self):
        return self.b4.fonk3()
    def fonk4(self, g):
        return g.fonk4()
    def fonk5(self, v1, v2):
        return self.b4.fonk5(v1, v2)
    def fonk6(self, v):
        return self.b4.fonk6(v)
    def fonk7(self, v):
        return self.b4.parseNeighbours(v)
    def fonk8(self):
        return self.b4.parseAll()
    def fonk9(self, v1, v2, c):
        return self.b4.fonk9(v1, v2, c)
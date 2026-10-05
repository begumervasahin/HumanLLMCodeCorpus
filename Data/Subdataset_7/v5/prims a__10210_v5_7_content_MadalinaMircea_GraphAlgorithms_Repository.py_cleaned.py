
from Graph import Graph
class class1:
    def fonk1(self, b1 = "graph1.txt"):
        self.fonk2(b1)
    def fonk2(self, b1):
        with open(b1, 'r') as file:
            b2 = int(file.readline().split()[0])
            self.b3 = Graph(b2)
            for line in file:
                v1, b4 = map(int, line.split())
                self.b3.fonk9(v1, b4)
                self.b3.fonk9(b4, v1)
    def fonk3(self):
        return self.b3.fonk3()
    def fonk4(self):
        return self.b3.fonk4()
    def fonk5(self, v1, b4):
        return self.b3.fonk5(v1, b4)
    def fonk6(self, v):
        return self.b3.fonk6(v)
    def fonk7(self, v):
        return self.b3.fonk7(v)
    def fonk8(self):
        return self.b3.get_all_vertices()
    def fonk9(self, v1, b4, b5 = None):
        return self.b3.fonk9(v1, b4, b5)
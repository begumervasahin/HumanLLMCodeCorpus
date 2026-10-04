from random import randint
class class1:
    def fonk1(self, b1 = None, numVertices = None, numEdges = None, b5 = None, directed = True):
        self.b2 = {}
        self.b3 = {}
        if b1 = = None:
            if any(b4 = = None for b4 in (numVertices, numEdges, b5)):
                numVertices, numEdges, b5 = map(int, input("numVertices, numEdges, b5: ").split())
            self.fonk7(numVertices, numEdges, b5, directed)
        else:
            self.fonk8(b1, directed)
    def fonk2(self):
        return len(self.b2)
    def fonk3(self):
        return range(self.fonk2())
    def fonk4(self):
        return ((b7,b8) for b7 in self.fonk3() for b8 in self.b2[b7])
    def fonk5(self, b7, b8, b3):
        self.b2.setdefault(b7, set()).add(b8)
        self.b3[(b7, b8)] = b3
    def fonk6(self, b7, b8, b3):
        self.fonk5(b7, b8, b3)
        self.fonk5(b8, b7, b3)
    def fonk7(self, numVertices, numEdges, b5, directed):
        b6 = self.addDirectedEdge if directed else self.addUndirectedEdge
        for vertex in range(numVertices):
            self.b2[vertex] = set()
        for edge in range(numEdges):
            b7 = b8 = None
            while b7 = = b8:
                b7 = randint(0, numVertices-1)
                b8 = randint(0, numVertices-1)
            b3 = randint(0, b5)
            b6(b7, b8, b3)
    def fonk8(b1, directed):
        b6 = self.addDirectedEdge if directed else self.addUndirectedEdge
        with open(b1, 'r') as f:
            for vertex in range(int(f.readline())):
                self.b2[vertex] = set()
            for line in f.readlines():
                b7, b8, b3 = map(int, line.split())
                b6(b7, b8, b3)
    def fonk9(self, b7):
        return ", ".join(f"({b8}, {self.b3[(b7, b8)]})" for b8 in self.b2[b7])
    def fonk10(self):
        return "\n".join(f"{vertex}: {self.fonk9(vertex)}" for vertex in range(self.fonk2()))
    def fonk11(self):
        return str(self)
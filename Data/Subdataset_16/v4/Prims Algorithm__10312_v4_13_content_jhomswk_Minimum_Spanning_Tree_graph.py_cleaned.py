from random import randint
class class1:
    def fonk1(self, b1 = None, numVertices=None, numEdges=None, b4=None, directed=True):
        self.b2 = {}
        self.b3 = {}
        if b1 is None:
            if any(arg is None for arg in (numVertices, numEdges, b4)):
                numVertices, numEdges, b4 = map(int, input("Enter numVertices, numEdges, b4: ").split())
            self.fonk7(numVertices, numEdges, b4, directed)
        else:
            self.fonk8(b1, directed)
    def fonk2(self):
        return len(self.b2)
    def fonk3(self):
        return range(self.fonk2())
    def fonk4(self):
        return ((b6, b7) for b6 in self.fonk3() for b7 in self.b2[b6])
    def fonk5(self, b6, b7, b3):
        self.b2.setdefault(b6, set()).add(b7)
        self.b3[(b6, b7)] = b3
    def fonk6(self, b6, b7, b3):
        self.fonk5(b6, b7, b3)
        self.fonk5(b7, b6, b3)
    def fonk7(self, numVertices, numEdges, b4, directed):
        b5 = self.add_directed_edge if directed else self.add_undirected_edge
        for vertex in range(numVertices):
            self.b2[vertex] = set()
        for _ in range(numEdges):
            b6 = b7 = None
            while b6 = = b7:
                b6 = randint(0, numVertices - 1)
                b7 = randint(0, numVertices - 1)
            b3 = randint(0, b4)
            b5(b6, b7, b3)
    def fonk8(self, b1, directed):
        b5 = self.add_directed_edge if directed else self.add_undirected_edge
        with open(b1, 'r') as f:
            for vertex in range(int(f.readline().strip())):
                self.b2[vertex] = set()
            for line in f:
                b6, b7, b3 = map(int, line.split())
                b5(b6, b7, b3)
    def fonk9(self, b6):
        return ", ".join(f"({b7}, {self.b3[(b6, b7)]})" for b7 in self.b2[b6])
    def fonk10(self):
        return "\n".join(f"{vertex}: {self.fonk9(vertex)}" for vertex in range(self.fonk2()))
    def fonk11(self):
        return str(self)
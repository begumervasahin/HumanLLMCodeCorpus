from random import randint
class class1:
    def fonk1(self, b1 = None, b10=None, num_edges=None, b5=None, b4=True):
        self.b2 = {}
        self.b3 = {}
        self.b4 = b4
        if b1 is None:
            if any(arg is None for arg in (b10, num_edges, b5)):
                b10, num_edges, b5 = map(int, input("Enter b10, num_edges, b5: ").split())
            self.fonk7(b10, num_edges, b5)
        else:
            self.fonk8(b1)
    def fonk2(self):
        return len(self.b2)
    def fonk3(self):
        return range(self.fonk2())
    def fonk4(self):
        return ((b8, b7) for b8 in self.fonk3() for b7 in self.b2[b8])
    def fonk5(self, b8, b7, b9):
        self.b2.setdefault(b8, set()).add(b7)
        self.b3[(b8, b7)] = b9
    def fonk6(self, b8, b7, b9):
        self.fonk5(b8, b7, b9)
        self.fonk5(b7, b8, b9)
    def fonk7(self, b10, num_edges, b5):
        b6 = self.add_directed_edge if self.b4 else self.add_undirected_edge
        for vertex in range(b10):
            self.b2[vertex] = set()
        for _ in range(num_edges):
            b8, b7 = None, None
            while b8 = = b7:
                b8 = randint(0, b10 - 1)
                b7 = randint(0, b10 - 1)
            b9 = randint(0, b5)
            b6(b8, b7, b9)
    def fonk8(self, b1):
        b6 = self.add_directed_edge if self.b4 else self.add_undirected_edge
        with open(b1, 'r') as file:
            b10 = int(file.readline().strip())
            for vertex in range(b10):
                self.b2[vertex] = set()
            for line in file:
                b8, b7, b9 = map(int, line.split())
                b6(b8, b7, b9)
    def fonk9(self, b8):
        return ", ".join(f"({b7}, {self.b3[(b8, b7)]})" for b7 in self.b2[b8])
    def fonk10(self):
        return "\n".join(f"{vertex}: {self.fonk9(vertex)}" for vertex in self.fonk3())
    def fonk11(self):
        return str(self)
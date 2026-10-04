class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
    def fonk2(self):
        return list(self.b1.keys())
    def fonk3(self, v):
        return self.b1[v]
    def fonk4(self):
        print("Vertices:")
        for vertex in self.b1:
            print(vertex)
        print('\n')
    def fonk5(self, v):
        print("Neighbours of " + v)
        for neighbour in self.b1[v]:
            print(neighbour)
        print('\n')
    def fonk6(self, v):
        if v not in self.b1:
            self.b1[v] = []
    def fonk7(self, u, v):
        self.fonk6(u)
        self.fonk6(v)
        self.b1[u].append(v)
        self.b1[v].append(u)
    def fonk8(self, u, v):
        self.fonk6(u)
        self.fonk6(v)
        self.b1[u].append(v)
if b2 = = "__main__":
    b3 = class1()
    b3.fonk6('A')
    b3.fonk6('B')
    b3.fonk6('C')
    b3.fonk7('A', 'B')
    b3.fonk7('A', 'C')
    b3.fonk8('B', 'C')
    b3.fonk4()
    b3.fonk5('A')
    b3.fonk5('B')
    b3.fonk5('C')
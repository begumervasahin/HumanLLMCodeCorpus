
class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
    def fonk2(self):
        return list(self.b1.keys())
    def fonk3(self, v):
        return self.b1.get(v, [])
    def fonk4(self):
        print("Vertices:")
        for vertex in self.b1:
            print(vertex)
        print('\n')
    def fonk5(self, v):
        print("Neighbours of", v)
        b2 = self.b1.get(v, [])
        for neighbour, weight in b2:
            print(neighbour + ", weight of edge:", weight)
    def fonk6(self, v):
        if v not in self.b1:
            self.b1[v] = []
    def fonk7(self, u, v):
        if u not in self.b1:
            self.fonk6(u)
        if v not in self.b1:
            self.fonk6(v)
        self.b1[u].append((v, 0))
        self.b1[v].append((u, 0))
    def fonk8(self, u, v):
        self.fonk7(u, v)
        self.b1[v].append((u, 0))

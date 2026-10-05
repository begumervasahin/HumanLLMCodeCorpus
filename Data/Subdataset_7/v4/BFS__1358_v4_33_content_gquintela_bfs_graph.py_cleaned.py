class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
    def fonk2(self):
        return list(self.b1.keys())
    def fonk3(self, v):
        return self.b1[v] if v in self.b1 else []
    def fonk4(self):
        print("Vertices:")
        for vertex in self.b1:
            print(vertex)
        print('\n')
    def fonk5(self, v):
        print("Neighbours of " + v)
        for neighbour in self.b1.get(v, []):
            print(neighbour[0] + ", weight of edge: " + str(neighbour[1]))
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
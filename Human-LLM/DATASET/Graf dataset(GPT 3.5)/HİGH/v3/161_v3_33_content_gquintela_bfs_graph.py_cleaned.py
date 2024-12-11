class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
    def fonk2(self):
        return list(self.b1.keys())
    def fonk3(self, vertex):
        return self.b1.get(vertex, [])
    def fonk4(self):
        print("Vertices:")
        for vertex in self.b1:
            print(vertex)
        print('\n')
    def fonk5(self, vertex):
        print("Neighbours of", vertex)
        b2 = self.b1.get(vertex, [])
        for neighbour, weight in b2:
            print(neighbour + ", weight of edge:", weight)
    def fonk6(self, vertex):
        if vertex not in self.b1:
            self.b1[vertex] = []
    def fonk7(self, u, v):
        self.fonk6(u)
        self.fonk6(v)
        self.b1[u].append((v, 0))
        self.b1[v].append((u, 0))
    def fonk8(self, u, v):
        self.fonk7(u, v)
        self.b1[v].append((u, 0))

class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
    def fonk2(self):
        return list(self.b1.keys())
    def fonk3(self, vertex):
        return self.b1[vertex] if vertex in self.b1 else []
    def fonk4(self):
        print("Vertices:")
        for vertex in self.b1:
            print(vertex)
        print('\n')
    def fonk5(self, vertex):
        print("Neighbors of " + vertex)
        for neighbor in self.b1.get(vertex, []):
            print(neighbor)
    def fonk6(self, vertex):
        if vertex not in self.b1:
            self.b1[vertex] = []
    def fonk7(self, u, v):
        if u not in self.b1:
            self.fonk6(u)
        if v not in self.b1:
            self.fonk6(v)
        self.b1[u].append(v)
        self.b1[v].append(u)
    def fonk8(self, u, v):
        if u not in self.b1:
            self.fonk6(u)
        if v not in self.b1:
            self.fonk6(v)
        self.b1[u].append(v)
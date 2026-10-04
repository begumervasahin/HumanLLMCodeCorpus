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
        print()
    def fonk5(self, v):
        if v in self.b1:
            print(f"Neighbours of {v}:")
            for neighbour, b2 in self.b1[v]:
                print(f"{neighbour}, b2 of edge: {b2}")
        else:
            print(f"Vertex {v} does not exist in the b4.")
    def fonk6(self, v):
        if v not in self.b1:
            self.b1[v] = []
    def fonk7(self, u, v, b2 = 1):
        self.fonk6(u)
        self.fonk6(v)
        self.b1[u].append((v, b2))
        self.b1[v].append((u, b2))
    def fonk8(self, u, v, b2 = 1):
        self.fonk6(u)
        self.b1[u].append((v, b2))
if b3 = = "__main__":
    b4 = class1()
    b4.fonk7('A', 'B')
    b4.fonk7('A', 'C')
    b4.fonk8('B', 'D')
    b4.fonk4()
    b4.fonk5('A')
    b4.fonk5('B')
    b4.fonk5('C')
    b4.fonk5('D')
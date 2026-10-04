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
        print()
    def fonk5(self, vertex):
        if vertex in self.b1:
            print(f"Neighbours of {vertex}:")
            for neighbour, b2 in self.b1[vertex]:
                print(f"{neighbour}, b2 of edge: {b2}")
        else:
            print(f"Vertex {vertex} does not exist in the b4.")
    def fonk6(self, vertex):
        if vertex not in self.b1:
            self.b1[vertex] = []
    def fonk7(self, vertex1, vertex2, b2 = 1):
        self.fonk6(vertex1)
        self.fonk6(vertex2)
        self.b1[vertex1].append((vertex2, b2))
        self.b1[vertex2].append((vertex1, b2))
    def fonk8(self, source, destination, b2 = 1):
        self.fonk6(source)
        self.b1[source].append((destination, b2))
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
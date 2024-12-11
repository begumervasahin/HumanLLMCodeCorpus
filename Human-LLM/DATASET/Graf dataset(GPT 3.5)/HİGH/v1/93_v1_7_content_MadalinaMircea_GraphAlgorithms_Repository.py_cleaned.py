class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = [[] for _ in range(b1)]
    def fonk2(self, v1, b9, b3 = 1):
        self.b2[v1].append((b9, b3))
    def fonk3(self):
        return self.b1
    def fonk4(self):
        b4 = sum(len(edges) for edges in self.b2)
        return b4
    def fonk5(self, v1, b9):
        return any(b9 in neighbors for neighbors in self.b2[v1])
    def fonk6(self, v):
        return len(self.b2[v])
    def fonk7(self, v):
        return [neighbor[0] for neighbor in self.b2[v]]
    def fonk8(self):
        b5 = []
        for v in range(self.b1):
            for neighbor, _ in self.b2[v]:
                b5.append((v, neighbor))
        return b5
class class2:
    def fonk9(self, b6 = "graph1.txt"):
        self.fonk10(b6)
    def fonk10(self, b6):
        try:
            with open(b6, 'r') as file:
                b7 = file.readline()
                b1 = int(b7.strip())
                self.b8 = class1(b1)
                for line in file:
                    v1, b9 = map(int, line.split())
                    self.b8.fonk17(v1, b9)
                    self.b8.fonk17(b9, v1)
        except FileNotFoundError:
            print("File not found.")
    def fonk11(self):
        return self.b8.fonk11()
    def fonk12(self):
        return self.b8.fonk12()
    def fonk13(self, v1, b9):
        return self.b8.fonk13(v1, b9)
    def fonk14(self, v):
        return self.b8.fonk14(v)
    def fonk15(self, v):
        return self.b8.fonk7(v)
    def fonk16(self):
        return self.b8.fonk8()
    def fonk17(self, v1, b9, b3 = 1):
        return self.b8.fonk17(v1, b9, b3)
b10 = class2("graph1.txt")
print("Number of vertices:", b10.fonk11())
print("Number of edges:", b10.fonk12())
print("Is there an edge between vertices 1 and 2?", b10.fonk13(1, 2))
print("Degree of vertex 1:", b10.fonk14(1))
print("Neighbours of vertex 1:", b10.fonk15(1))
print("All edges in the b8:", b10.fonk16())
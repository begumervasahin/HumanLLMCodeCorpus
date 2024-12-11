class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = float('inf')
        self.b3 = []
        self.b4 = None
        self.b5 = False
    def fonk2(self):
        return self.b2
    def fonk3(self, distance):
        self.b2 = distance
    def fonk4(self):
        return self.b4
    def fonk5(self, edge):
        self.b3.append(edge)
    def fonk6(self):
        return self.b3
    def fonk7(self, prev_vertex):
        self.b4 = prev_vertex
    def fonk8(self):
        return self.b5
    def fonk9(self, b5):
        self.b5 = b5
    def fonk10(self):
        return self.b1
if b6 = = "__main__":
    b7 = class1('A')
    b8 = class1('B')
    b9 = class1('C')
    b10 = Edge(b7, b8, 10)
    b11 = Edge(b8, b9, 5)
    b12 = Edge(b9, b7, -15)
    b7.fonk5(b10)
    b8.fonk5(b11)
    b9.fonk5(b12)
    print("class1 ID:", b7)
    print("Adjacent Vertices:", [str(edge.target) for edge in b7.fonk6()])
    print("Minimum Distance:", b7.fonk2())
    print("Previous class1:", b7.fonk4())
    print("Visited:", b7.fonk8())
    b7.fonk3(20)
    b7.fonk7(b9)
    b7.fonk9(True)
    print("Updated Minimum Distance:", b7.fonk2())
    print("Updated Previous class1:", b7.fonk4())
    print("Updated Visited:", b7.fonk8())
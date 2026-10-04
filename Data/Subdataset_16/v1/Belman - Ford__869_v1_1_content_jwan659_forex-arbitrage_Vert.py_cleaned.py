from Edges import Edge
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
    def fonk5(self, b4):
        self.b4 = b4
    def fonk6(self, edge):
        self.b3.append(edge)
    def fonk7(self):
        return self.b3
    def fonk8(self):
        return self.b5
    def fonk9(self, b5):
        self.b5 = b5
    def fonk10(self):
        return self.b1
if b6 = = "__main__":
    b7 = class1('A')
    b8 = class1('B')
    b9 = Edge(b7, b8, 10)
    b7.fonk6(b9)
    b7.fonk3(0)
    b8.fonk3(10)
    b7.fonk9(True)
    print(f"class1 A: {b7}, Min Distance: {b7.fonk2()}, Visited: {b7.fonk8()}")
    print(f"class1 B: {b8}, Min Distance: {b8.fonk2()}, Visited: {b8.fonk8()}")
    print(f"Edges from class1 A: {[str(edge.target) for edge in b7.fonk7()]}")
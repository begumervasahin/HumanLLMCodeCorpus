class class1:
    def fonk1(self, vertex):
        self.b1 = vertex
        self.b2 = []
    def fonk2(self, neighbor):
        if isinstance(neighbor, class1):
            if neighbor.b1 not in self.b2:
                self.b2.append(neighbor.b1)
                neighbor.b2.append(self.b1)
                self.b2 = sorted(self.b2)
                neighbor.b2 = sorted(neighbor.b2)
        else:
            return False
    def fonk3(self):
        return str(self.b2)
if b3 = = "__main__":
    b4 = class1("A")
    b5 = class1("B")
    b6 = class1("C")
    b4.fonk2(b5)
    b4.fonk2(b6)
    print(f"Neighbors of {b4.b1}: {b4}")
    print(f"Neighbors of {b5.b1}: {b5}")
    print(f"Neighbors of {b6.b1}: {b6}")
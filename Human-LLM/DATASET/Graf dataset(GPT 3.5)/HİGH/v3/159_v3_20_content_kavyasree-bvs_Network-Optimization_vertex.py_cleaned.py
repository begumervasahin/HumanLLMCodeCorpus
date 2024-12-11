class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, neighbor):
        if isinstance(neighbor, class1):
            if neighbor.b1 not in self.b2:
                self.b2.append(neighbor.b1)
                neighbor.b2.append(self.b1)
                self.fonk3()
                neighbor.fonk3()
    def fonk3(self):
        self.b2.sort()
    def fonk4(self):
        return str(self.b2)
if b3 = = "__main__":
    b4 = class1("A")
    b5 = class1("B")
    b6 = class1("C")
    b4.fonk2(b5)
    b4.fonk2(b6)
    b5.fonk2(b6)
    for vertex in [b4, b5, b6]:
        print("Neighbors of vertex", vertex.b1, ":", vertex)
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
    def fonk2(self, b5):
        self.b4 = float('inf')
        self.b5 = b5
        self.b6 = []
    def fonk3(self):
        return self.b4
    def fonk4(self, distance):
        self.b4 = distance
    def fonk5(self):
        return self.b7
    def fonk6(self, edge):
        self.b6.append(edge)
    def fonk7(self):
        return self.b6
    def fonk8(self, b7):
        self.b7 = b7
    def fonk9(self):
        return self.b8
    def fonk10(self, b8):
        self.b8 = b8
    def fonk11(self):
        return self.b5
if b9 = = "__main__":
    b10 = class2('A')
    b11 = class2('B')
    b12 = class2('C')
    b13 = class1(b10, b11, 10)
    b14 = class1(b11, b12, 5)
    b15 = class1(b12, b10, -15)
    b10.fonk6(b13)
    b11.fonk6(b14)
    b12.fonk6(b15)
    print("class2 ID:", b10)
    print("Adjacent Vertices:", [str(edge.b2) for edge in b10.fonk7()])
    print("Minimum Distance:", b10.fonk3())
    print("Previous class2:", b10.fonk5())
    print("Visited:", b10.fonk9())
    b10.fonk4(20)
    b10.fonk8(b12)
    b10.fonk10(True)
    print("Updated Minimum Distance:", b10.fonk3())
    print("Updated Previous class2:", b10.fonk5())
    print("Updated Visited:", b10.fonk9())
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
    def fonk2(self, b4):
        self.b4 = b4
        self.b5 = float('inf')
        self.b6 = []
        self.b7 = None
        self.b8 = False
    def fonk3(self):
        return self.b4
    def fonk4(self):
        return self.b5
    def fonk5(self, distance):
        self.b5 = distance
    def fonk6(self):
        return self.b7
    def fonk7(self, b7):
        self.b7 = b7
    def fonk8(self, edge):
        self.b6.append(edge)
    def fonk9(self):
        return self.b6
    def fonk10(self):
        return self.b8
    def fonk11(self, b8):
        self.b8 = b8
    def fonk12(self):
        return str(self.b4)
if b9 = = "__main__":
    b10 = class2('A')
    b11 = class2('B')
    b12 = class2('C')
    b13 = class1(b10, b11, 10)
    b14 = class1(b11, b12, 5)
    b15 = class1(b12, b10, -15)
    b10.fonk8(b13)
    b11.fonk8(b14)
    b12.fonk8(b15)
    print("class2 ID:", b10)
    print("Adjacent Vertices:", [str(edge.b2) for edge in b10.fonk9()])
    print("Minimum Distance:", b10.fonk4())
    print("Previous class2:", b10.fonk6())
    print("Visited:", b10.fonk10())
    b10.fonk5(20)
    b10.fonk7(b12)
    b10.fonk11(True)
    print("Updated Minimum Distance:", b10.fonk4())
    print("Updated Previous class2:", b10.fonk6())
    print("Updated Visited:", b10.fonk10())
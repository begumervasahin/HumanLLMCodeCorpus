class class1:
    b1 = 'b3', 'b4'
    def fonk1(self, b3, b2 = None):
        self.b3 = b3
        self.b4 = b2
    def fonk2(self, other):
        return self.b3 < other.b3
    def fonk3(self, other):
        return self.b3 <= other.b3
class class2:
    def fonk4(self):
        self.b5 = None
        self.b6 = None
        self.a1 = 0
    def fonk5(self):
        b7 = [str(node.b3) for node in self]
        return ", ".join(b7)
    b8 = __str__
    def fonk6(self):
        return self.a1
    def fonk7(self):
        return self.a1 = = 0
    def fonk8(self):
        if self.fonk7():
            raise IndexError("Queue is empty")
        b9 = self.b5.b3
        self.b5 = self.b5.b4
        self.a1 -= 1
        if self.fonk7():
            self.b6 = None
        return b9
    def fonk9(self, element):
        b10 = class1(element)
        if self.fonk7():
            self.b5 = b10
        else:
            self.b6.b4 = b10
        self.b6 = b10
        self.a1 += 1
    def fonk10(self, index):
        b11 = self.b5
        for _ in range(index):
            b11 = b11.b4
        return b11
    def fonk11(self, index, b3):
        b11 = self.b5
        for _ in range(index):
            b11 = b11.b4
        b11.b3 = b3
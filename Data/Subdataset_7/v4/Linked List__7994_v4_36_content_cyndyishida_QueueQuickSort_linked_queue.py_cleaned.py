class class1:
    b1 = 'b2', 'b3'
    def fonk1(self, b2, next_node):
        self.b2 = b2
        self.b3 = next_node
    def fonk2(self, other):
        return self.b2 < other.b2
    def fonk3(self, other):
        return self.b2 <= other.b2
class class2:
    def fonk4(self):
        self.b4 = None
        self.b5 = None
        self.a1 = 0
    def fonk5(self):
        b6 = self.b4
        b7 = []
        while b6:
            b7.append(str(b6.b2))
            b6 = b6.b3
        return ", ".join(b7)
    b8 = __str__
    def fonk6(self):
        return self.a1
    def fonk7(self):
        return self.a1 = = 0
    def fonk8(self):
        if self.fonk7():
            raise IndexError("Queue is empty")
        b9 = self.b4.b2
        self.b4 = self.b4.b3
        self.a1 -= 1
        if self.fonk7():
            self.b5 = None
        return b9
    def fonk9(self, element):
        b10 = class1(element, None)
        if self.fonk7():
            self.b4 = b10
        else:
            self.b5.b3 = b10
        self.b5 = b10
        self.a1 += 1
    def fonk10(self, index):
        b6 = self.b4
        for i in range(index):
            b6 = b6.b3
        return b6
    def fonk11(self, index, b2):
        b6 = self.b4
        for i in range(index):
            b6 = b6.b3
        b6.b2 = b2
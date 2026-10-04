class class1:
    b1 = 'b3', 'b2'
    def fonk1(self, b3, b2 = None):
        self.b3 = b3
        self.b2 = b2
    def fonk2(self, other):
        return self.b3 < other.b3
    def fonk3(self, other):
        return self.b3 <= other.b3
class class2:
    def fonk4(self):
        self.b4 = None
        self.b5 = None
        self.a1 = 0
    def fonk5(self):
        b6 = []
        b7 = self.b4
        while b7:
            b6.append(str(b7.b3))
            b7 = b7.b2
        return ", ".join(b6)
    b8 = __str__
    def fonk6(self):
        return self.a1
    def fonk7(self):
        return self.a1 = = 0
    def fonk8(self, element):
        b9 = class1(element)
        if self.fonk7():
            self.b4 = b9
        else:
            self.b5.b2 = b9
        self.b5 = b9
        self.a1 += 1
    def fonk9(self):
        if self.fonk7():
            raise IndexError("dequeue from empty queue")
        b10 = self.b4.b3
        self.b4 = self.b4.b2
        self.a1 -= 1
        if self.fonk7():
            self.b5 = None
        return b10
    def fonk10(self, index):
        if index < 0 or index >= self.a1:
            raise IndexError("index out of range")
        b7 = self.b4
        for _ in range(index):
            b7 = b7.b2
        return b7
    def fonk11(self, index, b3):
        if index < 0 or index >= self.a1:
            raise IndexError("index out of range")
        b7 = self.b4
        for _ in range(index):
            b7 = b7.b2
        b7.b3 = b3
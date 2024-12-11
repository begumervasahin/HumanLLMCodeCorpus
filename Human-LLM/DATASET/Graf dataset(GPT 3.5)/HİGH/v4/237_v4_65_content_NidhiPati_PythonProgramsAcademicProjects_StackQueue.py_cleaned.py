import sys
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, item):
        self.b1.append(item)
    def fonk3(self):
        if len(self.b1) == 0:
            raise IndexError("Stack is empty")
        return self.b1[-1]
    def fonk4(self):
        return self.b1.fonk4()
    def fonk5(self):
        return len(self.b1)
    def fonk6(self):
        return sys.getsizeof(self.b1)
class class2:
    a1 = 10
    def fonk7(self):
        self.b1 = [None] * class2.a1
        self.a2 = 0
        self.a3 = 0
    def fonk8(self):
        return self.a2
    def fonk9(self):
        return self.a2 = = 0
    def fonk10(self):
        if self.fonk9():
            raise IndexError("Empty Queue")
        return self.b1[self.a3]
    def fonk11(self):
        if self.fonk9():
            raise IndexError("Empty Queue")
        b2 = self.b1[self.a3]
        self.b1[self.a3] = None
        self.a3 = (self.a3 + 1) % len(self.b1)
        self.a2 -= 1
        return b2
    def fonk12(self, item):
        if self.a2 = = len(self.b1):
            self.fonk13(len(self.b1) * 2)
        b3 = (self.a3 + self.a2) % len(self.b1)
        self.b1[b3] = item
        self.a2 += 1
    def fonk13(self, capacity):
        b4 = self.b1
        self.b1 = [None] * capacity
        b5 = self.a3
        for index in range(0, len(b4)):
            self.b1[index] = b4[b5]
            b5 = (b5 + 1) % len(b4)
        self.a3 = 0
    def fonk14(self):
        return sys.getsizeof(self.b1)
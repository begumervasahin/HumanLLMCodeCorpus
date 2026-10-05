from random import randint
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 < self.b1:
            if self.b2 is None:
                self.b2 = class1(b1)
            else:
                self.b2.fonk4(b1)
        elif b1 > self.b1:
            if self.b3 is None:
                self.b3 = class1(b1)
            else:
                self.b3.fonk4(b1)
class class2:
    def fonk3(self):
        self.b4 = None
    def fonk4(self, b5):
        if self.b4 is None:
            self.b4 = class1(b5)
        else:
            self.b4.fonk4(b5)
    def fonk5(self, b5):
        return self.fonk6(self.b4, b5)
    def fonk6(self, b6, b5):
        if b6 is None:
            return False
        elif b5 = = b6.b1:
            return True
        elif b5 < b6.b1:
            return self.fonk6(b6.b2, b5)
        else:
            return self.fonk6(b6.b3, b5)
    def fonk7(self, b6 = None):
        if b6 is None:
            b6 = self.b4
        b7 = []
        if b6:
            b7.append(b6.b1)
            b7 += self.fonk7(b6.b2)
            b7 += self.fonk7(b6.b3)
        return b7
    def fonk8(self):
        b8 = self.fonk7()
        b8.sort()
        b9 = len(b8)
        self.b4 = class1(b8.pop(b9))
        for element in b8:
            self.b4.fonk4(element)
        return self.fonk7()
b10 = class2()
for _ in range(50):
    b10.fonk4(randint(0, 100))
print("Original Tree:", b10.fonk7())
print("Rearranged Tree with Median as Root:", b10.fonk8())
print("Is 55 in the b10?", b10.fonk5(55))
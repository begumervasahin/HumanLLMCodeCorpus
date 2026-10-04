import random
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = random.random()
    def fonk2(self):
        return str(self.b1)
class class2:
    def fonk3(self):
        self.b5 = None
        self.a1 = 0
    def fonk4(self, b7):
        b6 = b7.b3
        b7.b3 = b6.b2
        b6.b2 = b7
        return b6
    def fonk5(self, b7):
        b6 = b7.b2
        b7.b2 = b6.b3
        b6.b3 = b7
        return b6
    def fonk6(self, element):
        self.a1 += 1
        if self.b5 is None:
            self.b5 = class1(element)
        else:
            self.b5 = self.fonk7(element, self.b5)
    def fonk7(self, element, b7):
        if b7 is None:
            return class1(element)
        if element < b7.b1:
            b7.b2 = self.fonk7(element, b7.b2)
            if b7.b2.b4 > b7.b4:
                b7 = self.fonk5(b7)
        else:
            b7.b3 = self.fonk7(element, b7.b3)
            if b7.b3.b4 > b7.b4:
                b7 = self.fonk4(b7)
        return b7
    def fonk8(self, element):
        return self.fonk9(self.b5, element)
    def fonk9(self, b7, element):
        if b7 is None:
            return False
        if b7.b1 = = element:
            return True
        elif element < b7.b1:
            return self.fonk9(b7.b2, element)
        else:
            return self.fonk9(b7.b3, element)
    def fonk10(self):
        return self.fonk11(self.b5)
    def fonk11(self, b7):
        if b7 is None:
            return 0
        return 1 + max(self.fonk11(b7.b2), self.fonk11(b7.b3))
    def fonk12(self):
        return self.a1
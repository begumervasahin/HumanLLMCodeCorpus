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
    def fonk4(self, element):
        self.a1 += 1
        self.b5 = self.fonk5(self.b5, element)
    def fonk5(self, b6, element):
        if b6 is None:
            return class1(element)
        if element < b6.b1:
            b6.b2 = self.fonk5(b6.b2, element)
            if b6.b2.b4 > b6.b4:
                b6 = self.fonk7(b6)
        elif element > b6.b1:
            b6.b3 = self.fonk5(b6.b3, element)
            if b6.b3.b4 > b6.b4:
                b6 = self.fonk6(b6)
        return b6
    def fonk6(self, b6):
        b7 = b6.b3
        b6.b3 = b7.b2
        b7.b2 = b6
        return b7
    def fonk7(self, b6):
        b7 = b6.b2
        b6.b2 = b7.b3
        b7.b3 = b6
        return b7
    def fonk8(self, element):
        return self.fonk9(self.b5, element)
    def fonk9(self, b6, element):
        if b6 is None:
            return False
        if b6.b1 = = element:
            return True
        elif element < b6.b1:
            return self.fonk9(b6.b2, element)
        else:
            return self.fonk9(b6.b3, element)
    def fonk10(self):
        return self.fonk11(self.b5)
    def fonk11(self, b6):
        if b6 is None:
            return 0
        return 1 + max(self.fonk11(b6.b2), self.fonk11(b6.b3))
    def fonk12(self):
        return self.a1
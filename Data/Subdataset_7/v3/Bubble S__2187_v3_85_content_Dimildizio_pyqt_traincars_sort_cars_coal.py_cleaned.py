from random import randint, choice
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return f'class1(b2 = {self.b2}, b1={self.b1})'
    def fonk3(self, another):
        return self.b2 = = another
    def fonk4(self, another):
        return self.b2 > another
    def fonk5(self, another):
        return self.b2 < another
    def fonk6(self, another):
        return self.b2 >= another
    def fonk7(self, another):
        return self.b2 <= another
    def fonk8(self, another):
        return self.b2 != another
class class2:
    def fonk9(self, b3):
        self.b3 = [class1(randint(1, 74), randint(1, 1000)) for _ in range(b3)]
    def fonk10(self):
        return f'class2 with {len(self.b3)} b3'
    def fonk11(self, b4 = True):
        b5 = 'b2' if b4 else 'b1'
        b6 = False if b4 else True
        for i in range(len(self.b3)):
            for b8 in range(len(self.b3) - 1 - i):
                if getattr(self.b3[b8], b5) > getattr(self.b3[b8 + 1], b5):
                    self.b3[b8], self.b3[b8 + 1] = self.b3[b8 + 1], self.b3[b8]
    def fonk12(self, b4 = True):
        b5 = 'b2' if b4 else 'b1'
        for i in range(1, len(self.b3)):
            b7 = self.b3[i]
            b8 = i - 1
            while b8 >= 0 and getattr(self.b3[b8], b5) > getattr(b7, b5):
                self.b3[b8 + 1] = self.b3[b8]
                b8 -= 1
            self.b3[b8 + 1] = b7
    def fonk13(self, value, b4 = True):
        self.fonk11(b4)
        b11, b9 = 0, len(self.b3) - 1
        while b11 <= b9:
            b10 = (b11 + b9)
            if self.b3[b10] == value:
                return self.b3[b10]
            elif self.b3[b10] < value:
                b11 = b10 + 1
            else:
                b9 = b10 - 1
        return False
    def fonk14(self, value):
        self.fonk12()
        b11, b9 = 0, len(self.b3) - 1
        while b11 <= b9:
            b10 = (b11 + b9)
            if self.b3[b10].b1 = = value:
                return self.b3[b10]
            elif self.b3[b10].b1 < value:
                b11 = b10 + 1
            else:
                b9 = b10 - 1
        return False
    def fonk15(self, value, b4 = True):
        if b4:
            return self.fonk13(value, b4 = True)
        else:
            return self.fonk13(value, b4 = False)
    def fonk16(self, value, b12):
        if b12 = = 'b2':
            return self.fonk15(value, b4 = True)
        elif b12 = = 'b1':
            return self.fonk14(value)
        else:
            try:
                return self.b3[value]
            except IndexError:
                return False
    def fonk17(self, car):
        self.b3.remove(car)
        return car
class class3:
    b13 = None
    @classmethod
    def fonk18(cls, num_cars):
        cls.b13 = class2(num_cars)
    @classmethod
    def fonk19(cls):
        cls.b13 = None
class3.fonk18(10)
print(class3.b13)
print(class3.b13.fonk15(5))
class3.fonk19()
print(class3.b13)
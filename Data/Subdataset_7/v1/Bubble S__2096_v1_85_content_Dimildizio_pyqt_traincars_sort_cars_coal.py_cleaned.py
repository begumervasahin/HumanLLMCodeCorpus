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
        b4 = 'b2' if b4 else 'b1'
        for x in range(len(self.b3) - 1, 0, -1):
            b5 = True
            for y in range(x):
                if getattr(self.b3[y], b4) > getattr(self.b3[y + 1], b4):
                    self.b3[y], self.b3[y + 1] = self.b3[y + 1], self.b3[y]
                    b5 = False
            if b5:
                break
    def fonk12(self, b4 = True):
        b4 = 'b2' if b4 else 'b1'
        for x in range(len(self.b3) - 1):
            b5 = True
            for y in range(len(self.b3) - x - 1):
                if getattr(self.b3[y], b4) < getattr(self.b3[y + 1], b4):
                    self.b3[y], self.b3[y + 1] = self.b3[y + 1], self.b3[y]
                    b5 = False
            if b5:
                break
    def fonk13(self, b4 = True):
        b4 = 'b2' if b4 else 'b1'
        for x in range(1, len(self.b3)):
            b6 = self.b3[x]
            b7 = x - 1
            while getattr(b6, b4) < getattr(self.b3[b7], b4) and b7 >= 0:
                self.b3[b7 + 1] = self.b3[b7]
                b7 -= 1
            self.b3[b7 + 1] = b6
    def fonk14(self, b4 = True):
        b4 = 'b2' if b4 else 'b1'
        for x in range(1, len(self.b3)):
            b6 = self.b3[x]
            b7 = x - 1
            while getattr(b6, b4) > getattr(self.b3[b7], b4) and b7 >= 0:
                self.b3[b7 + 1] = self.b3[b7]
                b7 -= 1
            self.b3[b7 + 1] = b6
    def fonk15(self, value):
        b8 = len(self.b3) - 1
        a1 = 0
        while a1 <= b8:
            b9 = (b8 + a1)
            if self.b3[b9] == value:
                return self.b3[b9]
            elif self.b3[b9] > value:
                b8 = b9 - 1
            else:
                a1 = b9 + 1
        return False
    def fonk16(self, value):
        b8 = len(self.b3) - 1
        a1 = 0
        while a1 <= b8:
            b9 = (b8 + a1)
            if self.b3[b9] == value:
                return self.b3[b9]
            elif self.b3[b9] < value:
                b8 = b9 - 1
            else:
                a1 = b9 + 1
        return False
    def fonk17(self, value):
        self.fonk13(False)
        b8 = len(self.b3) - 1
        a1 = 0
        while a1 <= b8:
            b9 = (b8 + a1)
            if self.b3[b9].b1 = = value:
                return self.b3[b9]
            elif self.b3[b9].b1 > value:
                b8 = b9 - 1
            else:
                a1 = b9 + 1
        return False
    def fonk18(self, value, b10 = True):
        if b10:
            b11 = choice([self.bubble_sort_to_right, self.insertion_sort_to_right])
            b11()
            return self.fonk15(value)
        else:
            b11 = choice([self.bubble_sort_to_left, self.insertion_sort_to_left])
            b11()
            return self.fonk16(value)
    def fonk19(self, value, b12):
        if b12 = = 'b2':
            return self.fonk18(value)
        elif b12 = = 'b1':
            return self.fonk17(value)
        else:
            try:
                return self.b3[value]
            except IndexError:
                return False
    def fonk20(self, car):
        self.b3.remove(car)
        return car
class class3:
    b13 = False
    @classmethod
    def fonk21(cls, value):
        cls.b13 = class2(value)
    @classmethod
    def fonk22(cls):
        cls.b13 = False
class3.fonk21(10)
print(class3.b13)
print(class3.b13.fonk18(5))
class3.fonk22()
print(class3.b13)
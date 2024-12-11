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
        b4 = f'This is a b9 with {len(self.b3)} b3:'
        for b6 in self.b3:
            b4 += f'\n\t{b6}'
        return b4
    def fonk11(self, b5, num):
        if b5 = = 'b2':
            b6 = class1(num, randint(1, 1000))
        else:
            b6 = class1(randint(1, 74), num)
        self.b3.append(b6)
        return b6
    def fonk12(self, b7 = True):
        b7 = 'b2' if b7 else 'b1'
        for x in range(len(self.b3)-1, 0, -1):
            b8 = True
            for y in range(x):
                if getattr(self.b3[y], b7) > getattr(self.b3[y+1], b7):
                    self.b3[y], self.b3[y+1] = self.b3[y+1], self.b3[y]
                    b8 = False
            if b8:
                break
class class3:
    b9 = False
    @classmethod
    def fonk13(cls, value):
        cls.b9 = class2(value)
    @classmethod
    def fonk14(cls):
        cls.b9 = False
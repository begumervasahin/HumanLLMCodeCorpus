from random import randint, choice
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return f'class1(b1 = {self.b1}, b2={self.b2})'
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
        b4 = f'This is a b7 with {len(self.b3)} b3: '
        for b6 in self.b3:
            b4 += '\n\t' + str(b6)
        return b4
    def fonk11(self, b5, num):
        if b5 = = 'b2':
            b6 = class1(num, randint(1, 1000))
        else:
            b6 = class1(randint(1, 74), num)
        self.b3.append(b6)
        return b6
class class3:
    b7 = None
    @classmethod
    def fonk12(cls, value):
        cls.b7 = class2(value)
    @classmethod
    def fonk13(cls):
        cls.b7 = None

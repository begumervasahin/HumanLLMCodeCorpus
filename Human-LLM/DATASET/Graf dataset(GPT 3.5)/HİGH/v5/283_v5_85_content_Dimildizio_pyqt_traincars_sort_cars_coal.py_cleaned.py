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
        b4 = '\n'.join([f'\t{b6}' for b6 in self.b3])
        return f'This is a b10 with {len(self.b3)} b3:\n{b4}'
    def fonk11(self, b5, num):
        if b5 = = 'b2':
            b6 = class1(num, randint(1, 1000))
        else:
            b6 = class1(randint(1, 74), num)
        self.b3.append(b6)
        return b6
    def fonk12(self, b7 = True):
        b8 = 'b2' if b7 else 'b1'
        for i in range(len(self.b3) - 1, 0, -1):
            b9 = True
            for j in range(i):
                if getattr(self.b3[j], b8) > getattr(self.b3[j + 1], b8):
                    self.b3[j], self.b3[j + 1] = self.b3[j + 1], self.b3[j]
                    b9 = False
            if b9:
                break
class class3:
    b10 = None
    @classmethod
    def fonk13(cls, value):
        cls.b10 = class2(value)
    @classmethod
    def fonk14(cls):
        cls.b10 = None
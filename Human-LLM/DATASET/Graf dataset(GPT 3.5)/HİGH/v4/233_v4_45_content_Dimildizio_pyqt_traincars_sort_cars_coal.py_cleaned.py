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
        return f'class2 with {len(self.b3)} b3'
    def fonk11(self, b4, num):
        if b4 = = 'b2':
            b5 = class1(num, randint(1, 1000))
        else:
            b5 = class1(randint(1, 74), num)
        self.b3.append(b5)
        return b5
    def fonk12(self, b6 = True):
        pass
    def fonk13(self, b6 = True):
        pass
    def fonk14(self, b6 = True):
        pass
    def fonk15(self, b6 = True):
        pass
    def fonk16(self, b6 = True):
        pass
    def fonk17(self, b6 = True):
        pass
    def fonk18(self, value):
        pass
    def fonk19(self, value):
        pass
    def fonk20(self, value):
        pass
    def fonk21(self, value, b7 = True):
        pass
    def fonk22(self, value, mytype):
        pass
    def fonk23(self, b5):
        self.b3.remove(b5)
        return b5
class class3:
    b8 = None
    @classmethod
    def fonk24(cls, value):
        cls.b8 = class2(value)
    @classmethod
    def fonk25(cls):
        cls.b8 = None
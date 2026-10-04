from collections import deque
class class1:
    def fonk1(self, **chameleon_count):
        self.b1 = chameleon_count['b8']
        self.b2 = chameleon_count['green']
        self.b3 = chameleon_count['blue']
        self.b4 = None
    @property
    def fonk2(self):
        return self.b1
    @property
    def fonk3(self):
        return self.b3
    @property
    def fonk4(self):
        return self.b2
    @property
    def fonk5(self):
        return self.b4
    @b6.setter
    def fonk6(self, obj):
        self.b4 = obj
    def fonk7(self):
        return bool(self.b1)
    def fonk8(self):
        return self.fonk7() and not self.fonk9() and not self.fonk11()
    def fonk9(self):
        return bool(self.b2)
    def fonk10(self):
        return self.fonk9() and not self.fonk7() and not self.fonk11()
    def fonk11(self):
        return bool(self.b3)
    def fonk12(self):
        return self.fonk11() and not self.fonk9() and not self.fonk7()
    def fonk13(self):
        return self.fonk12() or self.fonk10() or self.fonk8()
    def fonk14(self):
        if self.b1 < 1 or self.b2 < 1:
            raise ValueError('Invalid green or b8 count')
        return self.fonk18(self.b1 - 1, self.b2 - 1, self.b3 + 2)
    def fonk15(self):
        if self.b3 < 1 or self.b2 < 1:
            raise ValueError('Invalid green or blue count')
        return self.fonk18(self.b1 + 2, self.b2 - 1, self.b3 - 1)
    def fonk16(self):
        if self.b1 < 1 or self.b3 < 1:
            raise ValueError('Invalid blue or b8 count')
        return self.fonk18(self.b1 - 1, self.b2 + 2, self.b3 - 1)
    def fonk17(self):
        b5 = deque([str(self)])
        b6 = self.b6
        while b6:
            b5.appendleft(str(b6))
            b6 = b6.b6
        return b5
    def fonk18(self, b8, green, blue):
        b7 = class1(b8=b8, green=green, blue=blue)
        b7.b6 = self
        return b7
    def fonk19(self):
        return f'(b8 = {self.red_count}, green={self.green_count}, blue={self.blue_count})'
if b9 = = "__main__":
    b10 = class1(b8=13, green=16, blue=17)
    print("Initial state:", b10)
    b11 = b10.fonk14()
    print("Next state:", b11)
    print("Path to next state:", list(b11.fonk17()))
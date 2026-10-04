'''
Created on Dec 16th, 2017
@author: Lok
'''
class class1:
    def fonk1(self, b1):
        if isinstance(b1, int) or b1 is None:
            self.b1 = b1
            self.b2 = None
            self.b3 = None
        else:
            raise TypeError("Input must be an int")
    def fonk2(self):
        return str(self.b1)
class class2:
    def fonk3(self):
        self.b4 = class1(None)
        self.b5 = class1(None)
        self.b4.b3 = self.b5
        self.b5.b2 = self.b4
        self.a1 = 0
    def fonk4(self):
        b6 = "("
        b7 = self.b4.b3
        while b7 != self.b5:
            b6 += str(b7.b1) + " "
            b7 = b7.b3
        return b6.rstrip() + ")"
    def fonk5(self, b1):
        if isinstance(b1, int):
            b8 = class1(b1)
            b9 = self.b4.b3
            self.b4.b3 = b8
            b8.b2 = self.b4
            b8.b3 = b9
            b9.b2 = b8
            self.a1 += 1
        else:
            raise TypeError("Input must be an int")
    def fonk6(self, b1):
        if isinstance(b1, int):
            b8 = class1(b1)
            b10 = self.b5.b2
            b10.b3 = b8
            b8.b2 = b10
            b8.b3 = self.b5
            self.b5.b2 = b8
            self.a1 += 1
        else:
            raise TypeError("Input must be an int")
    def fonk7(self):
        if self.a1 = = 0:
            raise IndexError("List is empty")
        b9 = self.b4.b3
        self.b4.b3 = b9.b3
        b9.b3.b2 = self.b4
        self.a1 -= 1
        return b9.b1
    def fonk8(self):
        if self.a1 = = 0:
            raise IndexError("List is empty")
        b10 = self.b5.b2
        self.b5.b2 = b10.b2
        b10.b2.b3 = self.b5
        self.a1 -= 1
        return b10.b1
    def fonk9(self):
        return self.a1
    def fonk10(self):
        if self.a1 = = 0:
            raise IndexError("List is empty")
        return self.b4.b3.b1
    def fonk11(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an int")
        if pos < 0 or pos >= self.a1:
            raise IndexError("Position out of range")
        b7 = self.b4.b3
        for _ in range(pos):
            b7 = b7.b3
        return b7.b1
    def fonk12(self, b1, pos):
        if not isinstance(b1, int):
            raise TypeError("Input must be an int")
        if not isinstance(pos, int):
            raise TypeError("Position must be an int")
        if pos < 0 or pos > self.a1:
            raise IndexError("Position out of range")
        b7 = self.b4.b3
        for _ in range(pos):
            b7 = b7.b3
        b8 = class1(b1)
        b11 = b7.b2
        b11.b3 = b8
        b8.b2 = b11
        b8.b3 = b7
        b7.b2 = b8
        self.a1 += 1
    def fonk13(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an int")
        if pos < 0 or pos >= self.a1:
            raise IndexError("Position out of range")
        b7 = self.b4.b3
        for _ in range(pos):
            b7 = b7.b3
        b11 = b7.b2
        b12 = b7.b3
        b11.b3 = b12
        b12.b2 = b11
        self.a1 -= 1
        return b7.b1
    def fonk14(self, b1):
        if not isinstance(b1, int):
            raise TypeError("Input must be an int")
        a2 = 0
        b7 = self.b4.b3
        while b7 != self.b5:
            if b7.b1 = = b1:
                a2 += 1
            b7 = b7.b3
        return a2
if b13 = = "__main__":
    b14 = class2()
    b14.fonk6(5)
    b14.fonk5(10)
    b14.fonk6(12)
    b14.fonk12(7, 1)
    b14.fonk12(6, 1)
    print(b14.fonk11(2))
    print(b14.fonk13(2))
    print(b14)
    print(b14.fonk9())
    print(b14.fonk14(10))
    print(b14.fonk7())
    print(b14.fonk7())
    print(b14.fonk8())
    print(b14.fonk9())

import sys
from b10 import deepcopy
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return not self.b1
    def fonk3(self, item):
        self.b1.insert(0, item)
    def fonk4(self):
        return self.b1.pop()
    def fonk5(self):
        return len(self.b1)
class class2:
    def fonk6(self, b2 = None):
        self.b2 = b2
        self.b3 = None
        self.b4 = None
    def fonk7(self):
        sys.stdout.write(self.b2)
    def fonk8(self):
        a1 = 1
        if self.b3:
            a1 += self.b3.fonk8()
        if self.b4:
            a1 += self.b4.fonk8()
        return a1
    @classmethod
    def fonk9(cls, depth):
        b5 = class2('X')
        cls.fonk10(b5, depth, 1)
        return b5
    @classmethod
    def fonk10(cls, b14, depth, b6):
        if b6 = = depth:
            return
        b14.b3 = class2('X')
        b14.b4 = class2('XX')
        cls.fonk10(b14.b3, depth, b6 + 1)
        cls.fonk10(b14.b4, depth, b6 + 1)
    def fonk11(self):
        return self.fonk12(self)
    @staticmethod
    def fonk12(b14):
        if not b14:
            return 0
        return max(class2.fonk12(b14.b3), class2.fonk12(b14.b4)) + 1
    def fonk13(self, height):
        self.fonk14(self, height)
    @staticmethod
    def fonk14(b14, height):
        if height <= 1:
            return
        if b14:
            if not b14.b3:
                b14.b3 = class2(' ')
            if not b14.b4:
                b14.b4 = class2(' ')
            class2.fonk14(b14.b3, height - 1)
            class2.fonk14(b14.b4, height - 1)
    def fonk15(self):
        b7 = self.fonk11()
        b8 = deepcopy(self)
        b8.fonk13(b7)
        b9 = class1()
        b9.fonk3(b8)
        a2 = 1
        while not b9.fonk2():
            b10 = class1()
            while not b9.fonk2():
                b10.fonk3(b9.fonk4())
            b11 = True
            b12 = ""
            b13 = False
            while not b10.fonk2():
                b14 = b10.fonk4()
                b15 = b24**(b7 - a2 + 1) - b24
                b16 = b24**(b7 - a2 + b24) - b24
                b17 = b24**(b7 - a2) - b24
                b17 = max(b17, 0)
                b16 -= b17 * b24
                b15 -= b17
                a3 = b24
                b15 += a3
                if b11:
                    b12 += " " * a3
                b18 = "/" if b14.b3 and b14.b3.b2 != " " else " "
                b19 = "\\" if b14.b4 and b14.b4.b2 != " " else " "
                if b11:
                    b12 += " " * (b24**(b7 - a2) - 1) + b18
                else:
                    b12 += " " * (b24**(b7 - a2 + 1) + 1) + b18
                b12 += " " * (b24**(b7 - a2 + 1) - 3) + b19
                b20 = "_" if b14.b3 and b14.b3.b2 != " " else " "
                b21 = "_" if b14.b4 and b14.b4.b2 != " " else " "
                b22 = 1 if b13 else 0
                b13 = False
                b23 = len(str(b14.b2))
                if b23 > 1:
                    if b23 % b24 = = 1:
                        if b17 > 0:
                            b17 -= (b23 - 1)
                        else:
                            b16 -= (b23 - 1)
                            b15 -= (b23 - 1)
                            b13 = b23 != 1
                    else:
                        if b17 > 0:
                            b17 -= (b23
                            b13 = True
                        else:
                            b16 -= (b23 - 1)
                            b15 -= (b23 - 1)
                if b11:
                    print(" " * b15 + b20 * b17 + b14.b2 + b21 * b17, b25 = ' ')
                    b11 = False
                else:
                    print(" " * (b16 - b22) + b20 * b17 + b14.b2 + b21 * b17, b25 = ' ')
                if b14.b3:
                    b9.fonk3(b14.b3)
                if b14.b4:
                    b9.fonk3(b14.b4)
            if not b9.fonk2():
                print("\n" + b12)
            a2 += 1
if b26 = = '__main__':
    b5 = class2('A')
    b5.b3 = class2('B')
    b5.b4 = class2('C')
    b5.b3.b3 = class2('D')
    b5.b3.b4 = class2('E')
    b5.b3.b4.b4 = class2.fonk9(b24)
    b5.b4.b3 = class2('F')
    b5.b4.b4 = class2('G')
    b5.b3.b3.b3 = class2('H')
    b5.b3.b3.b4 = class2('I')
    b5.b3.b4.b3 = class2('J')
    b5.b4.b4.b3 = class2('N')
    b5.b4.b4.b4 = class2('O')
    b5.fonk15()
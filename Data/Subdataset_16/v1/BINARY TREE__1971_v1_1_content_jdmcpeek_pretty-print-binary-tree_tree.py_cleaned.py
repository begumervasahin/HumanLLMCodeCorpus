import sys
from b9 import deepcopy
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return self.b1 = = []
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
        a1 = 0
        if self.b3:
            a1 += self.b3.fonk8()
        if self.b4:
            a1 += self.b4.fonk8()
        return a1 + 1
    @classmethod
    def fonk9(cls, depth):
        b5 = class2('X')
        cls.fonk10(b5, depth, 1)
        return b5
    @classmethod
    def fonk10(cls, b13, depth, b6):
        if b6 = = depth:
            return
        b13.b3 = class2('X')
        b13.b4 = class2('XX')
        cls.fonk10(b13.b3, depth, b6 + 1)
        cls.fonk10(b13.b4, depth, b6 + 1)
    def fonk11(self):
        return class2.fonk12(self)
    @staticmethod
    def fonk12(b13):
        if not b13:
            return 0
        else:
            return max(class2.fonk12(b13.b3), class2.fonk12(b13.b4)) + 1
    def fonk13(self, height):
        class2.fonk14(self, height)
    @staticmethod
    def fonk14(b13, height):
        if height <= 1:
            return
        if b13:
            if not b13.b3:
                b13.b3 = class2(' ')
            if not b13.b4:
                b13.b4 = class2(' ')
            class2.fonk14(b13.b3, height - 1)
            class2.fonk14(b13.b4, height - 1)
    def fonk15(self):
        b7 = self.fonk11()
        b5 = deepcopy(self)
        b5.fonk13(b7)
        b8 = class1()
        b8.fonk3(b5)
        a2 = 1
        while not b8.fonk2():
            b9 = class1()
            while not b8.fonk2():
                b9.fonk3(b8.fonk4())
            b10 = True
            b11 = ""
            b12 = False
            while not b9.fonk2():
                b13 = b9.fonk4()
                b14 = pow(b21, b7 - a2 + 1) - b21
                b15 = pow(b21, b7 - a2 + b21) - b21
                b16 = pow(b21, b7 - a2) - b21
                if b16 < 0:
                    b16 = 0
                b15 = b15 - (b16 * b21)
                b14 = b14 - b16
                a3 = b21
                b14 += a3
                if b10:
                    b11 += " " * a3
                b17 = "/" if b13.b3 and b13.b3.b2 != " " else " "
                if b10:
                    b11 += " " * (pow(b21, b7 - a2) - 1) + b17
                else:
                    b11 += " " * (pow(b21, b7 - a2 + 1) + 1) + b17
                b17 = "\\" if b13.b4 and b13.b4.b2 != " " else " "
                b11 += " " * (pow(b21, b7 - a2 + 1) - 3) + b17
                if b13.b3 and b13.b3.b2 = = " ":
                    b18 = " "
                else:
                    b18 = "_"
                if b13.b4 and b13.b4.b2 = = " ":
                    b19 = " "
                else:
                    b19 = "_"
                if b12:
                    a4 = 1
                    b12 = False
                else:
                    a4 = 0
                b20 = len(str(b13.b2))
                if b20 > 1:
                    if b20 % b21 = = 1:
                        if b16 > 0:
                            b16 -= ((b20 - 1)
                        else:
                            b15 -= (b20 - 1)
                            b14 -= (b20 - 1)
                            if b20 != 1:
                                b12 = True
                    else:
                        if b16 > 0:
                            b16 -= (b20
                            b12 = True
                        else:
                            b15 -= (b20 - 1)
                            b14 -= (b20 - 1)
                if b10:
                    print(" " * b14 + b18 * b16 + b13.b2 + b19 * b16, b22 = ' ')
                    b10 = False
                else:
                    print(" " * (b15 - a4) + b18 * b16 + b13.b2 + b19 * b16, b22 = ' ')
                if b13.b3:
                    b8.fonk3(b13.b3)
                if b13.b4:
                    b8.fonk3(b13.b4)
            if not b8.fonk2():
                print("\n" + b11)
            a2 += 1
if b23 = = '__main__':
    b24 = class2('A')
    b24.b3 = class2('B')
    b24.b4 = class2('C')
    b24.b3.b3 = class2('D')
    b24.b3.b4 = class2('E')
    b24.b3.b4.b4 = class2.fonk9(b21)
    b24.b4.b3 = class2('F')
    b24.b4.b4 = class2('G')
    b24.b3.b3.b3 = class2('H')
    b24.b3.b3.b4 = class2('I')
    b24.b3.b4.b3 = class2('J')
    b24.b4.b4.b3 = class2('N')
    b24.b4.b4.b4 = class2('O')
    b24.fonk15()
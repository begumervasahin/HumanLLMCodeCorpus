import sys
from copy import deepcopy
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        sys.stdout.write(self.b1)
    def fonk3(self):
        a1 = 0
        if self.b2:
            a1 += self.b2.fonk3()
        if self.b3:
            a1 += self.b3.fonk3()
        return a1 + 1
    @classmethod
    def fonk4(cls, depth):
        b4 = cls('X')
        cls.fonk5(b4, depth, 1)
        return b4
    @classmethod
    def fonk5(cls, b12, depth, b5):
        if b5 = = depth:
            return
        b12.b2 = class1('X')
        b12.b3 = class1('XX')
        cls.fonk5(b12.b2, depth, b5 + 1)
        cls.fonk5(b12.b3, depth, b5 + 1)
    def fonk6(self):
        return self.fonk7(self)
    @staticmethod
    def fonk7(b12):
        if not b12:
            return 0
        return max(class1.fonk7(b12.b2), class1.fonk7(b12.b3)) + 1
    def fonk8(self, height):
        self.fonk9(self, height)
    @staticmethod
    def fonk9(b12, height):
        if height <= 1:
            return
        if b12:
            if not b12.b2:
                b12.b2 = class1(' ')
            if not b12.b3:
                b12.b3 = class1(' ')
            class1.fonk9(b12.b2, height - 1)
            class1.fonk9(b12.b3, height - 1)
    def fonk10(self):
        b6 = self.fonk6()
        b4 = deepcopy(self)
        b4.fonk8(b6)
        b7 = class2()
        b7.fonk13(b4)
        a2 = 1
        while not b7.fonk12():
            b8 = class2()
            while not b7.fonk12():
                b8.fonk13(b7.fonk14())
            b9 = True
            b10 = ""
            b11 = False
            while not b8.fonk12():
                b12 = b8.fonk14()
                b13 = b22 ** (b6 - a2 + 1) - b22
                b14 = b22 ** (b6 - a2 + b22) - b22
                b15 = max(b22 ** (b6 - a2) - b22, 0)
                b14 -= b15 * b22
                b13 -= b15
                a3 = b22
                b13 += a3
                if b9:
                    b10 += " " * a3
                b16 = "/" if b12.b2 and b12.b2.b1 != " " else " "
                b17 = "\\" if b12.b3 and b12.b3.b1 != " " else " "
                if b9:
                    b10 += " " * (b22 ** (b6 - a2) - 1) + b16
                else:
                    b10 += " " * (b22 ** (b6 - a2 + 1) + 1) + b16
                b10 += " " * (b22 ** (b6 - a2 + 1) - 3) + b17
                b18 = "_" if b12.b2 and b12.b2.b1 != " " else " "
                b19 = "_" if b12.b3 and b12.b3.b1 != " " else " "
                b20 = 1 if b11 else 0
                b11 = False
                b21 = len(str(b12.b1))
                if b21 > 1:
                    if b21 % b22 = = 1:
                        if b15 > 0:
                            b15 -= (b21 - 1)
                        else:
                            b14 -= (b21 - 1)
                            b13 -= (b21 - 1)
                            b11 = b21 != 1
                    else:
                        if b15 > 0:
                            b15 -= b21
                            b11 = True
                        else:
                            b14 -= b21 - 1
                            b13 -= b21 - 1
                if b9:
                    print(" " * b13 + b18 * b15 + b12.b1 + b19 * b15, b23 = '')
                    b9 = False
                else:
                    print(" " * (b14 - b20) + b18 * b15 + b12.b1 + b19 * b15, b23 = '')
                if b12.b2:
                    b7.fonk13(b12.b2)
                if b12.b3:
                    b7.fonk13(b12.b3)
            if not b7.fonk12():
                print("\n" + b10)
            a2 += 1
class class2:
    def fonk11(self):
        self.b24 = []
    def fonk12(self):
        return len(self.b24) == 0
    def fonk13(self, item):
        self.b24.append(item)
    def fonk14(self):
        if not self.fonk12():
            return self.b24.pop(0)
        return None
if b25 = = '__main__':
    b26 = class1('A')
    b26.b2 = class1('B')
    b26.b3 = class1('C')
    b26.b2.b2 = class1('D')
    b26.b2.b3 = class1('E')
    b26.b2.b3.b3 = class1.fonk4(b22)
    b26.b3.b2 = class1('F')
    b26.b3.b3 = class1('G')
    b26.b2.b2.b2 = class1('H')
    b26.b2.b2.b3 = class1('I')
    b26.b2.b3.b2 = class1('J')
    b26.b3.b3.b2 = class1('N')
    b26.b3.b3.b3 = class1('O')
    b26.fonk10()
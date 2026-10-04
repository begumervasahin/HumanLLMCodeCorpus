from b8 import deepcopy
import sys
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
        else:
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
        b7 = Queue()
        b7.enqueue(b4)
        a2 = 1
        while not b7.is_empty():
            b8 = Queue()
            while not b7.is_empty():
                b8.enqueue(b7.dequeue())
            b9 = True
            b10 = ""
            b11 = False
            while not b8.is_empty():
                b12 = b8.dequeue()
                b13 = b21 ** (b6 - a2 + 1) - b21
                b14 = b21 ** (b6 - a2 + b21) - b21
                b15 = b21 ** (b6 - a2) - b21
                b15 = max(b15, 0)
                b14 -= b15 * b21
                b13 -= b15
                a3 = b21
                b13 += a3
                if b9:
                    b10 += " " * a3
                b16 = "/" if b12.b2 and b12.b2.b1 != " " else " "
                if b9:
                    b10 += " " * (b21 ** (b6 - a2) - 1) + b16
                else:
                    b10 += " " * (b21 ** (b6 - a2 + 1) + 1) + b16
                b16 = "\\" if b12.b3 and b12.b3.b1 != " " else " "
                b10 += " " * (b21 ** (b6 - a2 + 1) - 3) + b16
                b17 = "_" if b12.b2 and b12.b2.b1 != " " else " "
                b18 = "_" if b12.b3 and b12.b3.b1 != " " else " "
                b19 = 1 if b11 else 0
                b11 = False
                b20 = len(str(b12.b1))
                if b20 > 1:
                    if b20 % b21 = = 1:
                        if b15 > 0:
                            b15 -= (b20 - 1)
                        else:
                            b14 -= (b20 - 1)
                            b13 -= (b20 - 1)
                            b11 = b20 != 1
                    else:
                        if b15 > 0:
                            b15 -= b20
                            b11 = True
                        else:
                            b14 -= b20 - 1
                            b13 -= b20 - 1
                if b9:
                    print(" " * b13 + b17 * b15 + b12.b1 + b18 * b15, b22 = '')
                    b9 = False
                else:
                    print(" " * (b14 - b19) + b17 * b15 + b12.b1 + b18 * b15, b22 = '')
                if b12.b2:
                    b7.enqueue(b12.b2)
                if b12.b3:
                    b7.enqueue(b12.b3)
            if not b7.is_empty():
                print("\n" + b10)
            a2 += 1
if b23 = = '__main__':
    b24 = class1('A')
    b24.b2 = class1('B')
    b24.b3 = class1('C')
    b24.b2.b2 = class1('D')
    b24.b2.b3 = class1('E')
    b24.b2.b3.b3 = class1.fonk4(b21)
    b24.b3.b2 = class1('F')
    b24.b3.b3 = class1('G')
    b24.b2.b2.b2 = class1('H')
    b24.b2.b2.b3 = class1('I')
    b24.b2.b3.b2 = class1('J')
    b24.b3.b3.b2 = class1('N')
    b24.b3.b3.b3 = class1('O')
    b24.fonk10()
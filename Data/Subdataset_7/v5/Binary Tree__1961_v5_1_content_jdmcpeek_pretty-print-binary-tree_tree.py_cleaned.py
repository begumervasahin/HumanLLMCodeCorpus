import sys
from modules.b7 import Queue
from b8 import deepcopy
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
        b4 = class1('X')
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
        return self.fonk7()
    def fonk7(self):
        if not self:
            return 0
        else:
            return max(self.b2.fonk7() if self.b2 else 0, self.b3.fonk7() if self.b3 else 0) + 1
    def fonk8(self, height):
        self.fonk9(height)
    def fonk9(self, height):
        if height <= 1:
            return
        if self:
            if not self.b2:
                self.b2 = class1(' ')
            if not self.b3:
                self.b3 = class1(' ')
            self.b2.fonk9(height - 1)
            self.b3.fonk9(height - 1)
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
                b13 = b20 ** (b6 - a2 + 1) - b20
                b14 = b20 ** (b6 - a2 + b20) - b20
                b15 = b20 ** (b6 - a2) - b20
                b15 = max(0, b15)
                b14 -= b15 * b20
                b13 -= b15
                a3 = b20
                b13 += a3
                if b9:
                    b10 += " " * a3
                b16 = "/" if b12.b2 and b12.b2.b1 != " " else " "
                if b9:
                    b10 += " " * (b20 ** (b6 - a2) - 1) + b16
                else:
                    b10 += " " * (b20 ** (b6 - a2 + 1) + 1) + b16
                b16 = "\\" if b12.b3 and b12.b3.b1 != " " else " "
                b10 += " " * (b20 ** (b6 - a2 + 1) - 3) + b16
                b17 = "_" if b12.b2 and b12.b2.b1 != " " else " "
                b18 = "_" if b12.b3 and b12.b3.b1 != " " else " "
                if b11:
                    a4 = 1
                    b11 = False
                else:
                    a4 = 0
                b19 = len(str(b12.b1))
                if b19 > 1:
                    if b19 % b20 = = 1:
                        if b15 > 0:
                            b15 -= (b19 - 1)
                        else:
                            b14 -= (b19 - 1)
                            b13 -= (b19 - 1)
                            if b19 != 1:
                                b11 = True
                    else:
                        if b15 > 0:
                            b15 -= (b19
                            b11 = True
                        else:
                            b14 -= (b19 - 1)
                            b13 -= (b19 - 1)
                if b9:
                    print(" " * b13, b21 = '')
                    print(b17 * b15, b21 = '')
                    print(b12.b1, b21 = '')
                    print(b18 * b15, b21 = '')
                    b9 = False
                else:
                    print(" " * (b14 - a4), b21 = '')
                    print(b17 * b15, b21 = '')
                    print(b12.b1, b21 = '')
                    print(b18 * b15, b21 = '')
                if b12.b2:
                    b7.enqueue(b12.b2)
                if b12.b3:
                    b7.enqueue(b12.b3)
            if not b7.is_empty():
                print("\n" + b10)
            a2 += 1
if b22 = = '__main__':
    b23 = class1('A')
    b23.b2 = class1('B')
    b23.b3 = class1('C')
    b23.b2.b2 = class1('D')
    b23.b2.b3 = class1('E')
    b23.b2.b3.b3 = class1.fonk4(b20)
    b23.b3.b2 = class1('F')
    b23.b3.b3 = class1('G')
    b23.b2.b2.b2 = class1('H')
    b23.b2.b2.b3 = class1('I')
    b23.b2.b3.b2 = class1('J')
    b23.b3.b3.b2 = class1('N')
    b23.b3.b3.b3 = class1('O')
    b23.fonk10()
from b9 import Queue
from b10 import deepcopy
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        print(self.b1, b4 = '')
    def fonk3(self):
        a1 = 1
        if self.b2:
            a1 += self.b2.fonk3()
        if self.b3:
            a1 += self.b3.fonk3()
        return a1
    @classmethod
    def fonk4(cls, depth):
        b5 = class1('X')
        cls.fonk5(b5, depth, 1)
        return b5
    @staticmethod
    def fonk5(b14, depth, b6):
        if b6 = = depth:
            return
        b14.b2 = class1('X')
        b14.b3 = class1('XX')
        class1.fonk5(b14.b2, depth, b6 + 1)
        class1.fonk5(b14.b3, depth, b6 + 1)
    def fonk6(self):
        return class1.fonk7(self)
    @staticmethod
    def fonk7(b14):
        if not b14:
            return 0
        return max(class1.fonk7(b14.b2), class1.fonk7(b14.b3)) + 1
    def fonk8(self, height):
        class1.fonk9(self, height)
    @staticmethod
    def fonk9(b14, height):
        if height <= 1:
            return
        if b14:
            if not b14.b2:
                b14.b2 = class1(' ')
            if not b14.b3:
                b14.b3 = class1(' ')
            class1.fonk9(b14.b2, height - 1)
            class1.fonk9(b14.b3, height - 1)
    def fonk10(self):
        b7 = self.fonk6()
        b8 = deepcopy(self)
        b8.fonk8(b7)
        b9 = Queue()
        b9.put(b8)
        for gen in range(1, b7 + 1):
            b10 = Queue()
            while not b9.empty():
                b10.put(b9.get())
            b11 = True
            b12 = ""
            b13 = False
            while not b10.empty():
                b14 = b10.get()
                b15 = 2**(b7 - gen + 1) - 2
                b16 = 2**(b7 - gen + 2) - 2
                b17 = 2**(b7 - gen) - 2
                if b17 < 0:
                    b17 = 0
                b16 -= b17 * 2
                b15 -= b17
                b15 += 2
                if b11:
                    b12 += " " * 2
                b18 = "/" if b14.b2 and b14.b2.b1 != " " else " "
                if b11:
                    b12 += " " * (2**(b7 - gen) - 1) + b18
                else:
                    b12 += " " * (2**(b7 - gen + 1) + 1) + b18
                b19 = "\\" if b14.b3 and b14.b3.b1 != " " else " "
                b12 += " " * (2**(b7 - gen + 1) - 3) + b19
                b20 = "_" if b14.b2 and b14.b2.b1 != " " else " "
                b21 = "_" if b14.b3 and b14.b3.b1 != " " else " "
                b22 = 1 if len(str(b14.b1)) % 2 == 0 and b17 > 0 else 0
                b23 = len(str(b14.b1))
                if b11:
                    print(" " * b15 + b20 * b17 + b14.b1 + b21 * b17, b4 = '')
                    b11 = False
                else:
                    print(" " * (b16 - b22) + b20 * b17 + b14.b1 + b21 * b17, b4 = '')
                if b14.b2:
                    b9.put(b14.b2)
                if b14.b3:
                    b9.put(b14.b3)
            if not b9.empty():
                print("\n" + b12)
if b24 = = '__main__':
    b5 = class1('A')
    b5.b2 = class1('B')
    b5.b3 = class1('C')
    b5.b2.b2 = class1('D')
    b5.b2.b3 = class1('E')
    b5.b2.b3.b3 = class1.fonk4(2)
    b5.b3.b2 = class1('F')
    b5.b3.b3 = class1('G')
    b5.b2.b2.b2 = class1('H')
    b5.b2.b2.b3 = class1('I')
    b5.b2.b3.b2 = class1('J')
    b5.b3.b3.b2 = class1('N')
    b5.b3.b3.b3 = class1('O')
    b5.fonk10()
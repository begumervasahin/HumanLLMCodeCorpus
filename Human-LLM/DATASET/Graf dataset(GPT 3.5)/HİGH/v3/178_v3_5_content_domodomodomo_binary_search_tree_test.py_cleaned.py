import unittest
import random
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b1):
        self.b4 = self.fonk4(self.b4, b1)
    def fonk4(self, b6, b1):
        if b6 is None:
            return class1(b1)
        if b1 < b6.b1:
            b6.b2 = self.fonk4(b6.b2, b1)
        elif b1 > b6.b1:
            b6.b3 = self.fonk4(b6.b3, b1)
        return b6
    def fonk5(self):
        b5 = []
        self.fonk6(self.b4, b5)
        return b5
    def fonk6(self, b6, b5):
        if b6 is not None:
            self.fonk6(b6.b2, b5)
            b5.append(b6.b1)
            self.fonk6(b6.b3, b5)
    def fonk7(self, b1):
        self.b4 = self.fonk8(self.b4, b1)
    def fonk8(self, b6, b1):
        if b6 is None:
            return None
        if b1 < b6.b1:
            b6.b2 = self.fonk8(b6.b2, b1)
        elif b1 >= b6.b1:
            b6 = b6.b3
        return b6
    def fonk9(self, b1):
        self.b4 = self.fonk10(self.b4, b1)
    def fonk10(self, b6, b1):
        if b6 is None:
            return None
        if b1 > b6.b1:
            b6.b3 = self.fonk10(b6.b3, b1)
        elif b1 <= b6.b1:
            b6 = b6.b2
        return b6
    def fonk11(self):
        b5 = []
        b7 = []
        b8 = self.b4
        while b7 or b8:
            while b8:
                b7.append(b8)
                b8 = b8.b2
            b8 = b7.pop()
            b5.append(b8.b1)
            b8 = b8.b3
        return b5
class class3(unittest.TestCase):
    def fonk12(self):
        b9 = class2()
        for value in (random.randint(0, 99) for _ in range(1000)):
            b9.fonk3(value)
        b10 = b9.fonk5()
        random.shuffle(b10)
        for value in b10:
            b9.fonk7(value)
        self.assertEqual(b9.fonk5(), [])
    def fonk13(self):
        b9 = class2()
        for value in (random.randint(0, 99) for _ in range(1000)):
            b9.fonk3(value)
        b10 = b9.fonk11()
        random.shuffle(b10)
        for value in b10:
            b9.fonk9(value)
        self.assertEqual(b9.fonk5(), [])
if b11 = = '__main__':
    unittest.main()
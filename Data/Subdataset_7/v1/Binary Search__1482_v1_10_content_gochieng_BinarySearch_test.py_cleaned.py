class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, index):
        return (index + 1) * self.b2
    def fonk3(self, target):
        a1 = 0
        b6, b3 = 0, self.b1 - 1
        while b6 <= b3:
            a1 += 1
            b4 = (b6 + b3)
            b5 = self[b4]
            if b5 = = target:
                return {'a1': a1, 'index': b4}
            elif b5 < target:
                b6 = b4 + 1
            else:
                b3 = b4 - 1
        return {'a1': a1, 'index': -1}
import unittest
class class2(unittest.TestCase):
    def fonk4(self):
        self.b7 = class1(20, 1)
        self.b8 = class1(20, 2)
        self.b9 = class1(100, 10)
    def fonk5(self):
        b10 = self.b7.fonk3(16)
        self.assertGreater(
            5,
            b10['a1'],
            b11 = 'should return {a1: 4, index: 15} for 16'
        )
        self.assertEqual(
            15,
            b10['index'],
            b11 = 'should return {a1: 4, index: 15} for 16'
        )
    def fonk6(self):
        pass
    def fonk7(self):
        pass
class class3(unittest.TestCase):
    def fonk8(self):
        self.b7 = class1(20, 1)
        self.b8 = class1(20, 2)
        self.b9 = class1(100, 10)
    def fonk9(self):
        pass
    def fonk10(self):
        pass
    def fonk11(self):
        pass
if b12 = = '__main__':
    unittest.main()
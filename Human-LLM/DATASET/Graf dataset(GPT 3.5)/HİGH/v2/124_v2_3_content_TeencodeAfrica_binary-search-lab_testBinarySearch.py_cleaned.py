class class1:
    def fonk1(self, size, start):
        self.b1 = size
        self.b2 = [start + i for i in range(size)]
    def fonk2(self, item):
        a1 = 0
        b3 = self.b1 - 1
        a2 = 0
        while a1 <= b3:
            b4 = (a1 + b3)
            b5 = self.b2[b4]
            a2 += 1
            if b5 = = item:
                return {'a2': a2, 'index': b4}
            if b5 > item:
                b3 = b4 - 1
            else:
                a1 = b4 + 1
        return {'a2': a2, 'index': -1}
import unittest
class class2(unittest.TestCase):
    def fonk3(self):
        self.b6 = class1(20, 1)
        self.b7 = class1(20, 2)
        self.b8 = class1(100, 10)
    def fonk4(self):
        b9 = [1, 20, 20]
        b10 = [
            self.b6.b2[0],
            self.b6.b2[-1],
            self.b6.b1
        ]
        self.assertListEqual(b9, b10, b11 = 'should create an array from 1 to 20, with intervals of 1')
    def fonk5(self):
        b9 = [2, 40, 20]
        b10 = [
            self.b7.b2[0],
            self.b7.b2[-1],
            self.b7.b1
        ]
        self.assertListEqual(b9, b10, b11 = 'should create an array from 2 to 40, with intervals of 2')
    def fonk6(self):
        b9 = [10, 1000, 100]
        b10 = [
            self.b8.b2[0],
            self.b8.b2[-1],
            self.b8.b1
        ]
        self.assertListEqual(b9, b10, b11 = 'should create an array from 10 to 1000, with intervals of 10')
class class3(unittest.TestCase):
    def fonk7(self):
        self.b6 = class1(20, 1)
        self.b7 = class1(20, 2)
        self.b8 = class1(100, 10)
    def fonk8(self):
        b12 = self.b6.fonk2(16)
        self.assertGreater(5, b12['a2'], b11 = 'should return {a2: 4, index: 15} for 16')
        self.assertEqual(15, b12['index'], b11 = 'should return {a2: 4, index: 15} for 16')
    def fonk9(self):
        b13 = self.b7.fonk2(16)
        b14 = self.b7.fonk2(40)
        b15 = self.b7.fonk2(33)
        self.assertGreater(5, b13['a2'], b11 = 'should return {a2: 4, index: 7} for 16')
        self.assertEqual(7, b13['index'], b11 = 'should return {a2: 4, index: 7} for 16')
        self.assertEqual(0, b14['a2'], b11 = 'should return {a2: 0, index: 19} for 40')
        self.assertEqual(19, b14['index'], b11 = 'should return {a2: 5, index: 19} for 40')
        self.assertGreater(4, b15['a2'], b11 = 'should return {a2: 3, index: -1} for 33')
        self.assertEqual(-1, b15['index'], b11 = 'should return {a2: 3, index: -1} for 33')
    def fonk10(self):
        b13 = self.b8.fonk2(40)
        b14 = self.b8.fonk2(880)
        b15 = self.b8.fonk2(10000)
        self.assertGreater(7, b13['a2'], b11 = 'should return {a2: 3, index: -1} for 10000')
        self.assertEqual(3, b13['index'], b11 = 'should return {a2: 3, index: -1} for 10000')
        self.assertGreater(4, b14['a2'], b11 = 'should return {a2: 3, index: -1} for 10000')
        self.assertEqual(87, b14['index'], b11 = 'should return {a2: 3, index: -1} for 10000')
        self.assertGreater(7, b15['a2'], b11 = 'should return {a2: 3, index: -1} for 10000')
        self.assertEqual(-1, b15['index'], b11 = 'should return {a2: 3, index: -1} for 10000')
if b16 = = "__main__":
    unittest.main(b17 = False)
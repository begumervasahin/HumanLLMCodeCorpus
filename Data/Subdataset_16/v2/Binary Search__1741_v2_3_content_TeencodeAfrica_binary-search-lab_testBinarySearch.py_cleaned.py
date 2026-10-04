class class1:
    def fonk1(self, b1, interval):
        self.b1 = b1
        self.b2 = [(i * interval) + interval for i in range(b1)]
    def fonk2(self, index):
        return self.b2[index]
    def fonk3(self):
        return len(self.b2)
    def fonk4(self, value):
        b6, b3 = 0, self.b1 - 1
        a1 = 0
        while b6 <= b3:
            a1 += 1
            b4 = (b6 + b3)
            b5 = self.b2[b4]
            if b5 = = value:
                return {'a1': a1, 'index': b4}
            elif b5 < value:
                b6 = b4 + 1
            else:
                b3 = b4 - 1
        return {'a1': a1, 'index': -1}
import unittest
class class2(unittest.TestCase):
    def fonk5(self):
        self.b7 = class1(20, 1)
        self.b8 = class1(20, 2)
        self.b9 = class1(100, 10)
    def fonk6(self):
        self.assertListEqual(
            [1, 20, 20],
            [
                self.b7[0],
                self.b7[19],
                self.b7.b1
            ],
            b10 = 'The b2 should be created from 1 to 20, with intervals of 1'
        )
        for index in range(self.b7.b1 - 1):
            self.assertEqual(
                1,
                self.b7[index + 1] - self.b7[index],
                b10 = 'Each consecutive number should have an interval of 1'
            )
    def fonk7(self):
        self.assertListEqual(
            [2, 40, 20],
            [
                self.b8[0],
                self.b8[19],
                self.b8.b1
            ],
            b10 = 'The b2 should be created from 2 to 40, with intervals of 2'
        )
        for index in range(self.b8.b1 - 1):
            self.assertEqual(
                2,
                self.b8[index + 1] - self.b8[index],
                b10 = 'Each consecutive number should have an interval of 2'
            )
    def fonk8(self):
        self.assertListEqual(
            [10, 1000, 100],
            [
                self.b9[0],
                self.b9[99],
                self.b9.b1
            ],
            b10 = 'The b2 should be created from 10 to 1000, with intervals of 10'
        )
        for index in range(self.b9.b1 - 1):
            self.assertEqual(
                10,
                self.b9[index + 1] - self.b9[index],
                b10 = 'Each consecutive number should have an interval of 10'
            )
class class3(unittest.TestCase):
    def fonk9(self):
        self.b7 = class1(20, 1)
        self.b8 = class1(20, 2)
        self.b9 = class1(100, 10)
    def fonk10(self):
        b11 = self.b7.fonk4(16)
        self.assertGreater(
            5,
            b11['a1'],
            b10 = 'The search should return {a1: 4, index: 15} for 16'
        )
        self.assertEqual(
            15,
            b11['index'],
            b10 = 'The search should return {a1: 4, index: 15} for 16'
        )
    def fonk11(self):
        b12 = self.b8.fonk4(16)
        b13 = self.b8.fonk4(40)
        b14 = self.b8.fonk4(33)
        self.assertGreater(
            5,
            b12['a1'],
            b10 = 'The search should return {a1: 4, index: 7} for 16'
        )
        self.assertEqual(
            7,
            b12['index'],
            b10 = 'The search should return {a1: 4, index: 7} for 16'
        )
        self.assertEqual(
            0,
            b13['a1'],
            b10 = 'The search should return {a1: 0, index: 19} for 40'
        )
        self.assertEqual(
            19,
            b13['index'],
            b10 = 'The search should return {a1: 0, index: 19} for 40'
        )
        self.assertGreater(
            4,
            b14['a1'],
            b10 = 'The search should return {a1: 3, index: -1} for 33'
        )
        self.assertEqual(
            -1,
            b14['index'],
            b10 = 'The search should return {a1: 3, index: -1} for 33'
        )
    def fonk12(self):
        b13 = self.b9.fonk4(40)
        b15 = self.b9.fonk4(880)
        b16 = self.b9.fonk4(10000)
        self.assertGreater(
            7,
            b13['a1'],
            b10 = 'The search should return {a1: 3, index: 3} for 40'
        )
        self.assertEqual(
            3,
            b13['index'],
            b10 = 'The search should return {a1: 3, index: 3} for 40'
        )
        self.assertGreater(
            4,
            b15['a1'],
            b10 = 'The search should return {a1: 5, index: 87} for 880'
        )
        self.assertEqual(
            87,
            b15['index'],
            b10 = 'The search should return {a1: 5, index: 87} for 880'
        )
        self.assertGreater(
            7,
            b16['a1'],
            b10 = 'The search should return {a1: 3, index: -1} for 10000'
        )
        self.assertEqual(
            -1,
            b16['index'],
            b10 = 'The search should return {a1: 3, index: -1} for 10000'
        )
if b17 = = "__main__":
    unittest.main(b18 = False)
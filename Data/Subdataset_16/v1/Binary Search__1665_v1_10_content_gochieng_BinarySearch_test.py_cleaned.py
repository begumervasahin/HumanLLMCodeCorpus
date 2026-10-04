class class1:
    def fonk1(self, b1, interval):
        self.b1 = b1
        self.b2 = [i * interval + interval for i in range(b1)]
    def fonk2(self, index):
        return self.b2[index]
    def fonk3(self):
        return len(self.b2)
    def fonk4(self, value):
        a1 = 0
        b3 = self.b1 - 1
        a2 = 0
        while a1 <= b3:
            a2 += 1
            b4 = (a1 + b3)
            b5 = self.b2[b4]
            if b5 = = value:
                return {'a2': a2, 'index': b4}
            elif b5 < value:
                a1 = b4 + 1
            else:
                b3 = b4 - 1
        return {'a2': a2, 'index': -1}
import unittest
class class2(unittest.TestCase):
    def fonk5(self):
        self.b6 = class1(20, 1)
        self.b7 = class1(20, 2)
        self.b8 = class1(100, 10)
    def fonk6(self):
        self.assertListEqual(
            [1, 20, 20],
            [
                self.b6[0],
                self.b6[19],
                self.b6.b1
            ],
            b9 = 'should create an b2 from 1 to 20, with intervals of 1'
        )
        for index in range(self.b6.b1):
            if index < self.b6.b1 - 1:
                self.assertEqual(
                    1,
                    self.b6[index + 1] - self.b6[index],
                    b9 = 'should return 1 for consecutive numbers'
                )
    def fonk7(self):
        self.assertListEqual(
            [2, 40, 20],
            [
                self.b7[0],
                self.b7[19],
                self.b7.b1
            ],
            b9 = 'should create an b2 from 2 to 40, with intervals of 2'
        )
        for index in range(self.b7.b1):
            if index < self.b7.b1 - 1:
                self.assertEqual(
                    2,
                    self.b7[index + 1] - self.b7[index],
                    b9 = 'should return 2 for consecutive numbers'
                )
    def fonk8(self):
        self.assertListEqual(
            [10, 1000, 100],
            [
                self.b8[0],
                self.b8[99],
                self.b8.b1
            ],
            b9 = 'should create an b2 from 10 to 1000, with intervals of 10'
        )
        for index in range(self.b8.b1):
            if index < self.b8.b1 - 1:
                self.assertEqual(
                    10,
                    self.b8[index + 1] - self.b8[index],
                    b9 = 'should return 10 for consecutive numbers'
                )
class class3(unittest.TestCase):
    def fonk9(self):
        self.b6 = class1(20, 1)
        self.b7 = class1(20, 2)
        self.b8 = class1(100, 10)
    def fonk10(self):
        b10 = self.b6.fonk4(16)
        self.assertGreater(
            5,
            b10['a2'],
            b9 = 'should return {a2: 4, index: 15} for 16'
        )
        self.assertEqual(
            15,
            b10['index'],
            b9 = 'should return {a2: 4, index: 15} for 16'
        )
    def fonk11(self):
        b11 = self.b7.fonk4(16)
        b12 = self.b7.fonk4(40)
        b13 = self.b7.fonk4(33)
        self.assertGreater(
            5,
            b11['a2'],
            b9 = 'should return {a2: 4, index: 7} for 16'
        )
        self.assertEqual(
            7,
            b11['index'],
            b9 = 'should return {a2: 4, index: 7} for 16'
        )
        self.assertEqual(
            0,
            b12['a2'],
            b9 = 'should return {a2: 0, index: 19} for 40'
        )
        self.assertEqual(
            19,
            b12['index'],
            b9 = 'should return {a2: 0, index: 19} for 40'
        )
        self.assertGreater(
            4,
            b13['a2'],
            b9 = 'should return {a2: 3, index: -1} for 33'
        )
        self.assertEqual(
            -1,
            b13['index'],
            b9 = 'should return {a2: 3, index: -1} for 33'
        )
    def fonk12(self):
        b11 = self.b8.fonk4(40)
        b12 = self.b8.fonk4(880)
        b13 = self.b8.fonk4(10000)
        self.assertGreater(
            7,
            b11['a2'],
            b9 = 'should return {a2: 3, index: 3} for 40'
        )
        self.assertEqual(
            3,
            b11['index'],
            b9 = 'should return {a2: 3, index: 3} for 40'
        )
        self.assertGreater(
            4,
            b12['a2'],
            b9 = 'should return {a2: 5, index: 87} for 880'
        )
        self.assertEqual(
            87,
            b12['index'],
            b9 = 'should return {a2: 5, index: 87} for 880'
        )
        self.assertGreater(
            7,
            b13['a2'],
            b9 = 'should return {a2: 3, index: -1} for 10000'
        )
        self.assertEqual(
            -1,
            b13['index'],
            b9 = 'should return {a2: 3, index: -1} for 10000'
        )
if b14 = = '__main__':
    unittest.main()
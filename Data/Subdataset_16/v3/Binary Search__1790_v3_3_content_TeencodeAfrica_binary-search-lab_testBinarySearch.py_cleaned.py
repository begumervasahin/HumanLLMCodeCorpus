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
        self.assertEqual(self.b7[0], 1)
        self.assertEqual(self.b7[19], 20)
        self.assertEqual(len(self.b7), 20)
        for index in range(len(self.b7) - 1):
            self.assertEqual(
                self.b7[index + 1] - self.b7[index],
                1,
                b10 = 'Each consecutive number should have an interval of 1'
            )
    def fonk7(self):
        self.assertEqual(self.b8[0], 2)
        self.assertEqual(self.b8[19], 40)
        self.assertEqual(len(self.b8), 20)
        for index in range(len(self.b8) - 1):
            self.assertEqual(
                self.b8[index + 1] - self.b8[index],
                2,
                b10 = 'Each consecutive number should have an interval of 2'
            )
    def fonk8(self):
        self.assertEqual(self.b9[0], 10)
        self.assertEqual(self.b9[99], 1000)
        self.assertEqual(len(self.b9), 100)
        for index in range(len(self.b9) - 1):
            self.assertEqual(
                self.b9[index + 1] - self.b9[index],
                10,
                b10 = 'Each consecutive number should have an interval of 10'
            )
class class3(unittest.TestCase):
    def fonk9(self):
        self.b7 = class1(20, 1)
        self.b8 = class1(20, 2)
        self.b9 = class1(100, 10)
    def fonk10(self):
        b11 = self.b7.fonk4(16)
        self.assertEqual(b11['a1'], 5)
        self.assertEqual(b11['index'], 15)
    def fonk11(self):
        b12 = self.b8.fonk4(16)
        b13 = self.b8.fonk4(40)
        b14 = self.b8.fonk4(33)
        self.assertEqual(b12['a1'], 5)
        self.assertEqual(b12['index'], 7)
        self.assertEqual(b13['a1'], 1)
        self.assertEqual(b13['index'], 19)
        self.assertEqual(b14['a1'], 5)
        self.assertEqual(b14['index'], -1)
    def fonk12(self):
        b13 = self.b9.fonk4(40)
        b15 = self.b9.fonk4(880)
        b16 = self.b9.fonk4(10000)
        self.assertEqual(b13['a1'], 3)
        self.assertEqual(b13['index'], 3)
        self.assertEqual(b15['a1'], 5)
        self.assertEqual(b15['index'], 87)
        self.assertEqual(b16['a1'], 8)
        self.assertEqual(b16['index'], -1)
if b17 = = "__main__":
    unittest.main()
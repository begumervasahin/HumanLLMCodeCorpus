from collections import namedtuple
import unittest
b1 = namedtuple('b1', ['index', 'value'])
b2 = namedtuple('b2', ['b3', 'b4', 'b5'])
class class1:
    def fonk1(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = [b1(index, value) for index, value in enumerate(b5)]
    def fonk2(self):
        if not self.fonk3():
            return "Error: invalid input"
        a1 = 0
        for i in range(len(self.b6)):
            for j in range(i + 1, len(self.b6)):
                if (self.b6[i].value + self.b6[j].value) % self.b4 = = 0:
                    a1 += 1
        return a1
    def fonk3(self):
        return 2 <= self.b3 <= 100 and 1 <= self.b4 <= 100 and len(self.b5) <= 100
b7 = b2(b3=6, b4=3, b5=[1, 3, 2, 6, 1, 2])
b8 = b2(b3=10, b4=3, b5=[29, 97, 52, 86, 27, 89, 77, 19, 99, 96])
b9 = b2(b3=100, b4=22, b5=[
    43, 95, 51, 55, 40, 86, 65, 81, 51, 20, 47, 50, 65, 53, 23, 78,
    75, 75, 47, 73, 25, 27, 14, 8, 26, 58, 95, 28, 3, 23, 48, 69,
    26, 3, 73, 52, 34, 7, 40, 33, 56, 98, 71, 29, 70, 71, 28, 12,
    18, 49, 19, 25, 2, 18, 15, 41, 51, 42, 46, 19, 98, 56, 54, 98,
    72, 25, 16, 49, 34, 99, 48, 93, 64, 44, 50, 91, 44, 17, 63, 27,
    3, 65, 75, 19, 68, 30, 43, 37, 72, 54, 82, 92, 37, 52, 72, 62,
    3, 88, 82, 71
])
class class2(unittest.TestCase):
    def fonk4(self):
        b10 = class1(b7.b3, b7.b4, b7.b5)
        b11 = class1(b8.b3, b8.b4, b8.b5)
        b12 = class1(b9.b3, b9.b4, b9.b5)
        self.assertEqual(5, b10.fonk2())
        self.assertEqual(15, b11.fonk2())
        self.assertEqual(216, b12.fonk2())
    def fonk5(self):
        b13 = [
            class1(0, 3, [1, 2, 3]),
            class1(101, 3, [1, 2, 3]),
            class1(2, 0, [1, 2, 3]),
            class1(2, 101, [1, 2, 3]),
            class1(2, 1, []),
            class1(2, 1, [x for x in range(102)])
        ]
        for case in b13:
            self.assertEqual("Error: invalid input", case.fonk2())
if b14 = = "__main__":
    unittest.main()
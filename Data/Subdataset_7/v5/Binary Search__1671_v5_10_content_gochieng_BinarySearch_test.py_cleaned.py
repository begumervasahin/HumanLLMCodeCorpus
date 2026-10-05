import unittest
from binarysearch import BinarySearch
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = BinarySearch(20, 1)
        self.b2 = BinarySearch(20, 2)
        self.b3 = BinarySearch(100, 10)
    def fonk2(self):
        b4 = [1, 20, 20]
        b5 = [
            self.b1[0],
            self.b1[19],
            self.b1.length
        ]
        self.assertListEqual(
            b4,
            b5,
            b6 = 'should create an array from 1 to 20, with intervals of 1'
        )
        for index, number in enumerate(self.b1):
            if index < self.b1.length - 1:
                self.assertEqual(
                    1,
                    self.b1[index + 1] - self.b1[index],
                    b6 = 'should return 1 for consecutive numbers'
                )
    def fonk3(self):
        b4 = [2, 40, 20]
        b5 = [
            self.b2[0],
            self.b2[19],
            self.b2.length
        ]
        self.assertListEqual(
            b4,
            b5,
            b6 = 'should create an array from 2 to 40, with intervals of 2'
        )
        for index, number in enumerate(self.b2):
            if index < self.b2.length - 1:
                self.assertEqual(
                    2,
                    self.b2[index + 1] - self.b2[index],
                    b6 = 'should return 2 for consecutive numbers'
                )
    def fonk4(self):
        b4 = [10, 1000, 100]
        b5 = [
            self.b3[0],
            self.b3[99],
            self.b3.length
        ]
        self.assertListEqual(
            b4,
            b5,
            b6 = 'should create an array from 10 to 1000, with intervals of 10'
        )
        for index, number in enumerate(self.b3):
            if index < self.b3.length - 1:
                self.assertEqual(
                    10,
                    self.b3[index + 1] - self.b3[index],
                    b6 = 'should return 10 for consecutive numbers'
                )
class class2(unittest.TestCase):
    def fonk5(self):
        self.b1 = BinarySearch(20, 1)
        self.b2 = BinarySearch(20, 2)
        self.b3 = BinarySearch(100, 10)
    def fonk6(self):
        b7 = self.b1.b7(16)
        self.assertGreater(
            b7['count'],
            5,
            b6 = 'should return {count: 4, index: 15} for 16'
        )
        self.assertEqual(
            b7['index'],
            15,
            b6 = 'should return {count: 4, index: 15} for 16'
        )
    def fonk7(self):
        pass
    def fonk8(self):
        pass
if b8 = = '__main__':
    unittest.main()
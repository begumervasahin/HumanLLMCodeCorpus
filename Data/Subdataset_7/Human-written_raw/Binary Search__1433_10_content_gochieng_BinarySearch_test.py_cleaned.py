import unittest
from binarysearch import BinarySearch
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = BinarySearch(20, 1)
        self.b2 = BinarySearch(20, 2)
        self.b3 = BinarySearch(100, 10)
    def fonk2(self):
        self.assertListEqual(
            [1, 20, 20],
            [
                self.b1[0],
                self.b1[19],
                self.b1.length
            ],
            b4 = 'should create an array from 1 to 20, with intervals of 1'
        )
        for index, number in enumerate(self.b1):
            if index < self.b1.length - 1:
                self.assertEqual(
                    1,
                    self.b1[index + 1] - self.b1[index],
                    b4 = 'should return 1 for consequtive numbers'
                )
    def fonk3(self):
        self.assertListEqual(
            [2, 40, 20],
            [
                self.b2[0],
                self.b2[19],
                self.b2.length
            ],
            b4 = 'should create an array from 2 to 40, with intervals of 2'
        )
        for index, number in enumerate(self.b2):
            if index < self.b2.length - 1:
                self.assertEqual(
                    2,
                    self.b2[index + 1] - self.b2[index],
                    b4 = 'should return 2 for consequtive numbers')
    def fonk4(self):
        self.assertListEqual(
            [10, 1000, 100],
            [
                self.b3[0],
                self.b3[99],
                self.b3.length
            ],
            b4 = 'should create an array from 10 to 1000, with intervals of 10'
        )
        for index, number in enumerate(self.b3):
            if index < self.b3.length - 1:
                self.assertEqual(
                    10,
                    self.b3[index + 1] -
                    self.b3[index],
                    b4 = 'should return 10 for consequtive numbers'
                )
class class2(unittest.TestCase):
    def fonk5(self):
        self.b1 = BinarySearch(20, 1)
        self.b2 = BinarySearch(20, 2)
        self.b3 = BinarySearch(100, 10)
    def fonk6(self):
        b5 = self.b1.b5(16)
        self.assertGreater(
            5,
            b5['count'],
            b4 = 'should return {count: 4, index: 15} for 16'
        )
        self.assertEqual(
            15,
            b5['index'],
            b4 = 'should return {count: 4, index: 15} for 16'
        )
    def fonk7(self):
        b6 = self.b2.b5(16)
        b7 = self.b2.b5(40)
        b8 = self.b2.b5(33)
        self.assertGreater(
            5,
            b6['count'],
            b4 = 'should return {count: 4, index: 7} for 16'
        )
        self.assertEqual(
            7,
            b6['index'],
            b4 = 'should return {count: 4, index: 7} for 16'
        )
        self.assertEqual(
            0,
            b7['count'],
            b4 = 'should return {count: 0, index: 19} for 40'
        )
        self.assertEqual(
            19,
            b7['index'],
            b4 = 'should return {count: 5, index: 19} for 40'
        )
        self.assertGreater(
            4,
            b8['count'],
            b4 = 'should return {count: 3, index: -1} for 33'
        )
        self.assertEqual(
            -1,
            b8['index'],
            b4 = 'should return {count: 3, index: -1} for 33'
        )
    def fonk8(self):
        b6 = self.b3.b5(40)
        b7 = self.b3.b5(880)
        b8 = self.b3.b5(10000)
        self.assertGreater(
            7,
            b6['count'],
            b4 = 'should return {count:
        )
        self.assertEqual(
            3,
            b6['index'],
            b4 = 'should return {count:
        )
        self.assertGreater(
            4,
            b7['count'],
            b4 = 'should return {count:
        )
        self.assertEqual(
            87,
            b7['index'],
            b4 = 'should return {count:
        )
        self.assertGreater(
            7,
            b8['count'],
            b4 = 'should return {count: 3, index: -1} for 10000'
        )
        self.assertEqual(
            -1,
            b8['index'],
            b4 = 'should return {count: 3, index: -1} for 10000'
        )
if b9 = = '__main__':
    unittest.main()
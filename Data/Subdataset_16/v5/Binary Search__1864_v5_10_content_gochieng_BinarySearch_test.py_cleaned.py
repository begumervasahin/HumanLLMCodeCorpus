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
            b4 = 'The list should be correctly generated from 1 to 20 with an interval of 1.'
        )
        for index in range(self.b1.length - 1):
            self.assertEqual(
                1,
                self.b1[index + 1] - self.b1[index],
                b4 = 'Each consecutive element should have a difference of 1.'
            )
    def fonk3(self):
        self.assertListEqual(
            [2, 40, 20],
            [
                self.b2[0],
                self.b2[19],
                self.b2.length
            ],
            b4 = 'The list should be correctly generated from 2 to 40 with an interval of 2.'
        )
        for index in range(self.b2.length - 1):
            self.assertEqual(
                2,
                self.b2[index + 1] - self.b2[index],
                b4 = 'Each consecutive element should have a difference of 2.'
            )
    def fonk4(self):
        self.assertListEqual(
            [10, 1000, 100],
            [
                self.b3[0],
                self.b3[99],
                self.b3.length
            ],
            b4 = 'The list should be correctly generated from 10 to 1000 with an interval of 10.'
        )
        for index in range(self.b3.length - 1):
            self.assertEqual(
                10,
                self.b3[index + 1] - self.b3[index],
                b4 = 'Each consecutive element should have a difference of 10.'
            )
class class2(unittest.TestCase):
    def fonk5(self):
        self.b1 = BinarySearch(20, 1)
        self.b2 = BinarySearch(20, 2)
        self.b3 = BinarySearch(100, 10)
    def fonk6(self):
        b5 = self.b1.search(16)
        self.assertGreater(
            5,
            b5['count'],
            b4 = 'The search for 16 should take fewer than 5 steps.'
        )
        self.assertEqual(
            15,
            b5['index'],
            b4 = 'The index of 16 should be 15.'
        )
    def fonk7(self):
        b6 = self.b2.search(16)
        b7 = self.b2.search(40)
        b8 = self.b2.search(33)
        self.assertGreater(
            5,
            b6['count'],
            b4 = 'The search for 16 should take fewer than 5 steps.'
        )
        self.assertEqual(
            7,
            b6['index'],
            b4 = 'The index of 16 should be 7.'
        )
        self.assertEqual(
            0,
            b7['count'],
            b4 = 'The search for 40 should take 0 steps.'
        )
        self.assertEqual(
            19,
            b7['index'],
            b4 = 'The index of 40 should be 19.'
        )
        self.assertGreater(
            4,
            b8['count'],
            b4 = 'The search for 33 should take fewer than 4 steps.'
        )
        self.assertEqual(
            -1,
            b8['index'],
            b4 = '33 is not in the list, so the index should be -1.'
        )
    def fonk8(self):
        b6 = self.b3.search(40)
        b7 = self.b3.search(880)
        b8 = self.b3.search(10000)
        self.assertGreater(
            7,
            b6['count'],
            b4 = 'The search for 40 should take fewer than 7 steps.'
        )
        self.assertEqual(
            3,
            b6['index'],
            b4 = 'The index of 40 should be 3.'
        )
        self.assertGreater(
            4,
            b7['count'],
            b4 = 'The search for 880 should take fewer than 4 steps.'
        )
        self.assertEqual(
            87,
            b7['index'],
            b4 = 'The index of 880 should be 87.'
        )
        self.assertGreater(
            7,
            b8['count'],
            b4 = 'The search for 10000 should take fewer than 7 steps.'
        )
        self.assertEqual(
            -1,
            b8['index'],
            b4 = '10000 is not in the list, so the index should be -1.'
        )
if b9 = = '__main__':
    unittest.main()
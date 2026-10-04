import unittest
from binarySearch import binarySearch
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = binarySearch(20, 1)
        self.b2 = binarySearch(20, 2)
        self.b3 = binarySearch(100, 10)
    def fonk2(self):
        b4 = [1, 20, 20]
        b5 = [
            self.b1[0],
            self.b1[19],
            len(self.b1)
        ]
        self.assertListEqual(
            b4,
            b5,
            b6 = 'Should create an array from 1 to 20 with intervals of 1'
        )
        for index in range(len(self.b1) - 1):
            self.assertEqual(
                self.b1[index + 1] - self.b1[index],
                1,
                b6 = 'Each consecutive number should have an interval of 1'
            )
    def fonk3(self):
        b4 = [2, 40, 20]
        b5 = [
            self.b2[0],
            self.b2[19],
            len(self.b2)
        ]
        self.assertListEqual(
            b4,
            b5,
            b6 = 'Should create an array from 2 to 40 with intervals of 2'
        )
        for index in range(len(self.b2) - 1):
            self.assertEqual(
                self.b2[index + 1] - self.b2[index],
                2,
                b6 = 'Each consecutive number should have an interval of 2'
            )
    def fonk4(self):
        b4 = [10, 1000, 100]
        b5 = [
            self.b3[0],
            self.b3[99],
            len(self.b3)
        ]
        self.assertListEqual(
            b4,
            b5,
            b6 = 'Should create an array from 10 to 1000 with intervals of 10'
        )
        for index in range(len(self.b3) - 1):
            self.assertEqual(
                self.b3[index + 1] - self.b3[index],
                10,
                b6 = 'Each consecutive number should have an interval of 10'
            )
class class2(unittest.TestCase):
    def fonk5(self):
        self.b1 = binarySearch(20, 1)
        self.b2 = binarySearch(20, 2)
        self.b3 = binarySearch(100, 10)
    def fonk6(self):
        b7 = self.b1.search(16)
        self.assertEqual(b7['count'], 5, b6 = 'Should take 5 iterations to find 16')
        self.assertEqual(b7['index'], 15, b6 = 'Should return index 15 for 16')
    def fonk7(self):
        b8 = self.b2.search(16)
        b9 = self.b2.search(40)
        b10 = self.b2.search(33)
        self.assertEqual(b8['count'], 5, b6 = 'Should take 5 iterations to find 16')
        self.assertEqual(b8['index'], 7, b6 = 'Should return index 7 for 16')
        self.assertEqual(b9['count'], 1, b6 = 'Should take 1 iteration to find 40')
        self.assertEqual(b9['index'], 19, b6 = 'Should return index 19 for 40')
        self.assertEqual(b10['count'], 5, b6 = 'Should take 5 iterations to determine 33 is not in the list')
        self.assertEqual(b10['index'], -1, b6 = 'Should return index -1 for a value not found (33)')
    def fonk8(self):
        b9 = self.b3.search(40)
        b11 = self.b3.search(880)
        b12 = self.b3.search(10000)
        self.assertEqual(b9['count'], 3, b6 = 'Should take 3 iterations to find 40')
        self.assertEqual(b9['index'], 3, b6 = 'Should return index 3 for 40')
        self.assertEqual(b11['count'], 5, b6 = 'Should take 5 iterations to find 880')
        self.assertEqual(b11['index'], 87, b6 = 'Should return index 87 for 880')
        self.assertEqual(b12['count'], 8, b6 = 'Should take 8 iterations to determine 10000 is not in the list')
        self.assertEqual(b12['index'], -1, b6 = 'Should return index -1 for a value not found (10000)')
if b13 = = "__main__":
    unittest.main(b14 = False)
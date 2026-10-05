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
            self.b1.length
        ]
        self.assertListEqual(b4, b5, b6 = 'Failed to create array from 1 to 20 with intervals of 1')
        for index in range(self.b1.length - 1):
            self.assertEqual(
                1,
                self.b1[index + 1] - self.b1[index],
                b6 = 'Expected consecutive numbers with an interval of 1'
            )
    def fonk3(self):
        b4 = [2, 40, 20]
        b5 = [
            self.b2[0],
            self.b2[19],
            self.b2.length
        ]
        self.assertListEqual(b4, b5, b6 = 'Failed to create array from 2 to 40 with intervals of 2')
        for index in range(self.b2.length - 1):
            self.assertEqual(
                2,
                self.b2[index + 1] - self.b2[index],
                b6 = 'Expected consecutive numbers with an interval of 2'
            )
    def fonk4(self):
        b4 = [10, 1000, 100]
        b5 = [
            self.b3[0],
            self.b3[99],
            self.b3.length
        ]
        self.assertListEqual(b4, b5, b6 = 'Failed to create array from 10 to 1000 with intervals of 10')
        for index in range(self.b3.length - 1):
            self.assertEqual(
                10,
                self.b3[index + 1] - self.b3[index],
                b6 = 'Expected consecutive numbers with an interval of 10'
            )
class class2(unittest.TestCase):
    def fonk5(self):
        self.b1 = binarySearch(20, 1)
        self.b2 = binarySearch(20, 2)
        self.b3 = binarySearch(100, 10)
    def fonk6(self):
        b7 = self.b1.search(16)
        self.assertGreater(5, b7['count'], b6 = 'Expected at most 5 iterations for search')
        self.assertEqual(15, b7['index'], b6 = 'Expected index 15 for item 16')
    def fonk7(self):
        b8 = self.b2.search(16)
        b9 = self.b2.search(40)
        b10 = self.b2.search(33)
        self.assertGreater(5, b8['count'], b6 = 'Expected at most 5 iterations for search 16')
        self.assertEqual(7, b8['index'], b6 = 'Expected index 7 for item 16')
        self.assertEqual(0, b9['count'], b6 = 'Expected 0 iterations for search 40')
        self.assertEqual(19, b9['index'], b6 = 'Expected index 19 for item 40')
        self.assertGreater(4, b10['count'], b6 = 'Expected at most 4 iterations for search 33')
        self.assertEqual(-1, b10['index'], b6 = 'Expected index -1 for item 33')
    def fonk8(self):
        b8 = self.b3.search(40)
        b9 = self.b3.search(880)
        b10 = self.b3.search(10000)
        self.assertGreater(7, b8['count'], b6 = 'Expected at most 7 iterations for search 40')
        self.assertEqual(3, b8['index'], b6 = 'Expected index 3 for item 40')
        self.assertGreater(4, b9['count'], b6 = 'Expected at most 4 iterations for search 880')
        self.assertEqual(87, b9['index'], b6 = 'Expected index 87 for item 880')
        self.assertGreater(7, b10['count'], b6 = 'Expected more than 7 iterations for search 10000')
        self.assertEqual(-1, b10['index'], b6 = 'Expected index -1 for item 10000')
if b11 = = "__main__":
    unittest.main(b12 = False)
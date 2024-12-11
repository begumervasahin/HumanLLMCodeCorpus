import unittest
import random
from sorters import QuickSort, BubbleSort, InsertionSort
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.b2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.b2)
        print("Setting things up... Expected: {0} Non-Sorted: {1}".format(self.b1, self.b2))
    def fonk2(self):
        b3 = BubbleSort()
        b3.sort(self.b2, 0, len(self.b2) - 1)
        self.assertEqual(self.b1, self.b2)
    def fonk3(self):
        b3 = InsertionSort()
        b3.sort(self.b2)
        self.assertEqual(self.b1, self.b2)
    def fonk4(self):
        b3 = QuickSort()
        b3.sort(self.b2, 0, len(self.b2) - 1)
        self.assertEqual(self.b1, self.b2)
    def fonk5(self):
        print()
        self.assertEqual("foo", 1)
if b4 = = '__main__':
    unittest.main()
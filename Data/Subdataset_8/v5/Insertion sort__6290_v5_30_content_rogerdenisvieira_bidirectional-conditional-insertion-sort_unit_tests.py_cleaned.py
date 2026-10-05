import unittest
import random
from sorters import QuickSort, BubbleSort, InsertionSort
class SortersTestCase(unittest.TestCase):
    def setUp(self):
        self.expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.non_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.non_sorted)
        print(f"Setting things up... Expected: {self.expected} Non-Sorted: {self.non_sorted}")
    def test_bubble_sorting(self):
        sorter = BubbleSort()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted) - 1)
        self.assertEqual(self.expected, self.non_sorted)
    def test_insertion_sorting(self):
        sorter = InsertionSort()
        sorter.sort(self.non_sorted)
        self.assertEqual(self.expected, self.non_sorted)
    def test_quick_sorting(self):
        sorter = QuickSort()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted) - 1)
        self.assertEqual(self.expected, self.non_sorted)
    def test_fake(self):
        print()
        self.assertEqual("foo", 1)
if __name__ == '__main__':
    unittest.main()
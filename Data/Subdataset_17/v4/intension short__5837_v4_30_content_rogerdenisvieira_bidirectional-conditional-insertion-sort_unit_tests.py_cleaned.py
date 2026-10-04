import unittest
from sorters import QS, BCIS, IS
import random
class SortersTestCase(unittest.TestCase):
    def setUp(self):
        self.expected = list(range(10))
        self.non_sorted = self.expected.copy()
        random.shuffle(self.non_sorted)
        print(f"Setting things up... Expected: {self.expected} Non-Sorted: {self.non_sorted}")
    def test_bcis_sorting(self):
        sorter = BCIS()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted) - 1)
        self.assertEqual(self.expected, self.non_sorted)
    def test_is_sorting(self):
        sorter = IS()
        sorter.sort(self.non_sorted)
        self.assertEqual(self.expected, self.non_sorted)
    def test_qs_sorting(self):
        sorter = QS()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted) - 1)
        self.assertEqual(self.expected, self.non_sorted)
    def test_fake(self):
        print("This test is expected to fail.")
        self.assertEqual("foo", 1)
if __name__ == '__main__':
    unittest.main()
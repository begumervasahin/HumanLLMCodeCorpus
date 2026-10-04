import unittest
from sorters import QS, BCIS, IS
import random
class SortersTestCase(unittest.TestCase):
    def setUp(self):
        self.expected = list(range(10))
        self.non_sorted = self.expected.copy()
        random.shuffle(self.non_sorted)
        print(f"Setup complete. Expected: {self.expected}, Non-Sorted: {self.non_sorted}")
    def test_bcis_sorting(self):
        sorter = BCIS()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted) - 1)
        self.assertEqual(self.expected, self.non_sorted, "BCIS failed to sort correctly.")
    def test_is_sorting(self):
        sorter = IS()
        sorter.sort(self.non_sorted)
        self.assertEqual(self.expected, self.non_sorted, "IS failed to sort correctly.")
    def test_qs_sorting(self):
        sorter = QS()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted) - 1)
        self.assertEqual(self.expected, self.non_sorted, "QS failed to sort correctly.")
    def test_fake(self):
        print("Running a test designed to fail.")
        self.assertEqual("foo", 1, "This test is expected to fail.")
if __name__ == '__main__':
    unittest.main()
class BinarySearch:
    def __init__(self, length, step):
        self.length = length
        self.step = step
    def __getitem__(self, index):
        return (index + 1) * self.step
    def search(self, target):
        count = 0
        left, right = 0, self.length - 1
        while left <= right:
            count += 1
            mid = (left + right)
            mid_val = self[mid]
            if mid_val == target:
                return {'count': count, 'index': mid}
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return {'count': count, 'index': -1}
import unittest
class BinarySearchTest(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list_search(self):
        search = self.one_to_twenty.search(16)
        self.assertGreater(
            search['count'],
            5,
            msg='should return {count: 4, index: 15} for 16'
        )
        self.assertEqual(
            search['index'],
            15,
            msg='should return {count: 4, index: 15} for 16'
        )
    def test_medium_list_search(self):
        pass
    def test_large_list_search(self):
        pass
class ListComprehensionTest(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list(self):
        pass
    def test_medium_list(self):
        pass
    def test_large_list(self):
        pass
if __name__ == '__main__':
    unittest.main()
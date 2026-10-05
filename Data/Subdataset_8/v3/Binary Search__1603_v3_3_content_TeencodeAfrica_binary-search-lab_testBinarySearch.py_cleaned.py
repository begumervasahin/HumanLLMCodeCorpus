class BinarySearch:
    def __init__(self, size, start):
        self.length = size
        self.data = [start + i for i in range(size)]
    def search(self, item):
        low = 0
        high = self.length - 1
        count = 0
        while low <= high:
            mid = (low + high)
            guess = self.data[mid]
            count += 1
            if guess == item:
                return {'count': count, 'index': mid}
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return {'count': count, 'index': -1}
import unittest
class BinarySearchTest(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list_search(self):
        search_result = self.one_to_twenty.search(16)
        self.assertLessEqual(search_result['count'], 5, msg='Expected at most 5 iterations for search')
        self.assertEqual(search_result['index'], 15, msg='Expected index 15 for item 16')
    def test_medium_list_search(self):
        search1 = self.two_to_forty.search(16)
        search2 = self.two_to_forty.search(40)
        search3 = self.two_to_forty.search(33)
        self.assertLessEqual(search1['count'], 5, msg='Expected at most 5 iterations for search 16')
        self.assertEqual(search1['index'], 7, msg='Expected index 7 for item 16')
        self.assertEqual(search2['count'], 0, msg='Expected 0 iterations for search 40')
        self.assertEqual(search2['index'], 19, msg='Expected index 19 for item 40')
        self.assertLessEqual(search3['count'], 4, msg='Expected at most 4 iterations for search 33')
        self.assertEqual(search3['index'], -1, msg='Expected index -1 for item 33')
    def test_large_list_search(self):
        search1 = self.ten_to_thousand.search(40)
        search2 = self.ten_to_thousand.search(880)
        search3 = self.ten_to_thousand.search(10000)
        self.assertLessEqual(search1['count'], 7, msg='Expected at most 7 iterations for search 40')
        self.assertEqual(search1['index'], 3, msg='Expected index 3 for item 40')
        self.assertLessEqual(search2['count'], 4, msg='Expected at most 4 iterations for search 880')
        self.assertEqual(search2['index'], 87, msg='Expected index 87 for item 880')
        self.assertGreater(search3['count'], 7, msg='Expected more than 7 iterations for search 10000')
        self.assertEqual(search3['index'], -1, msg='Expected index -1 for item 10000')
if __name__ == "__main__":
    unittest.main()
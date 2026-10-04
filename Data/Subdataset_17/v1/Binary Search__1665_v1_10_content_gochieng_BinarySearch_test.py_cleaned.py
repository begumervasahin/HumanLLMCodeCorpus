class BinarySearch:
    def __init__(self, length, interval):
        self.length = length
        self.array = [i * interval + interval for i in range(length)]
    def __getitem__(self, index):
        return self.array[index]
    def __len__(self):
        return len(self.array)
    def search(self, value):
        low = 0
        high = self.length - 1
        count = 0
        while low <= high:
            count += 1
            mid = (low + high)
            mid_value = self.array[mid]
            if mid_value == value:
                return {'count': count, 'index': mid}
            elif mid_value < value:
                low = mid + 1
            else:
                high = mid - 1
        return {'count': count, 'index': -1}
import unittest
class ListComprehensionTest(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list(self):
        self.assertListEqual(
            [1, 20, 20],
            [
                self.one_to_twenty[0],
                self.one_to_twenty[19],
                self.one_to_twenty.length
            ],
            msg='should create an array from 1 to 20, with intervals of 1'
        )
        for index in range(self.one_to_twenty.length):
            if index < self.one_to_twenty.length - 1:
                self.assertEqual(
                    1,
                    self.one_to_twenty[index + 1] - self.one_to_twenty[index],
                    msg='should return 1 for consecutive numbers'
                )
    def test_medium_list(self):
        self.assertListEqual(
            [2, 40, 20],
            [
                self.two_to_forty[0],
                self.two_to_forty[19],
                self.two_to_forty.length
            ],
            msg='should create an array from 2 to 40, with intervals of 2'
        )
        for index in range(self.two_to_forty.length):
            if index < self.two_to_forty.length - 1:
                self.assertEqual(
                    2,
                    self.two_to_forty[index + 1] - self.two_to_forty[index],
                    msg='should return 2 for consecutive numbers'
                )
    def test_large_list(self):
        self.assertListEqual(
            [10, 1000, 100],
            [
                self.ten_to_thousand[0],
                self.ten_to_thousand[99],
                self.ten_to_thousand.length
            ],
            msg='should create an array from 10 to 1000, with intervals of 10'
        )
        for index in range(self.ten_to_thousand.length):
            if index < self.ten_to_thousand.length - 1:
                self.assertEqual(
                    10,
                    self.ten_to_thousand[index + 1] - self.ten_to_thousand[index],
                    msg='should return 10 for consecutive numbers'
                )
class BinarySearchTest(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list_search(self):
        search = self.one_to_twenty.search(16)
        self.assertGreater(
            5,
            search['count'],
            msg='should return {count: 4, index: 15} for 16'
        )
        self.assertEqual(
            15,
            search['index'],
            msg='should return {count: 4, index: 15} for 16'
        )
    def test_medium_list_search(self):
        search1 = self.two_to_forty.search(16)
        search2 = self.two_to_forty.search(40)
        search3 = self.two_to_forty.search(33)
        self.assertGreater(
            5,
            search1['count'],
            msg='should return {count: 4, index: 7} for 16'
        )
        self.assertEqual(
            7,
            search1['index'],
            msg='should return {count: 4, index: 7} for 16'
        )
        self.assertEqual(
            0,
            search2['count'],
            msg='should return {count: 0, index: 19} for 40'
        )
        self.assertEqual(
            19,
            search2['index'],
            msg='should return {count: 0, index: 19} for 40'
        )
        self.assertGreater(
            4,
            search3['count'],
            msg='should return {count: 3, index: -1} for 33'
        )
        self.assertEqual(
            -1,
            search3['index'],
            msg='should return {count: 3, index: -1} for 33'
        )
    def test_large_list_search(self):
        search1 = self.ten_to_thousand.search(40)
        search2 = self.ten_to_thousand.search(880)
        search3 = self.ten_to_thousand.search(10000)
        self.assertGreater(
            7,
            search1['count'],
            msg='should return {count: 3, index: 3} for 40'
        )
        self.assertEqual(
            3,
            search1['index'],
            msg='should return {count: 3, index: 3} for 40'
        )
        self.assertGreater(
            4,
            search2['count'],
            msg='should return {count: 5, index: 87} for 880'
        )
        self.assertEqual(
            87,
            search2['index'],
            msg='should return {count: 5, index: 87} for 880'
        )
        self.assertGreater(
            7,
            search3['count'],
            msg='should return {count: 3, index: -1} for 10000'
        )
        self.assertEqual(
            -1,
            search3['index'],
            msg='should return {count: 3, index: -1} for 10000'
        )
if __name__ == '__main__':
    unittest.main()
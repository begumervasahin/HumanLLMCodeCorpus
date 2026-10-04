class BinarySearch:
    def __init__(self, length, interval):
        self.length = length
        self.array = [i * interval + interval for i in range(length)]
    def __getitem__(self, index):
        return self.array[index]
    def __len__(self):
        return len(self.array)
    def search(self, value):
        low, high = 0, self.length - 1
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
class BinarySearchArrayTest(unittest.TestCase):
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
            msg='Array should be created from 1 to 20 with an interval of 1'
        )
        for index in range(self.one_to_twenty.length - 1):
            self.assertEqual(
                1,
                self.one_to_twenty[index + 1] - self.one_to_twenty[index],
                msg='Consecutive numbers should have an interval of 1'
            )
    def test_medium_list(self):
        self.assertListEqual(
            [2, 40, 20],
            [
                self.two_to_forty[0],
                self.two_to_forty[19],
                self.two_to_forty.length
            ],
            msg='Array should be created from 2 to 40 with an interval of 2'
        )
        for index in range(self.two_to_forty.length - 1):
            self.assertEqual(
                2,
                self.two_to_forty[index + 1] - self.two_to_forty[index],
                msg='Consecutive numbers should have an interval of 2'
            )
    def test_large_list(self):
        self.assertListEqual(
            [10, 1000, 100],
            [
                self.ten_to_thousand[0],
                self.ten_to_thousand[99],
                self.ten_to_thousand.length
            ],
            msg='Array should be created from 10 to 1000 with an interval of 10'
        )
        for index in range(self.ten_to_thousand.length - 1):
            self.assertEqual(
                10,
                self.ten_to_thousand[index + 1] - self.ten_to_thousand[index],
                msg='Consecutive numbers should have an interval of 10'
            )
class BinarySearchAlgorithmTest(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list_search(self):
        search = self.one_to_twenty.search(16)
        self.assertLessEqual(
            search['count'], 5,
            msg='Binary search should find 16 with at most 4 comparisons'
        )
        self.assertEqual(
            15,
            search['index'],
            msg='Index of 16 should be 15'
        )
    def test_medium_list_search(self):
        search_16 = self.two_to_forty.search(16)
        search_40 = self.two_to_forty.search(40)
        search_33 = self.two_to_forty.search(33)
        self.assertLessEqual(
            search_16['count'], 5,
            msg='Binary search should find 16 with at most 4 comparisons'
        )
        self.assertEqual(
            7,
            search_16['index'],
            msg='Index of 16 should be 7'
        )
        self.assertEqual(
            0,
            search_40['count'],
            msg='Binary search should find 40 with 0 additional comparisons'
        )
        self.assertEqual(
            19,
            search_40['index'],
            msg='Index of 40 should be 19'
        )
        self.assertLessEqual(
            search_33['count'], 4,
            msg='Binary search should determine 33 is not in the list with at most 3 comparisons'
        )
        self.assertEqual(
            -1,
            search_33['index'],
            msg='Search for 33 should return -1 as it is not in the list'
        )
    def test_large_list_search(self):
        search_40 = self.ten_to_thousand.search(40)
        search_880 = self.ten_to_thousand.search(880)
        search_10000 = self.ten_to_thousand.search(10000)
        self.assertLessEqual(
            search_40['count'], 7,
            msg='Binary search should find 40 with at most 3 comparisons'
        )
        self.assertEqual(
            3,
            search_40['index'],
            msg='Index of 40 should be 3'
        )
        self.assertLessEqual(
            search_880['count'], 4,
            msg='Binary search should find 880 with at most 5 comparisons'
        )
        self.assertEqual(
            87,
            search_880['index'],
            msg='Index of 880 should be 87'
        )
        self.assertLessEqual(
            search_10000['count'], 7,
            msg='Binary search should determine 10000 is not in the list with at most 3 comparisons'
        )
        self.assertEqual(
            -1,
            search_10000['index'],
            msg='Search for 10000 should return -1 as it is not in the list'
        )
if __name__ == '__main__':
    unittest.main()
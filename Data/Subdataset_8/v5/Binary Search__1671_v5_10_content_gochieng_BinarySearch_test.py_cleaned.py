import unittest
from binarysearch import BinarySearch
class ListComprehensionTest(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list(self):
        expected_result = [1, 20, 20]
        actual_result = [
            self.one_to_twenty[0],
            self.one_to_twenty[19],
            self.one_to_twenty.length
        ]
        self.assertListEqual(
            expected_result,
            actual_result,
            msg='should create an array from 1 to 20, with intervals of 1'
        )
        for index, number in enumerate(self.one_to_twenty):
            if index < self.one_to_twenty.length - 1:
                self.assertEqual(
                    1,
                    self.one_to_twenty[index + 1] - self.one_to_twenty[index],
                    msg='should return 1 for consecutive numbers'
                )
    def test_medium_list(self):
        expected_result = [2, 40, 20]
        actual_result = [
            self.two_to_forty[0],
            self.two_to_forty[19],
            self.two_to_forty.length
        ]
        self.assertListEqual(
            expected_result,
            actual_result,
            msg='should create an array from 2 to 40, with intervals of 2'
        )
        for index, number in enumerate(self.two_to_forty):
            if index < self.two_to_forty.length - 1:
                self.assertEqual(
                    2,
                    self.two_to_forty[index + 1] - self.two_to_forty[index],
                    msg='should return 2 for consecutive numbers'
                )
    def test_large_list(self):
        expected_result = [10, 1000, 100]
        actual_result = [
            self.ten_to_thousand[0],
            self.ten_to_thousand[99],
            self.ten_to_thousand.length
        ]
        self.assertListEqual(
            expected_result,
            actual_result,
            msg='should create an array from 10 to 1000, with intervals of 10'
        )
        for index, number in enumerate(self.ten_to_thousand):
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
if __name__ == '__main__':
    unittest.main()
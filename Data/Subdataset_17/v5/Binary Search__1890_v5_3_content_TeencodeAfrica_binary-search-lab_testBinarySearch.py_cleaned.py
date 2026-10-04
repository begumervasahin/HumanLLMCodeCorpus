import unittest
from binarySearch import binarySearch
class TestBinarySearchArrayCreation(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = binarySearch(20, 1)
        self.two_to_forty = binarySearch(20, 2)
        self.ten_to_thousand = binarySearch(100, 10)
    def test_small_list_creation(self):
        expected_values = [1, 20, 20]
        actual_values = [
            self.one_to_twenty[0],
            self.one_to_twenty[19],
            len(self.one_to_twenty)
        ]
        self.assertListEqual(
            expected_values,
            actual_values,
            msg='Should create an array from 1 to 20 with intervals of 1'
        )
        for index in range(len(self.one_to_twenty) - 1):
            self.assertEqual(
                self.one_to_twenty[index + 1] - self.one_to_twenty[index],
                1,
                msg='Each consecutive number should have an interval of 1'
            )
    def test_medium_list_creation(self):
        expected_values = [2, 40, 20]
        actual_values = [
            self.two_to_forty[0],
            self.two_to_forty[19],
            len(self.two_to_forty)
        ]
        self.assertListEqual(
            expected_values,
            actual_values,
            msg='Should create an array from 2 to 40 with intervals of 2'
        )
        for index in range(len(self.two_to_forty) - 1):
            self.assertEqual(
                self.two_to_forty[index + 1] - self.two_to_forty[index],
                2,
                msg='Each consecutive number should have an interval of 2'
            )
    def test_large_list_creation(self):
        expected_values = [10, 1000, 100]
        actual_values = [
            self.ten_to_thousand[0],
            self.ten_to_thousand[99],
            len(self.ten_to_thousand)
        ]
        self.assertListEqual(
            expected_values,
            actual_values,
            msg='Should create an array from 10 to 1000 with intervals of 10'
        )
        for index in range(len(self.ten_to_thousand) - 1):
            self.assertEqual(
                self.ten_to_thousand[index + 1] - self.ten_to_thousand[index],
                10,
                msg='Each consecutive number should have an interval of 10'
            )
class TestBinarySearchFunctionality(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = binarySearch(20, 1)
        self.two_to_forty = binarySearch(20, 2)
        self.ten_to_thousand = binarySearch(100, 10)
    def test_search_in_small_list(self):
        result = self.one_to_twenty.search(16)
        self.assertEqual(result['count'], 5, msg='Should take 5 iterations to find 16')
        self.assertEqual(result['index'], 15, msg='Should return index 15 for 16')
    def test_search_in_medium_list(self):
        result_16 = self.two_to_forty.search(16)
        result_40 = self.two_to_forty.search(40)
        result_33 = self.two_to_forty.search(33)
        self.assertEqual(result_16['count'], 5, msg='Should take 5 iterations to find 16')
        self.assertEqual(result_16['index'], 7, msg='Should return index 7 for 16')
        self.assertEqual(result_40['count'], 1, msg='Should take 1 iteration to find 40')
        self.assertEqual(result_40['index'], 19, msg='Should return index 19 for 40')
        self.assertEqual(result_33['count'], 5, msg='Should take 5 iterations to determine 33 is not in the list')
        self.assertEqual(result_33['index'], -1, msg='Should return index -1 for a value not found (33)')
    def test_search_in_large_list(self):
        result_40 = self.ten_to_thousand.search(40)
        result_880 = self.ten_to_thousand.search(880)
        result_10000 = self.ten_to_thousand.search(10000)
        self.assertEqual(result_40['count'], 3, msg='Should take 3 iterations to find 40')
        self.assertEqual(result_40['index'], 3, msg='Should return index 3 for 40')
        self.assertEqual(result_880['count'], 5, msg='Should take 5 iterations to find 880')
        self.assertEqual(result_880['index'], 87, msg='Should return index 87 for 880')
        self.assertEqual(result_10000['count'], 8, msg='Should take 8 iterations to determine 10000 is not in the list')
        self.assertEqual(result_10000['index'], -1, msg='Should return index -1 for a value not found (10000)')
if __name__ == "__main__":
    unittest.main(exit=False)
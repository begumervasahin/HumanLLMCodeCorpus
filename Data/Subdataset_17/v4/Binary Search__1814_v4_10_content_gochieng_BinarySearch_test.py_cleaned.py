import unittest
from binarysearch import BinarySearch
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
            msg='The list should be correctly generated from 1 to 20 with an interval of 1.'
        )
        for index in range(self.one_to_twenty.length - 1):
            self.assertEqual(
                1,
                self.one_to_twenty[index + 1] - self.one_to_twenty[index],
                msg='Each consecutive element should have a difference of 1.'
            )
    def test_medium_list(self):
        self.assertListEqual(
            [2, 40, 20],
            [
                self.two_to_forty[0],
                self.two_to_forty[19],
                self.two_to_forty.length
            ],
            msg='The list should be correctly generated from 2 to 40 with an interval of 2.'
        )
        for index in range(self.two_to_forty.length - 1):
            self.assertEqual(
                2,
                self.two_to_forty[index + 1] - self.two_to_forty[index],
                msg='Each consecutive element should have a difference of 2.'
            )
    def test_large_list(self):
        self.assertListEqual(
            [10, 1000, 100],
            [
                self.ten_to_thousand[0],
                self.ten_to_thousand[99],
                self.ten_to_thousand.length
            ],
            msg='The list should be correctly generated from 10 to 1000 with an interval of 10.'
        )
        for index in range(self.ten_to_thousand.length - 1):
            self.assertEqual(
                10,
                self.ten_to_thousand[index + 1] - self.ten_to_thousand[index],
                msg='Each consecutive element should have a difference of 10.'
            )
class BinarySearchTest(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list_search(self):
        search_result = self.one_to_twenty.search(16)
        self.assertGreater(
            5,
            search_result['count'],
            msg='The search for 16 should take fewer than 5 steps.'
        )
        self.assertEqual(
            15,
            search_result['index'],
            msg='The index of 16 should be 15.'
        )
    def test_medium_list_search(self):
        search_result_1 = self.two_to_forty.search(16)
        search_result_2 = self.two_to_forty.search(40)
        search_result_3 = self.two_to_forty.search(33)
        self.assertGreater(
            5,
            search_result_1['count'],
            msg='The search for 16 should take fewer than 5 steps.'
        )
        self.assertEqual(
            7,
            search_result_1['index'],
            msg='The index of 16 should be 7.'
        )
        self.assertEqual(
            0,
            search_result_2['count'],
            msg='The search for 40 should take 0 steps.'
        )
        self.assertEqual(
            19,
            search_result_2['index'],
            msg='The index of 40 should be 19.'
        )
        self.assertGreater(
            4,
            search_result_3['count'],
            msg='The search for 33 should take fewer than 4 steps.'
        )
        self.assertEqual(
            -1,
            search_result_3['index'],
            msg='33 is not in the list, so the index should be -1.'
        )
    def test_large_list_search(self):
        search_result_1 = self.ten_to_thousand.search(40)
        search_result_2 = self.ten_to_thousand.search(880)
        search_result_3 = self.ten_to_thousand.search(10000)
        self.assertGreater(
            7,
            search_result_1['count'],
            msg='The search for 40 should take fewer than 7 steps.'
        )
        self.assertEqual(
            3,
            search_result_1['index'],
            msg='The index of 40 should be 3.'
        )
        self.assertGreater(
            4,
            search_result_2['count'],
            msg='The search for 880 should take fewer than 4 steps.'
        )
        self.assertEqual(
            87,
            search_result_2['index'],
            msg='The index of 880 should be 87.'
        )
        self.assertGreater(
            7,
            search_result_3['count'],
            msg='The search for 10000 should take fewer than 7 steps.'
        )
        self.assertEqual(
            -1,
            search_result_3['index'],
            msg='10000 is not in the list, so the index should be -1.'
        )
if __name__ == '__main__':
    unittest.main()
class BinarySearch:
    def __init__(self, length, interval):
        self.length = length
        self.array = [(i * interval) + interval for i in range(length)]
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
class TestBinarySearchArrayCreation(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list(self):
        self.assertEqual(self.one_to_twenty[0], 1)
        self.assertEqual(self.one_to_twenty[19], 20)
        self.assertEqual(len(self.one_to_twenty), 20)
        for index in range(len(self.one_to_twenty) - 1):
            self.assertEqual(
                self.one_to_twenty[index + 1] - self.one_to_twenty[index],
                1,
                msg='Each consecutive number should have an interval of 1'
            )
    def test_medium_list(self):
        self.assertEqual(self.two_to_forty[0], 2)
        self.assertEqual(self.two_to_forty[19], 40)
        self.assertEqual(len(self.two_to_forty), 20)
        for index in range(len(self.two_to_forty) - 1):
            self.assertEqual(
                self.two_to_forty[index + 1] - self.two_to_forty[index],
                2,
                msg='Each consecutive number should have an interval of 2'
            )
    def test_large_list(self):
        self.assertEqual(self.ten_to_thousand[0], 10)
        self.assertEqual(self.ten_to_thousand[99], 1000)
        self.assertEqual(len(self.ten_to_thousand), 100)
        for index in range(len(self.ten_to_thousand) - 1):
            self.assertEqual(
                self.ten_to_thousand[index + 1] - self.ten_to_thousand[index],
                10,
                msg='Each consecutive number should have an interval of 10'
            )
class TestBinarySearchFunctionality(unittest.TestCase):
    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)
    def test_small_list_search(self):
        result = self.one_to_twenty.search(16)
        self.assertEqual(result['count'], 5)
        self.assertEqual(result['index'], 15)
    def test_medium_list_search(self):
        result_16 = self.two_to_forty.search(16)
        result_40 = self.two_to_forty.search(40)
        result_33 = self.two_to_forty.search(33)
        self.assertEqual(result_16['count'], 5)
        self.assertEqual(result_16['index'], 7)
        self.assertEqual(result_40['count'], 1)
        self.assertEqual(result_40['index'], 19)
        self.assertEqual(result_33['count'], 5)
        self.assertEqual(result_33['index'], -1)
    def test_large_list_search(self):
        result_40 = self.ten_to_thousand.search(40)
        result_880 = self.ten_to_thousand.search(880)
        result_10000 = self.ten_to_thousand.search(10000)
        self.assertEqual(result_40['count'], 3)
        self.assertEqual(result_40['index'], 3)
        self.assertEqual(result_880['count'], 5)
        self.assertEqual(result_880['index'], 87)
        self.assertEqual(result_10000['count'], 8)
        self.assertEqual(result_10000['index'], -1)
if __name__ == "__main__":
    unittest.main()
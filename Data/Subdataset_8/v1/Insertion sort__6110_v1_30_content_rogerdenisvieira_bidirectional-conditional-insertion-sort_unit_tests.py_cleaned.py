import unittest
import random
class QS:
    def sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.sort(arr, low, pi - 1)
            self.sort(arr, pi + 1, high)
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
class BCIS:
    def sort(self, arr, l, r):
        if l < r:
            pi = self.partition(arr, l, r)
            self.sort(arr, l, pi - 1)
            self.sort(arr, pi + 1, r)
    def partition(self, arr, l, r):
        x = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i
class IS:
    def sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
class SortersTestCase(unittest.TestCase):
    def setUp(self):
        self.expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.non_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.non_sorted)
        print("Setting things up... Expected: {0} Non-Sorted: {1}".format(self.expected, self.non_sorted))
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
    def atest_fake(self):
        print()
        self.assertEqual("foo", 1)
if __name__ == '__main__':
    unittest.main()
import unittest
import random
class QuickSort:
    def sort(self, arr, low, high):
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self.sort(arr, low, pivot_index - 1)
            self.sort(arr, pivot_index + 1, high)
    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
class BinaryCascadeInsertionSort:
    def sort(self, arr, low, high):
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self.sort(arr, low, pivot_index - 1)
            self.sort(arr, pivot_index + 1, high)
    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
class InsertionSort:
    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
class SortersTestCase(unittest.TestCase):
    def setUp(self):
        self.expected = list(range(10))
        self.non_sorted = self.expected[:]
        random.shuffle(self.non_sorted)
        print(f"Setup complete. Expected: {self.expected}, Non-Sorted: {self.non_sorted}")
    def test_quick_sort(self):
        sorter = QuickSort()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted) - 1)
        self.assertEqual(self.expected, self.non_sorted)
    def test_binary_cascade_insertion_sort(self):
        sorter = BinaryCascadeInsertionSort()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted) - 1)
        self.assertEqual(self.expected, self.non_sorted)
    def test_insertion_sort(self):
        sorter = InsertionSort()
        sorter.sort(self.non_sorted)
        self.assertEqual(self.expected, self.non_sorted)
    def test_intentional_failure(self):
        self.assertEqual("foo", 1)
if __name__ == '__main__':
    unittest.main()
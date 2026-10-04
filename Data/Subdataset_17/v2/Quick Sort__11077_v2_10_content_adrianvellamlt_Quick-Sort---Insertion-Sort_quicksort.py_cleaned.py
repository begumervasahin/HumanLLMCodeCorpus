import insertionsort as ins
class QuickSort:
    def get_median_of_three_index(self, array, start, end):
        def switch(index):
            nonlocal median_index
            return {
                0: start,
                1: median_index,
                2: end - 1
            }[index]
        def get_median_index(start, length):
            return start + length
        def median(i, j, k):
            return j if i < j < k or k < j < i else k if i < k < j or j < k < i else i
        median_index = get_median_index(start, end - start)
        return median(switch(0), switch(1), switch(2))
    def partition(self, array, start, end, is_median_of_three):
        median_index = self.get_median_of_three_index(array, start, end) if is_median_of_three else start
        pivot = array[median_index]
        array[median_index], array[start] = array[start], pivot
        i = start + 1
        for j in range(start + 1, end):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[start], array[i - 1] = array[i - 1], array[start]
        return i - 1
    def sort(self, arr, is_median_of_three):
        stack = [0, len(arr)]
        while stack:
            end = stack.pop()
            start = stack.pop()
            if end - start < 2:
                continue
            p = self.partition(arr, start, end, is_median_of_three)
            stack.extend([p + 1, end, start, p])
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        self.sort(arr, False)
        return arr
    def sort_median_of_three(self, arr):
        if len(arr) <= 1:
            return arr
        self.sort(arr, True)
        return arr
    def optimised_sort(self, arr):
        if len(arr) > 16:
            return self.sort_median_of_three(arr)
        return ins.InsertionSort().sort(arr)
if __name__ == "__main__":
    array = [33, 10, 55, 71, 29, 14, 37, 93, 52, 65]
    sorter = QuickSort()
    print("Quick Sort:", sorter.quick_sort(array[:]))
    print("Quick Sort with Median of Three:", sorter.sort_median_of_three(array[:]))
    print("Optimised Sort:", sorter.optimised_sort(array[:]))
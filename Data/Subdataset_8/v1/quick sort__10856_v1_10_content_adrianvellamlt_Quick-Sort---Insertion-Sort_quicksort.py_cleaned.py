import insertionsort as ins
class QuickSort(object):
    def GetMedianOfThreeIndex(self, array, start, end):
        def Switch(index):
            nonlocal medianIndex
            return {
                0: start,
                1: medianIndex,
                2: end - 1
            }[index]
        def GetMedianIndex(start, length):
            if length % 2 == 0:
                return start + length
            else:
                return start + length
        def Median(i, j, k):
            if i < j:
                return j if j < k else k
            else:
                return i if i < k else k
        medianIndex = GetMedianIndex(start, end - start)
        return Median(array[start], array[end - 1], array[medianIndex])
    def Partition(self, array, start, end, isMedianOfThree):
        medianIndex = self.GetMedianOfThreeIndex(array, start, end) if isMedianOfThree else start
        pivot = array[medianIndex]
        array[medianIndex], array[start] = array[start], pivot
        i = start + 1
        for j in range(start + 1, end):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[start], array[i - 1] = array[i - 1], array[start]
        return i - 1
    def Sort(self, arr, isMedianOfThree):
        stack = []
        stack.append(0)
        stack.append(len(arr))
        while len(stack) > 0:
            end = stack.pop()
            start = stack.pop()
            if end - start < 2:
                continue
            p = self.Partition(arr, start, end, isMedianOfThree)
            stack.append(p + 1)
            stack.append(end)
            stack.append(start)
            stack.append(p)
    def QuickSort(self, arr):
        if len(arr) <= 1:
            return arr
        self.Sort(arr, False)
        return arr
    def SortMedianOfThree(self, arr):
        if len(arr) <= 1:
            return arr
        self.Sort(arr, True)
        return arr
    def OptimisedSort(self, arr):
        if len(arr) > 16:
            return self.SortMedianOfThree(arr)
        return ins.InsertionSort().Sort(arr)
if __name__ == "__main__":
    qs = QuickSort()
    arr = [3, 6, 8, 10, 1, 2, 1, 5, 9, 4, 7]
    print("Original array:", arr)
    sorted_arr = qs.QuickSort(arr.copy())
    print("QuickSort:", sorted_arr)
    sorted_arr_median = qs.SortMedianOfThree(arr.copy())
    print("QuickSort with Median of Three:", sorted_arr_median)
    sorted_arr_optimised = qs.OptimisedSort(arr.copy())
    print("OptimisedSort:", sorted_arr_optimised)
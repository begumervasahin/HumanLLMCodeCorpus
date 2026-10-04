import random
import datetime
import xlwt
class Sorts:
    def __init__(self):
        wb = xlwt.Workbook()
        style0 = xlwt.easyxf('font: name Arial, color-index black')
        minNum = 0
        maxNum = 1000
        maxNsquaredSize = 10000
        maxSize = 10000000
        size = 10
        increment = "0"
        programBegin = datetime.datetime.now()
        while size <= maxSize:
            iterationBegin = datetime.datetime.now()
            print("iteration:", size)
            ws = wb.add_sheet(str(size))
            if size <= maxNsquaredSize:
                ws.write(0, 0, "Bubble sort")
                ws.write(0, 1, "Insertion sort")
            ws.write(0, 2, "Quick sort")
            ws.write(0, 3, "Heap sort")
            ws.write(0, 4, "Merge sort")
            ws.write(0, 5, "Radix sort")
            for i in range(1, 6):
                array = self.generate_random_array(size, minNum, maxNum)
                if size <= maxNsquaredSize:
                    time = self.bubble_sort(array)
                    ws.write(i, 0, time, style0)
                    time = self.insertion_sort(array)
                    ws.write(i, 1, time, style0)
                time = self.quick_sort(array)
                ws.write(i, 2, time, style0)
                time = self.heap_sort(array)
                ws.write(i, 3, time, style0)
                time = self.merge_sort(array)
                ws.write(i, 4, time, style0)
                time = self.radix_sort(array)
                ws.write(i, 5, time, style0)
            increment = self.increment_array(increment)
            size += int(increment)
            wb.save('Data.xls')
            print("Time taken for iteration:", datetime.datetime.now() - iterationBegin)
            print()
        print("Time taken overall:", datetime.datetime.now() - programBegin)
    def bubble_sort(self, array):
        a = array[:]
        startTime = datetime.datetime.now()
        length = len(a)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if a[j + 1] < a[j]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return self.get_milliseconds(startTime)
    def insertion_sort(self, array):
        a = array[:]
        startTime = datetime.datetime.now()
        length = len(a)
        for i in range(1, length):
            temp = a[i]
            j = i
            while j > 0 and temp < a[j - 1]:
                a[j] = a[j - 1]
                j -= 1
            a[j] = temp
        return self.get_milliseconds(startTime)
    def radix_sort(self, array):
        a = array[:]
        startTime = datetime.datetime.now()
        bucketCount = 10
        largest = max(a)
        largestDigit = len(str(largest))
        for digit in range(1, largestDigit + 1):
            buckets = [[] for _ in range(bucketCount)]
            division = 10 ** (digit - 1)
            for element in a:
                currentDigit = (element
                buckets[currentDigit].append(element)
            i = 0
            for bucket in buckets:
                for element in bucket:
                    a[i] = element
                    i += 1
        return self.get_milliseconds(startTime)
    def quick_sort(self, array):
        a = array[:]
        startTime = datetime.datetime.now()
        self._quick_sort(a)
        return self.get_milliseconds(startTime)
    def _quick_sort(self, a):
        if len(a) <= 1:
            return a
        less = []
        more = []
        pivotList = []
        pivot = a[0]
        for element in a:
            if element < pivot:
                less.append(element)
            elif element > pivot:
                more.append(element)
            else:
                pivotList.append(element)
        return self._quick_sort(less) + pivotList + self._quick_sort(more)
    def merge_sort(self, array):
        a = array[:]
        startTime = datetime.datetime.now()
        self._merge_sort(a)
        return self.get_milliseconds(startTime)
    def _merge_sort(self, a):
        if len(a) > 1:
            mid = len(a)
            left = a[:mid]
            right = a[mid:]
            self._merge_sort(left)
            self._merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                a[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                a[k] = right[j]
                j += 1
                k += 1
    def heap_sort(self, array):
        a = array[:]
        startTime = datetime.datetime.now()
        length = len(a)
        self.heapify(a, length)
        end = length - 1
        while end > 0:
            a[end], a[0] = a[0], a[end]
            end -= 1
            self.sift_down(a, 0, end)
        return self.get_milliseconds(startTime)
    def heapify(self, a, length):
        start = (length - 2)
        while start >= 0:
            self.sift_down(a, start, length - 1)
            start -= 1
    def sift_down(self, a, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and a[child + 1] > a[child]:
                child += 1
            if a[child] > a[root]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                return
    def increment_array(self, inc):
        if inc[:1] == "4":
            return "5" + inc[1:]
        if inc[:1] == "5":
            return "4" + inc[1:] + "0"
        if inc[:1] == "0":
            return "40"
    def get_milliseconds(self, startTime):
        c = datetime.datetime.now() - startTime
        milliseconds = (c.days * 24 * 60 * 60 + c.seconds) * 1000 + c.microseconds / 1000.0
        return milliseconds
    def generate_random_array(self, size, minimum, maximum):
        return [random.randint(minimum, maximum) for _ in range(size)]
if __name__ == "__main__":
    s = Sorts()
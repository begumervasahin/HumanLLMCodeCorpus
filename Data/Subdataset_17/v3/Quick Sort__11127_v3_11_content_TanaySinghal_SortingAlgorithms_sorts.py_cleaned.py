import random
import datetime
import xlwt
class Sorts:
    def __init__(self):
        self.wb = xlwt.Workbook()
        self.style0 = xlwt.easyxf('font: name Arial, color-index black')
        self.min_num = 0
        self.max_num = 1000
        self.max_nsquared_size = 10000
        self.max_size = 10000000
        self.size = 10
        self.increment = "0"
        self.program_begin = datetime.datetime.now()
        self.run_sorts()
    def run_sorts(self):
        while self.size <= self.max_size:
            iteration_begin = datetime.datetime.now()
            print(f"Iteration size: {self.size}")
            ws = self.wb.add_sheet(str(self.size))
            headers = ["Bubble Sort", "Insertion Sort", "Quick Sort", "Heap Sort", "Merge Sort", "Radix Sort"]
            for idx, header in enumerate(headers):
                if self.size > self.max_nsquared_size and idx < 2:
                    continue
                ws.write(0, idx, header)
            for i in range(1, 6):
                array = self.generate_random_array(self.size, self.min_num, self.max_num)
                if self.size <= self.max_nsquared_size:
                    ws.write(i, 0, self.time_sort(self.bubble_sort, array), self.style0)
                    ws.write(i, 1, self.time_sort(self.insertion_sort, array), self.style0)
                ws.write(i, 2, self.time_sort(self.quick_sort, array), self.style0)
                ws.write(i, 3, self.time_sort(self.heap_sort, array), self.style0)
                ws.write(i, 4, self.time_sort(self.merge_sort, array), self.style0)
                ws.write(i, 5, self.time_sort(self.radix_sort, array), self.style0)
            self.increment = self.increment_array(self.increment)
            self.size += int(self.increment)
            self.wb.save('Data.xls')
            print(f"Time taken for iteration: {datetime.datetime.now() - iteration_begin}\n")
        print(f"Total time taken: {datetime.datetime.now() - self.program_begin}")
    def bubble_sort(self, array):
        a = array[:]
        length = len(a)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if a[j + 1] < a[j]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a
    def insertion_sort(self, array):
        a = array[:]
        length = len(a)
        for i in range(1, length):
            temp = a[i]
            j = i
            while j > 0 and temp < a[j - 1]:
                a[j] = a[j - 1]
                j -= 1
            a[j] = temp
        return a
    def radix_sort(self, array):
        a = array[:]
        bucket_count = 10
        largest = max(a)
        largest_digit = len(str(largest))
        for digit in range(1, largest_digit + 1):
            buckets = [[] for _ in range(bucket_count)]
            division = 10 ** (digit - 1)
            for element in a:
                current_digit = (element
                buckets[current_digit].append(element)
            i = 0
            for bucket in buckets:
                for element in bucket:
                    a[i] = element
                    i += 1
        return a
    def quick_sort(self, array):
        return self._quick_sort(array[:])
    def _quick_sort(self, a):
        if len(a) <= 1:
            return a
        less, more, pivot_list = [], [], []
        pivot = a[0]
        for element in a:
            if element < pivot:
                less.append(element)
            elif element > pivot:
                more.append(element)
            else:
                pivot_list.append(element)
        return self._quick_sort(less) + pivot_list + self._quick_sort(more)
    def merge_sort(self, array):
        a = array[:]
        self._merge_sort(a)
        return a
    def _merge_sort(self, a):
        if len(a) > 1:
            mid = len(a)
            left, right = a[:mid], a[mid:]
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
        length = len(a)
        self.heapify(a, length)
        end = length - 1
        while end > 0:
            a[end], a[0] = a[0], a[end]
            end -= 1
            self.sift_down(a, 0, end)
        return a
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
        if inc.startswith("4"):
            return "5" + inc[1:]
        if inc.startswith("5"):
            return "4" + inc[1:] + "0"
        if inc.startswith("0"):
            return "40"
    def get_milliseconds(self, start_time):
        delta = datetime.datetime.now() - start_time
        return (delta.days * 24 * 60 * 60 + delta.seconds) * 1000 + delta.microseconds / 1000.0
    def generate_random_array(self, size, minimum, maximum):
        return [random.randint(minimum, maximum) for _ in range(size)]
    def time_sort(self, sort_function, array):
        start_time = datetime.datetime.now()
        sort_function(array)
        return self.get_milliseconds(start_time)
if __name__ == "__main__":
    s = Sorts()
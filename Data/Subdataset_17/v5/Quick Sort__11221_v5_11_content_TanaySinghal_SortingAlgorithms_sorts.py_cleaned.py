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
            print(f"Iteration: {self.size}")
            ws = self.wb.add_sheet(str(self.size))
            self.write_headers(ws)
            self.sort_and_write_results(ws)
            self.increment = self.increment_array(self.increment)
            self.size += int(self.increment)
            self.wb.save('Data.xls')
            print(f"Time taken for iteration: {datetime.datetime.now() - iteration_begin}\n")
        print(f"Total time taken: {datetime.datetime.now() - self.program_begin}")
    def write_headers(self, ws):
        if self.size <= self.max_nsquared_size:
            ws.write(0, 0, "Bubble sort")
            ws.write(0, 1, "Insertion sort")
        ws.write(0, 2, "Quick sort")
        ws.write(0, 3, "Heap sort")
        ws.write(0, 4, "Merge sort")
        ws.write(0, 5, "Radix sort")
    def sort_and_write_results(self, ws):
        for i in range(1, 6):
            array = self.generate_random_array(self.size, self.min_num, self.max_num)
            if self.size <= self.max_nsquared_size:
                ws.write(i, 0, self.bubble_sort(array[:]), self.style0)
                ws.write(i, 1, self.insertion_sort(array[:]), self.style0)
            ws.write(i, 2, self.quick_sort(array[:]), self.style0)
            ws.write(i, 3, self.heap_sort(array[:]), self.style0)
            ws.write(i, 4, self.merge_sort(array[:]), self.style0)
            ws.write(i, 5, self.radix_sort(array[:]), self.style0)
    @staticmethod
    def bubble_sort(array):
        start_time = datetime.datetime.now()
        length = len(array)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if array[j + 1] < array[j]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return Sorts.get_milliseconds(start_time)
    @staticmethod
    def insertion_sort(array):
        start_time = datetime.datetime.now()
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return Sorts.get_milliseconds(start_time)
    @staticmethod
    def radix_sort(array):
        start_time = datetime.datetime.now()
        max_digit = len(str(max(array)))
        for digit in range(max_digit):
            buckets = [[] for _ in range(10)]
            for number in array:
                buckets[(number
            array = [number for bucket in buckets for number in bucket]
        return Sorts.get_milliseconds(start_time)
    @staticmethod
    def quick_sort(array):
        start_time = datetime.datetime.now()
        Sorts._quick_sort(array, 0, len(array) - 1)
        return Sorts.get_milliseconds(start_time)
    @staticmethod
    def _quick_sort(array, low, high):
        if low < high:
            pi = Sorts.partition(array, low, high)
            Sorts._quick_sort(array, low, pi - 1)
            Sorts._quick_sort(array, pi + 1, high)
    @staticmethod
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
    @staticmethod
    def merge_sort(array):
        start_time = datetime.datetime.now()
        Sorts._merge_sort(array)
        return Sorts.get_milliseconds(start_time)
    @staticmethod
    def _merge_sort(array):
        if len(array) > 1:
            mid = len(array)
            left_half = array[:mid]
            right_half = array[mid:]
            Sorts._merge_sort(left_half)
            Sorts._merge_sort(right_half)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1
    @staticmethod
    def heap_sort(array):
        start_time = datetime.datetime.now()
        n = len(array)
        for i in range(n
            Sorts.heapify(array, n, i)
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            Sorts.heapify(array, i, 0)
        return Sorts.get_milliseconds(start_time)
    @staticmethod
    def heapify(array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and array[largest] < array[left]:
            largest = left
        if right < n and array[largest] < array[right]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            Sorts.heapify(array, n, largest)
    @staticmethod
    def increment_array(inc):
        if inc[:1] == "4":
            return "5" + inc[1:]
        if inc[:1] == "5":
            return "4" + inc[1:] + "0"
        if inc[:1] == "0":
            return "40"
    @staticmethod
    def get_milliseconds(start_time):
        delta = datetime.datetime.now() - start_time
        milliseconds = delta.total_seconds() * 1000
        return milliseconds
    @staticmethod
    def generate_random_array(size, minimum, maximum):
        return [random.randint(minimum, maximum) for _ in range(size)]
if __name__ == "__main__":
    Sorts()
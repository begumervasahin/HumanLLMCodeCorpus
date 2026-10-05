import ctypes
import random
import time
class SortAlgorithm:
    def __init__(self, array):
        self.array = array
        self.array_accesses = 0
        self.extra_memory = 0
        self.recursive_calls = 0
    def sort(self):
        pass
class SelectionSort(SortAlgorithm):
    def sort(self):
        for i in range(len(self.array) - 1, 0, -1):
            max_position = 0
            for location in range(1, i + 1):
                self.array_accesses += 2
                if self.array[location] > self.array[max_position]:
                    max_position = location
            self.array[max_position], self.array[i] = self.array[i], self.array[max_position]
            self.array_accesses += 4
class QuickSort(SortAlgorithm):
    def sort(self):
        self.quick_sort(0, len(self.array) - 1)
    def quick_sort(self, start, end):
        self.recursive_calls += 1
        if start < end:
            pivot = self.partition(start, end)
            self.quick_sort(start, pivot - 1)
            self.quick_sort(pivot + 1, end)
    def partition(self, first, last):
        pivot = self.array[first]
        small = last
        big = first + 1
        while big <= small:
            self.array_accesses += 2
            while big <= last and self.array[big] <= pivot:
                self.array_accesses += 1
                big += 1
            while self.array[small] > pivot:
                self.array_accesses += 1
                small -= 1
            if big < small:
                self.array[big], self.array[small] = self.array[small], self.array[big]
                self.array_accesses += 4
        self.array[first], self.array[small] = self.array[small], self.array[first]
        self.array_accesses += 4
        return small
class MergeSort(SortAlgorithm):
    def sort(self):
        self.array = self.merge_sort(self.array)
    def merge_sort(self, array):
        self.recursive_calls += 1
        n = len(array)
        if n <= 1:
            return array
        left_array = array[:n
        right_array = array[n
        list1 = self.merge_sort(left_array)
        list2 = self.merge_sort(right_array)
        return self.merge(list1, list2)
    def merge(self, l1, l2):
        result = []
        i = j = 0
        while i < len(l1) and j < len(l2):
            self.array_accesses += 2
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        result.extend(l1[i:])
        result.extend(l2[j:])
        return result
class HeapSort(SortAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        self.size = len(array)
    def sort(self):
        self.build_max_heap()
        for i in range(self.size - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.size -= 1
            self.max_heapify(0)
    def build_max_heap(self):
        for i in range(self.size
            self.max_heapify(i)
    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < self.size and self.array[left] > self.array[largest]:
            largest = left
        if right < self.size and self.array[right] > self.array[largest]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.max_heapify(largest)
def create_array(array_size):
    numbers_in_array = (array_size * ctypes.py_object)()
    for value in range(1, array_size + 1):
        numbers_in_array[value - 1] = value
    return numbers_in_array
def shuffle_array(array):
    for element in range(len(array) - 1, 0, -1):
        random_index = random.randint(0, element)
        array[element], array[random_index] = array[random_index], array[element]
    return array
def main():
    while True:
        print("1: Merge Sort\n"
              "2: Heap Sort\n"
              "3: Quick Sort\n"
              "4: Selection Sort\n"
              "5: Exit\n")
        try:
            user_input = int(input("Enter your choice:\t"))
            if user_input < 1 or user_input > 5:
                print("\nInvalid input. Try Again!\n\n")
                continue
            array_size = int(input("Enter the number of elements in the Array:\t"))
        except:
            print("\nInvalid input. Try again!\n\n")
            continue
        unsorted_array = create_array(array_size)
        shuffle_array(unsorted_array)
        print("Array Before Sorting:")
        print(", ".join(map(str, unsorted_array)) + "\n")
        starting_time = time.time()
        if user_input == 1:
            print("***Merge Sort***")
            sorted_array = MergeSort(unsorted_array)
        elif user_input == 2:
            print("***Heap Sort***")
            sorted_array = HeapSort(unsorted_array)
        elif user_input == 3:
            print("***Quick Sort***")
            sorted_array = QuickSort(unsorted_array, 0, len(unsorted_array) - 1)
        elif user_input == 4:
            print("***Selection Sort***")
            sorted_array = SelectionSort(unsorted_array)
        elif user_input == 5:
            print("\nExiting program...\n")
            exit()
        elapsed_time = time.time() - starting_time
        print("Array After Sorting:")
        print(", ".join(map(str, sorted_array.array)) + "\n")
        print("Elapsed Time:\t\t\t\t\t\t\t", elapsed_time, "seconds")
        print("Number of Array Accesses:\t\t\t\t\t" + str(sorted_array.array_accesses))
        print("Number of Extra Memory Space Occupied:\t\t" + str(sorted_array.extra_memory))
        print("Number of Recursive Calls:\t\t\t\t\t" + str(sorted_array.recursive_calls), end="\n\n\n")
if __name__ == "__main__":
    main()
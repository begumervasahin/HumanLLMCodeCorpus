from random import randint
A = []
B = []
C = []
D = []
def random_array_generator(array, size):
    while size > 0:
        array.append(randint(0, 10000))
        size -= 1
random_array_generator(A, 10)
random_array_generator(B, 100)
random_array_generator(C, 1000)
random_array_generator(D, 10000)
class SortAlgorithm:
    def __init__(self):
        self.comparisons = 0
    def quick_sort(self, array, start, end):
        if start < end:
            self.comparisons += 1
            pivot_index = self.partition(array, start, end)
            self.comparisons += 1
            self.quick_sort(array, start, pivot_index - 1)
            self.comparisons += 1
            self.quick_sort(array, pivot_index + 1, end)
            self.comparisons += 1
    def partition(self, array, start, end):
        pivot = array[end]
        pivot_index = start - 1
        for j in range(start, end):
            self.comparisons += 1
            if array[j] <= pivot:
                pivot_index += 1
                array[pivot_index], array[j] = array[j], array[pivot_index]
        array[pivot_index + 1], array[end] = array[end], array[pivot_index + 1]
        return pivot_index + 1
def run_quick_algorithm(array):
    print("Original Array:", array)
    sorter = SortAlgorithm()
    sorter.quick_sort(array, 0, len(array) - 1)
    print("Sorted Array:", array)
    print("Number of comparisons:", sorter.comparisons)
def main():
    run_quick_algorithm(B)
if __name__ == "__main__":
    main()
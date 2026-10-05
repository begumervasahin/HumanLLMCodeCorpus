from random import randint
A = []
B = []
C = []
D = []
def random_array_generator(Array, size):
    for _ in range(size):
        Array.append(randint(0, 10000))
random_array_generator(A, 10)
random_array_generator(B, 100)
random_array_generator(C, 1000)
random_array_generator(D, 10000)
class SortAlgorithm:
    def __init__(self):
        self.counter_quick = 0
    def quick_sort(self, Array, start, end):
        if start < end:
            pivot_index = self.partition(Array, start, end)
            self.quick_sort(Array, start, pivot_index - 1)
            self.quick_sort(Array, pivot_index + 1, end)
    def partition(self, Array, start, end):
        pivot = Array[end]
        pivot_index = start - 1
        for j in range(start, end):
            if Array[j] <= pivot:
                pivot_index += 1
                Array[pivot_index], Array[j] = Array[j], Array[pivot_index]
        Array[pivot_index + 1], Array[end] = Array[end], Array[pivot_index + 1]
        return pivot_index + 1
def run_quick_algorithm(Array):
    print("Original Array:", Array)
    sorter = SortAlgorithm()
    sorter.quick_sort(Array, 0, len(Array) - 1)
    print("Sorted Array:", Array)
    print("Number of comparisons:", sorter.counter_quick)
def main():
    run_quick_algorithm(B)
if __name__ == "__main__":
    main()
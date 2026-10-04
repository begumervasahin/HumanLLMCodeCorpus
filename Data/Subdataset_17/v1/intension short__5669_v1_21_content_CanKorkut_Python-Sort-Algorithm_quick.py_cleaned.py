import random
def random_array_generator(size):
    return [random.randint(0, 10000) for _ in range(size)]
A = random_array_generator(10)
B = random_array_generator(100)
C = random_array_generator(1000)
D = random_array_generator(10000)
sorted_array = list(range(10))
reverse_sorted_array = sorted_array[::-1]
class SortAlgorithm:
    def __init__(self):
        self.counter_quick = 0
    def quick_sort(self, array, low, high):
        if low < high:
            self.counter_quick += 1
            pivot_index = self.partition(array, low, high)
            self.counter_quick += 1
            self.quick_sort(array, low, pivot_index - 1)
            self.counter_quick += 1
            self.quick_sort(array, pivot_index + 1, high)
            self.counter_quick += 1
    def partition(self, array, low, high):
        pivot = array[high]
        self.counter_quick += 1
        i = low - 1
        for j in range(low, high):
            self.counter_quick += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                self.counter_quick += 1
        array[i + 1], array[high] = array[high], array[i + 1]
        self.counter_quick += 1
        return i + 1
def run_quick_algorithm(array):
    print("Original Array:", array)
    sorter = SortAlgorithm()
    sorter.quick_sort(array, 0, len(array) - 1)
    print("Sorted Array:", array)
    print("Operation Count:", sorter.counter_quick)
def main():
    run_quick_algorithm(B)
if __name__ == "__main__":
    main()
from random import randint
def generate_random_array(size, upper_limit=10000):
    return [randint(0, upper_limit) for _ in range(size)]
A = generate_random_array(10)
B = generate_random_array(100)
C = generate_random_array(1000)
D = generate_random_array(10000)
sorted_array = list(range(10))
reverse_sorted_array = list(range(9, -1, -1))
class SortAlgorithm:
    def __init__(self):
        self.quick_sort_steps = 0
    def quick_sort(self, array, low, high):
        if low < high:
            self.quick_sort_steps += 1
            pivot_index = self.partition(array, low, high)
            self.quick_sort_steps += 1
            self.quick_sort(array, low, pivot_index - 1)
            self.quick_sort_steps += 1
            self.quick_sort(array, pivot_index + 1, high)
            self.quick_sort_steps += 1
    def partition(self, array, low, high):
        pivot = array[high]
        self.quick_sort_steps += 1
        i = low - 1
        for j in range(low, high):
            self.quick_sort_steps += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                self.quick_sort_steps += 1
        array[i + 1], array[high] = array[high], array[i + 1]
        self.quick_sort_steps += 1
        return i + 1
def run_quick_sort(array):
    print("Original array:", array)
    sorter = SortAlgorithm()
    sorter.quick_sort(array, 0, len(array) - 1)
    print("Sorted array:", array)
    print("QuickSort steps:", sorter.quick_sort_steps)
def main():
    run_quick_sort(B)
if __name__ == "__main__":
    main()
import random
def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]
small_array = generate_random_array(10)
medium_array = generate_random_array(100)
large_array = generate_random_array(1000)
extra_large_array = generate_random_array(10000)
sorted_array = list(range(10))
reverse_sorted_array = sorted_array[::-1]
class Sorter:
    def __init__(self):
        self.comparison_count = 0
    def quick_sort(self, array, low, high):
        if low < high:
            pivot_index = self.partition(array, low, high)
            self.quick_sort(array, low, pivot_index - 1)
            self.quick_sort(array, pivot_index + 1, high)
    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            self.comparison_count += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
def run_quick_sort(array):
    print("Original Array:", array)
    sorter = Sorter()
    sorter.quick_sort(array, 0, len(array) - 1)
    print("Sorted Array:", array)
    print("Total Comparisons Made:", sorter.comparison_count)
def main():
    run_quick_sort(medium_array)
if __name__ == "__main__":
    main()
import time
import random
def selection_sort(array):
    start_time = time.time()
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    end_time = time.time()
    print(f"Time taken to sort the array: {end_time - start_time:.6f} seconds")
    return array
def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]
def print_list(array):
    print(array)
if __name__ == "__main__":
    array = generate_random_list(100, 0, 1000)
    print("Original array:")
    print_list(array)
    sorted_array = selection_sort(array)
    print("Sorted array:")
    print_list(sorted_array)
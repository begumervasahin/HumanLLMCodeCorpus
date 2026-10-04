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
    print(f"Time taken to sort the array: {end_time - start_time} seconds")
    return array
if __name__ == "__main__":
    array = [random.randint(0, 1000) for _ in range(100)]
    print("Original array:", array)
    sorted_array = selection_sort(array)
    print("Sorted array:", sorted_array)
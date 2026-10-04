import time
import random
def selection_sort(array):
    start_time = time.time()
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    end_time = time.time()
    print(f"Sorting completed in {end_time - start_time} seconds")
    return array
array = [random.randint(0, 100) for _ in range(10)]
sorted_array = selection_sort(array)
print("Sorted array:", sorted_array)
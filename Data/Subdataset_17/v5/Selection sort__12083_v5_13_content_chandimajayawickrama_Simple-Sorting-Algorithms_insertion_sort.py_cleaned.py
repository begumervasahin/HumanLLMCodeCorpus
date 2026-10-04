import time
import random
def insertion_sort(array):
    start_time = time.time()
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    end_time = time.time()
    print(f"Sorted array: {array}")
    print(f"Time taken: {end_time - start_time} seconds")
    return array
if __name__ == "__main__":
    array = [random.randint(0, 100) for _ in range(10)]
    print(f"Original array: {array}")
    insertion_sort(array)
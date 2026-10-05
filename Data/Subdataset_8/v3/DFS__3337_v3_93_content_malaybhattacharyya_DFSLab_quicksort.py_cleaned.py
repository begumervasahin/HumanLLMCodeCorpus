from random import randint, sample
import sys
import time
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
def randomized_partition(arr, start, end):
    random_index = randint(start, end)
    arr[end], arr[random_index] = arr[random_index], arr[end]
    return partition(arr, start, end)
def quicksort(arr, start, end):
    if end > start:
        pivot_index = partition(arr, start, end)
        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s <number of elements>' % sys.argv[0])
    N = int(sys.argv[1])
    if N <= 0:
        sys.exit('Usage: %s <number of elements>' % sys.argv[0])
    numbers = sample(range(1000000), N)
    start_time = time.process_time()
    for _ in range(1000):
        array_copy = numbers.copy()
        quicksort(array_copy, 0, N - 1)
        for i in range(N - 1):
            assert array_copy[i] <= array_copy[i + 1]
    end_time = time.process_time()
    print("Execution time:", end_time - start_time)
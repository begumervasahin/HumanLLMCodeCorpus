import time
from random import randint
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
def main():
    print("Quick Sort Performance Test")
    randlists = []
    start_times = []
    end_times = []
    input_size = 100000
    max_size = 10000000
    step = 1100000
    while input_size <= max_size:
        randlist = [randint(1, input_size) for _ in range(input_size)]
        randlists.append(randlist)
        print(f"Sorting list of size {input_size}...")
        start_time = time.time()
        start_times.append(start_time)
        quick_sort(randlist, 0, len(randlist) - 1)
        end_time = time.time()
        end_times.append(end_time)
        print(f"Time taken for input size {input_size}: {end_time - start_time} seconds")
        input_size += step
if __name__ == "__main__":
    main()
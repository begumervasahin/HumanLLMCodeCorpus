import time
comparisons = 0
swaps = 0
def quick_sort(arr):
    global comparisons, swaps
    comparisons = 0
    swaps = 0
    start = time.time()
    sorted_array = sort(arr)
    end = time.time()
    print(f"QUICK SORT\nComparisons: {comparisons}\nSwaps: {swaps}")
    print(f"Time elapsed: {end - start:.4f} seconds\n")
    return sorted_array
def sort(array):
    global comparisons, swaps
    if len(array) <= 1:
        return array
    pivot = array[len(array) - 1]
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]
    comparisons += len(array) - 1
    swaps += 1
    return sort(less) + equal + sort(greater)
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")
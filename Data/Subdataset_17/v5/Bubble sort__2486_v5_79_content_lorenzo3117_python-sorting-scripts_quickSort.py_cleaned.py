import time
comparisons = 0
swaps = 0
def quick_sort(arr):
    global comparisons, swaps
    comparisons = 0
    swaps = 0
    start = time.time()
    sorted_array = _quick_sort(arr)
    end = time.time()
    print(f"QUICK SORT\nComparisons: {comparisons}\nSwaps: {swaps}")
    print(f"Time elapsed: {end - start:.4f} seconds\n")
    return sorted_array
def _quick_sort(array):
    global comparisons, swaps
    if len(array) <= 1:
        return array
    pivot = array[-1]
    less, equal, greater = [], [], []
    for x in array:
        comparisons += 1
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    swaps += len(less) + len(greater)
    return _quick_sort(less) + equal + _quick_sort(greater)
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")
import time
comparisons = 0
swaps = 0
def quick_sort(arr):
    global comparisons, swaps
    comparisons, swaps = 0, 0
    start_time = time.time()
    sorted_arr = quick_sort_recursive(arr)
    end_time = time.time()
    print("QUICK SORT")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print(f"Time elapsed: {end_time - start_time:.4f} seconds\n")
    return sorted_arr
def quick_sort_recursive(array):
    global comparisons, swaps
    if len(array) <= 1:
        return array
    pivot = array[len(array)
    less, equal, greater = [], [], []
    for x in array:
        comparisons += 1
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    swaps += 1
    return quick_sort_recursive(less) + equal + quick_sort_recursive(greater)
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print("Original array:", array)
    sorted_array = quick_sort(array)
    print("Sorted array:", sorted_array)
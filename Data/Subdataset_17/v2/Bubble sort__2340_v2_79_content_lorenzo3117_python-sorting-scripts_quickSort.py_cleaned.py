import time
comparisons = 0
swaps = 0
def quick_sort(arr):
    global comparisons, swaps
    comparisons, swaps = 0, 0
    start = time.time()
    sorted_arr = sort(arr)
    end = time.time()
    print("QUICK SORT")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print(f"Time elapsed: {end - start:.4f} seconds\n")
    return sorted_arr
def sort(array):
    global comparisons, swaps
    if len(array) <= 1:
        return array
    pivot = array[len(array) - 1]
    less, equal, greater = [], [], []
    for x in array:
        if x < pivot:
            comparisons += 1
            less.append(x)
        elif x == pivot:
            comparisons += 1
            equal.append(x)
        else:
            comparisons += 1
            greater.append(x)
    swaps += 1
    return sort(less) + equal + sort(greater)
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print("Original array:", array)
    sorted_array = quick_sort(array)
    print("Sorted array:", sorted_array)
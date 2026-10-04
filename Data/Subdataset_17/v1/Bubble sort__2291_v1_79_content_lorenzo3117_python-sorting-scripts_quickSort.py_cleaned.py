import time
comparisons = 0
swaps = 0
def quickSort(arr):
    global comparisons, swaps
    comparisons, swaps = 0, 0
    start = time.time()
    sorted_arr = sort(arr)
    end = time.time()
    print("QUICK SORT")
    print("Comparisons: " + str(comparisons))
    print("Swaps: " + str(swaps))
    print("Time elapsed: " + str(end - start) + " seconds\n")
    return sorted_arr
def sort(array):
    global comparisons, swaps
    less, equal, greater = [], [], []
    if len(array) > 1:
        pivot = array[len(array) - 1]
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
    else:
        return array
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print("Original array:", array)
    sorted_array = quickSort(array)
    print("Sorted array:", sorted_array)
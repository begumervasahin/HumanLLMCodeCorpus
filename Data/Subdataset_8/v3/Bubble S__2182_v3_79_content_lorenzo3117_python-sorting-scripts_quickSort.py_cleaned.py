import time
def quick_sort(arr):
    comparisons, swaps = quick_sort_recursive(arr)
    return comparisons, swaps
def quick_sort_recursive(array):
    comparisons = 0
    swaps = 0
    if len(array) > 1:
        pivot = array[len(array) - 1]
        less = []
        equal = []
        greater = []
        for x in array:
            if x < pivot:
                comparisons += 1
                less.append(x)
            elif x == pivot:
                comparisons += 1
                equal.append(x)
            elif x > pivot:
                comparisons += 1
                greater.append(x)
        swaps += 1
        comparisons_less, swaps_less = quick_sort_recursive(less)
        comparisons_greater, swaps_greater = quick_sort_recursive(greater)
        return comparisons + comparisons_less + comparisons_greater, swaps + swaps_less + swaps_greater
    else:
        return comparisons, swaps
arr = [12, 11, 13, 5, 6, 7]
print("Unsorted array:", arr)
start_time = time.time()
comparisons, swaps = quick_sort(arr)
end_time = time.time()
print("Sorted array:", arr)
print("QUICK SORT")
print("Comparisons:", comparisons)
print("Swaps:", swaps)
print("Time elapsed:", end_time - start_time)
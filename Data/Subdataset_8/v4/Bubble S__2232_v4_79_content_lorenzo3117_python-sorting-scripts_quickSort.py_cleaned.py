import time
comparisons = 0
swaps = 0
def quick_sort(arr):
    start_time = time.time()
    sort(arr)
    end_time = time.time()
    print("QUICK SORT")
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)
    print("Time elapsed:", end_time - start_time, "\n")
def sort(array):
    global comparisons, swaps
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[-1]
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
        return sort(less) + equal + sort(greater)
    else:
        return array
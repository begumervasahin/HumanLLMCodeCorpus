def quicksort(arr):
    pivoter = []
    high_val = []
    low_val = []
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    for i in arr:
        if i < pivot:
            low_val.append(i)
        elif i > pivot:
            high_val.append(i)
        else:
            pivoter.append(i)
    low = quicksort(low_val)
    high = quicksort(high_val)
    quick_sorted = low + pivoter + high
    return quick_sorted
x = quicksort([1, 3, 5, 2])
print(x)
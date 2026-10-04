def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivoter = []
    high_val = []
    low_val = []
    pivot = arr[0]
    for i in arr:
        if i < pivot:
            low_val.append(i)
        elif i > pivot:
            high_val.append(i)
        else:
            pivoter.append(i)
    low_sorted = quicksort(low_val)
    high_sorted = quicksort(high_val)
    sorted_arr = low_sorted + pivoter + high_sorted
    return sorted_arr
x = quicksort([1, 3, 5, 2])
print(x)
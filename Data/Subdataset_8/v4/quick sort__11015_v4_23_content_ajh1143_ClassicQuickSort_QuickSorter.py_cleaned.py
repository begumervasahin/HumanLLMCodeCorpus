def quicksort(arr):
    pivoter = []
    high_values = []
    low_values = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                low_values.append(i)
            elif i > pivot:
                high_values.append(i)
            else:
                pivoter.append(i)
        low_sorted = quicksort(low_values)
        high_sorted = quicksort(high_values)
        sorted_arr = low_sorted + pivoter + high_sorted
    return sorted_arr
sorted_array = quicksort([1, 3, 5, 2])
print(sorted_array)
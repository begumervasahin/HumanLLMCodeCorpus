def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    low_values = [i for i in arr if i < pivot]
    pivoter = [i for i in arr if i == pivot]
    high_values = [i for i in arr if i > pivot]
    return quicksort(low_values) + pivoter + quicksort(high_values)
sorted_array = quicksort([1, 3, 5, 2])
print(sorted_array)
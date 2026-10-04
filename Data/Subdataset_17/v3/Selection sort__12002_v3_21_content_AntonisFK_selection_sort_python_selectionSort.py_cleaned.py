def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
array_to_sort = [5, 3, 2, 10, 45, 3, 1]
sorted_array = selection_sort(array_to_sort)
print("Sorted array:", sorted_array)
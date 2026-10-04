def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
numbers = [0, 2, 100, 0, 120, 11]
sorted_numbers = selection_sort_descending(numbers)
print(sorted_numbers)

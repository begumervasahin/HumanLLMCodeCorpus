def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
arr = [6, 5, 8, 4, 3, 2, 8, 9, 10, 15, 0]
print("Original list:", arr)
selection_sort(arr)
print("Sorted list:", arr)
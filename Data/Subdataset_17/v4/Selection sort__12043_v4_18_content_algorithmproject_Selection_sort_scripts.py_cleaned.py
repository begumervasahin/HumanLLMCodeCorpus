def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [6, 3, 1, 9, 2, 5, 8, 7, 4]
print("Sorted array:", selection_sort(arr))
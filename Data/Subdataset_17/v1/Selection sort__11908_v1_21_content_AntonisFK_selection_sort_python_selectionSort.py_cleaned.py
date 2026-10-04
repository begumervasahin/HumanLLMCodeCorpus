def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for b in range(i + 1, len(arr)):
            if arr[b] < arr[min_index]:
                min_index = b
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
arr = [5, 3, 2, 10, 45, 3, 1]
selectionSort(arr)
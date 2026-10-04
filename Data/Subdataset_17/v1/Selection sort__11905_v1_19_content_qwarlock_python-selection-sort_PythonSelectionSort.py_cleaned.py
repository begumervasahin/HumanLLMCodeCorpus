def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        smallestNumber = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallestNumber]:
                smallestNumber = j
        arr[i], arr[smallestNumber] = arr[smallestNumber], arr[i]
arr = [6, 5, 8, 4, 3, 2, 8, 9, 10, 15, 0]
print("Original list:", arr)
selectionSort(arr)
print("Sorted list:", arr)
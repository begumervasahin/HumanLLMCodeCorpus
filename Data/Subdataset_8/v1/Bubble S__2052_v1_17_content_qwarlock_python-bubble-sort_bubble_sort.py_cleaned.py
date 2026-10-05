def bubble_sort(arr):
    counter = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            counter += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return counter
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", arr)
counter = bubble_sort(arr)
print("Sorted List:", arr)
print("Number of comparisons:", counter)
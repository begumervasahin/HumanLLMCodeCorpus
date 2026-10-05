def bubble_sort(arr: list[int], counter: int) -> int:
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            counter += 1
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return counter
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", arr)
counter = 0
counter = bubble_sort(arr, counter)
print("Sorted list:", arr)
print("Number of comparisons:", counter)
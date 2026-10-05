def bubble_sort(arr: list[int]) -> tuple[list[int], int]:
    comparisons = 0
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return arr, comparisons
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", arr)
sorted_arr, comparisons = bubble_sort(arr)
print("Sorted list:", sorted_arr)
print("Number of comparisons:", comparisons)
def bubble_sort(arr):
    comparison_count = 0
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            comparison_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparison_count
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", arr)
comparison_count = bubble_sort(arr)
print("Sorted List:", arr)
print("Number of comparisons:", comparison_count)
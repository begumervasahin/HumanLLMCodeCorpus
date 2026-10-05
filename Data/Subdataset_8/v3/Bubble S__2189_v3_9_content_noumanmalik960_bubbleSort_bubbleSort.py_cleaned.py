def bubble_sort(arr):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_swapped = True
arr = [9, 8, 6, 6, 5, 4, 3, 2, 1, 0]
bubble_sort(arr)
print(arr)
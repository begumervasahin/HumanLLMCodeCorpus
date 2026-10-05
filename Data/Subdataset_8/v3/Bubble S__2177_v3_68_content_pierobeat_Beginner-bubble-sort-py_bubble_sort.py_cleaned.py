def bubble_sort(arr):
    while True:
        is_sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        if is_sorted:
            return arr
print(bubble_sort([1, 2, 3, 4, 5, 6]))
print(bubble_sort([2, 1, 4, 3, 6, 5]))
print(bubble_sort([6, 5, 4, 3, 2, 1]))

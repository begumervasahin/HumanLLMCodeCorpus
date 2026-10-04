def selection_sort(arr):
    for last_pos in range(len(arr) - 1, 0, -1):
        max_pos = 0
        for pos in range(1, last_pos + 1):
            if arr[pos] > arr[max_pos]:
                max_pos = pos
        arr[last_pos], arr[max_pos] = arr[max_pos], arr[last_pos]
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(arr)
print(arr)
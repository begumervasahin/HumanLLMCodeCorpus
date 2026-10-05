def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
my_arr = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
sorted_arr = selection_sort(my_arr)
print(sorted_arr)
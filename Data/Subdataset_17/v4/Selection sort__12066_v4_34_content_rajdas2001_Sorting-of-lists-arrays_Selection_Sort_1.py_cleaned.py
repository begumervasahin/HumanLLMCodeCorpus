def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr
arr = [49, 25, 26, 2, 99]
sorted_arr = selection_sort(arr)
print("Sorted array is:")
for element in sorted_arr:
    print(element, end=' ')
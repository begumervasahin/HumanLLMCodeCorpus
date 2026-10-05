def quick_sort(arr, left, right):
    if left < right:
        pivot = arr[left]
        partition_index = left
        for i in range(left + 1, right):
            if arr[i] < pivot:
                partition_index += 1
                arr[partition_index], arr[i] = arr[i], arr[partition_index]
        arr[left], arr[partition_index] = arr[partition_index], arr[left]
        quick_sort(arr, left, partition_index)
        quick_sort(arr, partition_index + 1, right)
arr = [3, 6, 8, 1, 5, 2, 7, 4]
quick_sort(arr, 0, len(arr))
print(arr)
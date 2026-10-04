def merge(arr, left, mid, right):
    left_subarray = arr[left:mid+1]
    right_subarray = arr[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1
        k += 1
    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1
    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1
def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left)
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
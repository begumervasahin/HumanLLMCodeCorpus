def quick_sort_lomuto_helper(arr, start, end):
    if len(arr) == 1:
        return arr
    elif start < end:
        pivot = lomuto_partition(arr, start, end)
        quick_sort_lomuto_helper(arr, start, pivot - 1)
        quick_sort_lomuto_helper(arr, pivot + 1, end)
    return arr
def quick_sort_lomuto(arr):
    return quick_sort_lomuto_helper(arr, 0, len(arr) - 1)
def lomuto_partition(arr, start, end):
    i = start
    j = start - 1
    while i < end:
        if arr[i] <= arr[end]:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    arr[end], arr[j + 1] = arr[j + 1], arr[end]
    return j + 1
def quick_sort_hoare_helper(arr, start, end):
    if len(arr) == 1:
        return arr
    if start < end:
        pivot = hoare_partition(arr, start, end)
        quick_sort_hoare_helper(arr, start, pivot)
        quick_sort_hoare_helper(arr, pivot + 1, end)
    return arr
def hoare_partition(arr, start, end):
    flag = True
    i = start - 1
    j = end + 1
    while flag:
        i += 1
        while arr[i] < arr[start]:
            i += 1
        j -= 1
        while arr[j] > arr[start]:
            j -= 1
        if i >= j:
            flag = False
            return j
        else:
            arr[i], arr[j] = arr[j], arr[i]
def quick_sort_hoare(arr):
    return quick_sort_hoare_helper(arr, 0, len(arr) - 1)
arr = [15, 4, 68, 24, 75, 16, 42]
sorted_hoare = quick_sort_hoare(arr.copy())
print("Sorted using Hoare's partition scheme:", sorted_hoare)
sorted_lomuto = quick_sort_lomuto(arr.copy())
print("Sorted using Lomuto's partition scheme:", sorted_lomuto)
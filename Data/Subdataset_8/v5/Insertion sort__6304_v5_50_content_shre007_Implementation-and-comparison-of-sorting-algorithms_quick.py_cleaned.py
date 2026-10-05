import statistics
def pivot_position(arr, first, last):
    low = arr[first]
    high = arr[last]
    mid = (first + last)
    pivot_val = statistics.median([low, arr[mid], high])
    if pivot_val == low:
        pivot_index = first
    elif pivot_val == high:
        pivot_index = last
    else:
        pivot_index = mid
    arr[last], arr[pivot_index] = arr[pivot_index], arr[last]
    pivot = arr[last]
    left = first
    right = last - 1
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
    return right
def quicksort(arr, first, last):
    if first < last:
        p = pivot_position(arr, first, last)
        quicksort(arr, first, p - 1)
        quicksort(arr, p + 1, last)
given_list = [56, 26, 93, 17, 31, 44]
n = len(given_list)
quicksort(given_list, 0, n - 1)
print(given_list)
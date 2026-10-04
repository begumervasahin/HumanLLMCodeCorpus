import statistics
def find_pivot_position(arr, first, last):
    low = arr[first]
    high = arr[last]
    mid = (first + last)
    pivot_value = statistics.median([low, arr[mid], high])
    if pivot_value == low:
        pivot_index = first
    elif pivot_value == high:
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
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
    return right
def quicksort(arr, first, last):
    if first < last:
        pivot = find_pivot_position(arr, first, last)
        quicksort(arr, first, pivot - 1)
        quicksort(arr, pivot + 1, last)
if __name__ == "__main__":
    given_list = [56, 26, 93, 17, 31, 44]
    quicksort(given_list, 0, len(given_list) - 1)
    print("Sorted list:", given_list)
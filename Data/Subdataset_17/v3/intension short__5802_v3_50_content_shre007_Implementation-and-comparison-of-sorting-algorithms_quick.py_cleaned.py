import statistics
def find_pivot_position(arr, first, last):
    low = arr[first]
    mid = arr[(first + last)
    high = arr[last]
    pivot_value = statistics.median([low, mid, high])
    if pivot_value == low:
        pivot_index = first
    elif pivot_value == high:
        pivot_index = last
    else:
        pivot_index = (first + last)
    arr[pivot_index], arr[last] = arr[last], arr[pivot_index]
    left = first
    right = last - 1
    while True:
        while left <= right and arr[left] <= pivot_value:
            left += 1
        while left <= right and arr[right] >= pivot_value:
            right -= 1
        if left > right:
            break
        arr[left], arr[right] = arr[right], arr[left]
    arr[last], arr[right] = arr[right], arr[last]
    return right
def quicksort(arr, first, last):
    if first < last:
        pivot_index = find_pivot_position(arr, first, last)
        quicksort(arr, first, pivot_index - 1)
        quicksort(arr, pivot_index + 1, last)
if __name__ == "__main__":
    given_list = [56, 26, 93, 17, 31, 44]
    quicksort(given_list, 0, len(given_list) - 1)
    print("Sorted list:", given_list)
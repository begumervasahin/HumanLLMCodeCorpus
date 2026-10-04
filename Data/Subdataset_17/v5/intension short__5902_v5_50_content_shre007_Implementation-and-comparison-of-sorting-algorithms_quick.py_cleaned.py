import statistics
def find_pivot_index(arr, first, last):
    mid = (first + last)
    candidates = [arr[first], arr[mid], arr[last]]
    pivot_value = statistics.median(candidates)
    if pivot_value == arr[first]:
        return first
    elif pivot_value == arr[last]:
        return last
    else:
        return mid
def partition(arr, first, last):
    pivot_index = find_pivot_index(arr, first, last)
    arr[pivot_index], arr[last] = arr[last], arr[pivot_index]
    pivot = arr[last]
    left, right = first, last - 1
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[last] = arr[last], arr[left]
    return left
def quicksort(arr, first, last):
    if first < last:
        pivot_index = partition(arr, first, last)
        quicksort(arr, first, pivot_index - 1)
        quicksort(arr, pivot_index + 1, last)
if __name__ == "__main__":
    arr = [56, 26, 93, 17, 31, 44]
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
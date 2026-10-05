def quicksort(arr):
    _quicksort_helper(arr, 0, len(arr) - 1)
def _quicksort_helper(arr, first, last):
    if first < last:
        split_point = _partition(arr, first, last)
        _quicksort_helper(arr, first, split_point - 1)
        _quicksort_helper(arr, split_point + 1, last)
def _partition(arr, first, last):
    pivot_value = arr[first]
    left_mark = first + 1
    right_mark = last
    while left_mark <= right_mark:
        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark += 1
        while arr[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            break
        arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]
    arr[first], arr[right_mark] = arr[right_mark], arr[first]
    return right_mark
if __name__ == "__main__":
    alist = [57, 26, 93, 77, 33, 44, 50, 20]
    quicksort(alist)
    print(alist)
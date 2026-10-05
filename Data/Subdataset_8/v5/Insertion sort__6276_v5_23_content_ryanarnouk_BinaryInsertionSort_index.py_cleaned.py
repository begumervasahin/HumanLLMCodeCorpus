def binary_search(arr, value, start, end):
    if start == end:
        if arr[start] > value:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = (start + end)
    if arr[mid] < value:
        return binary_search(arr, value, mid + 1, end)
    elif arr[mid] > value:
        return binary_search(arr, value, start, mid - 1)
    else:
        return mid
def insertion_sort(arr):
    for i in range(1, len(arr)):
        value_to_insert = arr[i]
        insertion_index = binary_search(arr, value_to_insert, 0, i - 1)
        arr = arr[:insertion_index] + [value_to_insert] + arr[insertion_index:i] + arr[i + 1:]
    return arr
if __name__ == "__main__":
    print("Sorted array:")
    sorted_array = insertion_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54])
    print(sorted_array)
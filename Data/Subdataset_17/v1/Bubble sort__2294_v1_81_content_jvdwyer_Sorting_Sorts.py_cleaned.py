from random import randrange
def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result
def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
    return arr
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle_index = len(arr)
    left_split = arr[:middle_index]
    right_split = arr[middle_index:]
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)
    return merge(left_sorted, right_sorted)
def quick_sort(arr, start, end):
    if start >= end:
        return arr
    pivot_index = randrange(start, end + 1)
    pivot_element = arr[pivot_index]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    less_than_pointer = start
    for i in range(start, end):
        if arr[i] < pivot_element:
            arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
            less_than_pointer += 1
    arr[end], arr[less_than_pointer] = arr[less_than_pointer], arr[end]
    quick_sort(arr, start, less_than_pointer - 1)
    quick_sort(arr, less_than_pointer + 1, end)
    return arr
if __name__ == '__main__':
    array = [randrange(1, 101) for _ in range(10)]
    print("Original array:", array)
    bubble_sorted_array = bubble_sort(array.copy())
    print("Bubble Sorted array:", bubble_sorted_array)
    merge_sorted_array = merge_sort(array.copy())
    print("Merge Sorted array:", merge_sorted_array)
    quick_sorted_array = quick_sort(array.copy(), 0, len(array) - 1)
    print("Quick Sorted array:", quick_sorted_array)
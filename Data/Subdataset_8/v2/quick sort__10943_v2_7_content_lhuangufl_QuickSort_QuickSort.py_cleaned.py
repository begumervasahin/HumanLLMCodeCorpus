def partition(array, start, end):
    pivot_value = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot_value:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1
def quick_sort(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)
if __name__ == '__main__':
    nums = [3, 1, 6, 8, 0]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
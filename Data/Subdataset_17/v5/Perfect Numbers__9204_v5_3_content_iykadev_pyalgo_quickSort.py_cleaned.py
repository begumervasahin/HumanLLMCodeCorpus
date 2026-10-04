def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
def quick_sort_helper(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort_helper(array, low, pivot_index - 1)
        quick_sort_helper(array, pivot_index + 1, high)
def partition(array, low, high):
    pivot = array[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and array[left] <= pivot:
            left += 1
        while array[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            array[left], array[right] = array[right], array[left]
    array[low], array[right] = array[right], array[low]
    return right
array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(array)
print(array)
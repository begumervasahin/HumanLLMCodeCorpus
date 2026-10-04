import random
arr = [random.randrange(100) for _ in range(10)]
def is_sorted(array) -> bool:
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
print("Original array:", arr)
sorted_arr = insertion_sort(arr.copy())
print("Sorted array:", sorted_arr)
is_sorted_correctly = is_sorted(sorted_arr)
print("Is the array sorted correctly?", is_sorted_correctly)
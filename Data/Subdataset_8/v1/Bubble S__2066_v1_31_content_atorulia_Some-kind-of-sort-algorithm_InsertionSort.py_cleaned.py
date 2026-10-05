import random
arr = [random.randrange(100) for i in range(10)]
def checkSort(array) -> bool:
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return True
    return False
def insertion(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
print("Original array:")
print(arr)
print("Sorted array:")
sorted_arr = insertion(arr)
print(sorted_arr)
if checkSort(sorted_arr):
    print("Array is not sorted.")
else:
    print("Array is sorted.")
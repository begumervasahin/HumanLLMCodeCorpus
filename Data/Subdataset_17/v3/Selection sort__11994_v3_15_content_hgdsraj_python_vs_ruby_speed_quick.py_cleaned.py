def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
sorted_arr = bubble_sort(arr)
print("Sorted array:")
print(sorted_arr)
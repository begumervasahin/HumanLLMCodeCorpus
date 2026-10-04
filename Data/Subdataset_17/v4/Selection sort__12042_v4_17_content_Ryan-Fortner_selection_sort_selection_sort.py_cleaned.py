
my_arr = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
sorted_array = selection_sort(my_arr)
print("Sorted array:", sorted_array)
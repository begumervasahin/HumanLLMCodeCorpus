def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
    return arr
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
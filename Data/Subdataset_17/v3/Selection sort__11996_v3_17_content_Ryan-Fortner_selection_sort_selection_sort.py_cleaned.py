def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def print_sorted_array(arr):
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
if __name__ == "__main__":
    my_arr = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    print("Original array:", my_arr)
    print_sorted_array(my_arr)
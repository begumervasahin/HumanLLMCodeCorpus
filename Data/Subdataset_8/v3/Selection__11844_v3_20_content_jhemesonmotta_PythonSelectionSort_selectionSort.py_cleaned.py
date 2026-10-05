def selection_sort(arr):
    for last_unsorted_pos in range(len(arr) - 1, 0, -1):
        largest_pos = 0
        for current_pos in range(1, last_unsorted_pos + 1):
            if arr[current_pos] > arr[largest_pos]:
                largest_pos = current_pos
        arr[last_unsorted_pos], arr[largest_pos] = arr[largest_pos], arr[last_unsorted_pos]
if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(arr)
    print("Sorted array:", arr)
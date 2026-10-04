def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
def print_array(arr, message):
    print(message, arr)
if __name__ == "__main__":
    arr = [6, 5, 8, 4, 3, 2, 8, 9, 10, 15, 0]
    print_array(arr, "Original list:")
    selection_sort(arr)
    print_array(arr, "Sorted list:")
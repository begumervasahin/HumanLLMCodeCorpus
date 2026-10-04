def insertion_sort(arr):
    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
def print_array(arr, message):
    print(message, arr)
if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print_array(arr, "Original list:")
    insertion_sort(arr)
    print_array(arr, "Sorted list:")
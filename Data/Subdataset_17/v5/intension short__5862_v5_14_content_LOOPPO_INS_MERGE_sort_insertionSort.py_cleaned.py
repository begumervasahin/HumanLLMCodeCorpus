def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i - 1
        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = current_value
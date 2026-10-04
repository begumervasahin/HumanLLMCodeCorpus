def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i - 1
        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = current_value
if __name__ == "__main__":
    arr = [32, 13, 14, 15, 98]
    print("Original array:", arr)
    insertion_sort(arr)
    print("Sorted array is:", arr)
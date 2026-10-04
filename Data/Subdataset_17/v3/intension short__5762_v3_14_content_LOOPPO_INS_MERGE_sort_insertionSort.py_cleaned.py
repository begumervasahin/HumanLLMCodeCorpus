def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        position = i - 1
        while position >= 0 and array[position] > current_value:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = current_value
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("Original array:", data)
    insertion_sort(data)
    print("Sorted array:", data)
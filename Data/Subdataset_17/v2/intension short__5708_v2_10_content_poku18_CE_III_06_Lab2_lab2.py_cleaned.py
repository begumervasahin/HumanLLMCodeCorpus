def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        position = i
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1
        array[position] = current_value
    return array
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)
    left_half = array[:mid]
    right_half = array[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)
def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array
if __name__ == '__main__':
    user_input = input("Enter the array items separated by space: ")
    input_array = list(map(int, user_input.split()))
    insertion_sorted = insertion_sort(input_array.copy())
    print("Sorted array using insertion sort is:", insertion_sorted)
    merge_sorted = merge_sort(input_array)
    print("Sorted array using merge sort is:", merge_sorted)
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
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    merged_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1
    merged_array.extend(left[i:])
    merged_array.extend(right[j:])
    return merged_array
if __name__ == '__main__':
    user_input = input("Enter the array items separated by space: ")
    input_array = list(map(int, user_input.split()))
    insertion_sorted_array = insertion_sort(input_array.copy())
    print("Sorted array using insertion sort:", insertion_sorted_array)
    merge_sorted_array = merge_sort(input_array)
    print("Sorted array using merge sort:", merge_sorted_array)
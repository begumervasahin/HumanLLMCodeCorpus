def insertion_sort(array):
    for i in range(1, len(array)):
        current_element = array[i]
        j = i - 1
        while j >= 0 and array[j] > current_element:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_element
    return array
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)
    left_half = array[:mid]
    right_half = array[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
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
    print("Enter the array items separated by space:")
    input_array = list(map(int, input().split()))
    sorted_array_insertion = insertion_sort(input_array.copy())
    sorted_array_merge = merge_sort(input_array.copy())
    print("Sorted array using insertion sort:", sorted_array_insertion)
    print("Sorted array using merge sort:", sorted_array_merge)
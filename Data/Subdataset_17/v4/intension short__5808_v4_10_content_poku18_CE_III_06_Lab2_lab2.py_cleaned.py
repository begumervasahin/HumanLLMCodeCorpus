def insertion_sort(array):
    n = len(array)
    for index in range(1, n):
        current_value = array[index]
        position = index
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
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
if __name__ == '__main__':
    print("Enter the array items separated by space:")
    inparray = list(map(int, input().split()))
    insertion_sorted = insertion_sort(inparray.copy())
    print("Sorted array using insertion sort is:", insertion_sorted)
    merge_sorted = merge_sort(inparray)
    print("Sorted array using merge sort is:", merge_sorted)
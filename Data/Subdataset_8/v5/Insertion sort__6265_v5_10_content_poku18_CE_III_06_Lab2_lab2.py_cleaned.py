def insertion_sort(array):
    n = len(array)
    for index in range(1, n):
        current = array[index]
        position = index
        while position > 0 and array[position - 1] > current:
            array[position] = array[position - 1]
            position -= 1
        array[position] = current
    return array
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)
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
    input_array = list(map(int, input().split()))
    print("Sorted array using insertion sort:", insertion_sort(input_array))
    print("Sorted array using merge sort:", merge_sort(input_array))
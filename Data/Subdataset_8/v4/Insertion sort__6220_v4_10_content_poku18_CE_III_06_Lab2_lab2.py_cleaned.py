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
    if len(array) == 1:
        return array
    if len(array) > 1:
        mid = len(array)
        left = array[:mid]
        right = array[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)
def merge(left, right):
    result = []
    n1 = len(left)
    n2 = len(right)
    i = j = 0
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
if __name__ == '__main__':
    print("Enter the array items separated by space:\n")
    inp_array = list(map(int, input().split()))
    print("Sorted array using insertion sort is:", insertion_sort(inp_array))
    print("Sorted array using merge sort is:", merge_sort(inp_array))
def merge(array, left, middle, right):
    left_part = array[left:middle + 1]
    right_part = array[middle + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1
def merge_sort(array, left, right):
    if left < right:
        middle = (left + right)
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, middle, right)
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print("Original array:", array)
    merge_sort(array, 0, len(array) - 1)
    print("Sorted array:", array)
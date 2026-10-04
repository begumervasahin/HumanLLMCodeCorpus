def merge(array, left, mid, right):
    left_subarray = array[left:mid + 1]
    right_subarray = array[mid + 1:right + 1]
    i, j, k = 0, 0, left
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            array[k] = left_subarray[i]
            i += 1
        else:
            array[k] = right_subarray[j]
            j += 1
        k += 1
    array[k:right + 1] = left_subarray[i:] + right_subarray[j:]
def mergesort(array, left, right):
    if left < right:
        mid = (left + right)
        mergesort(array, left, mid)
        mergesort(array, mid + 1, right)
        merge(array, left, mid, right)
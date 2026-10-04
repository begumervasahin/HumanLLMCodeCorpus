def merge(array, left, mid, right):
    left_subarray = array[left:mid+1]
    right_subarray = array[mid+1:right+1]
    i = j = 0
    k = left
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            array[k] = left_subarray[i]
            i += 1
        else:
            array[k] = right_subarray[j]
            j += 1
        k += 1
    while i < len(left_subarray):
        array[k] = left_subarray[i]
        i += 1
        k += 1
    while j < len(right_subarray):
        array[k] = right_subarray[j]
        j += 1
        k += 1
def mergesort(array, left, right):
    if left < right:
        mid = left + (right - left)
        mergesort(array, left, mid)
        mergesort(array, mid + 1, right)
        merge(array, left, mid, right)
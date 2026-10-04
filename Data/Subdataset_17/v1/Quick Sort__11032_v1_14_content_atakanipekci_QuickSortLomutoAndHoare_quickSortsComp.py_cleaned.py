def quickSortLomutoHelper(arr, start, end):
    if len(arr) == 1:
        return arr
    elif start < end:
        piv = lomutoPartition(arr, start, end)
        quickSortLomutoHelper(arr, start, piv - 1)
        quickSortLomutoHelper(arr, piv + 1, end)
    return arr
def quickSortLomuto(arr):
    return quickSortLomutoHelper(arr, 0, len(arr) - 1)
def lomutoPartition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
def quickSortHoareHelper(arr, start, end):
    if len(arr) == 1:
        return arr
    if start < end:
        piv = hoarePartition(arr, start, end)
        quickSortHoareHelper(arr, start, piv)
        quickSortHoareHelper(arr, piv + 1, end)
    return arr
def hoarePartition(arr, start, end):
    pivot = arr[start]
    i = start - 1
    j = end + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
def quickSortHoare(arr):
    return quickSortHoareHelper(arr, 0, len(arr) - 1)
if __name__ == "__main__":
    arr = [15, 4, 68, 24, 75, 16, 42]
    arr_hoare = arr.copy()
    sorted_hoare = quickSortHoare(arr_hoare)
    print("Sorted using Hoare partition:", sorted_hoare)
    arr_lomuto = arr.copy()
    sorted_lomuto = quickSortLomuto(arr_lomuto)
    print("Sorted using Lomuto partition:", sorted_lomuto)
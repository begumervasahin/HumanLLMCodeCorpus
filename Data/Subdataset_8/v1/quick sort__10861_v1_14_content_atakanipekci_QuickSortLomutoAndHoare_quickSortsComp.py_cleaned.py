def quickSortLomutoHelper(arr, start, end):
    if len(arr) == 1:
        return arr
    elif start < end:
        piv = Lomu(arr, start, end)
        quickSortLomutoHelper(arr, start, piv - 1)
        quickSortLomutoHelper(arr, piv + 1, end)
    return arr
def quickSortLomuto(arr):
    return quickSortLomutoHelper(arr, 0, len(arr) - 1)
def Lomu(arr, start, end):
    i = start
    j = start - 1
    while i < end:
        if arr[i] <= arr[end]:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    arr[end], arr[j + 1] = arr[j + 1], arr[end]
    return j + 1
def quickSortHoareHelper(arr, start, end):
    if len(arr) == 1:
        return arr
    if start < end:
        piv = HoaHoaHoa(arr, start, end)
        quickSortHoareHelper(arr, start, piv)
        quickSortHoareHelper(arr, piv + 1, end)
    return arr
def HoaHoaHoa(arr, start, end):
    flag = True
    i = start - 1
    j = end + 1
    while flag:
        i += 1
        while arr[i] < arr[start]:
            i += 1
        j -= 1
        while arr[j] > arr[start]:
            j -= 1
        if i >= j:
            flag = False
            return j
        else:
            arr[i], arr[j] = arr[j], arr[i]
def quickSortHoare(arr):
    return quickSortHoareHelper(arr, 0, len(arr) - 1)
arr = [15, 4, 68, 24, 75, 16, 42]
qsh = quickSortHoare(arr.copy())
print("Sorted using Hoare's partition scheme:", qsh)
qsl = quickSortLomuto(arr.copy())
print("Sorted using Lomuto's partition scheme:", qsl)
def merge(arr, left, right, mid):
    if left == mid == right:
        return
    a = [0] * (mid - left + 1)
    b = [0] * (right - mid)
    for i in range(0, mid - left + 1):
        a[i] = arr[i + left]
    for i in range(0, right - mid):
        b[i] = arr[i + mid + 1]
    k = left
    j = 0
    for i in range(0, len(a)):
        while j < len(b) and a[i] > b[j]:
            arr[k] = b[j]
            j += 1
            k += 1
        arr[k] = a[i]
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1
def merge_sort(arr, left, right):
    mid = left + round((right - left) / 2)
    if right == left:
        return
    elif (right - left) == 1:
        merge(arr, left, right, mid)
    else:
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
    merge(arr, left, right, mid)
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
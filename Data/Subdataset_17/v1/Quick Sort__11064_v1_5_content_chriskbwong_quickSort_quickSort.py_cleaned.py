def partition(arr, l, h):
    i = l - 1
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1
def quickSort(arr, l, h):
    size = h - l + 1
    stack = [0] * size
    top = -1
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        p = partition(arr, l, h)
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h
if __name__ == "__main__":
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in arr:
        print(i, end=" ")
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quickSort(arr, low, high):
    size = high - low + 1
    stack = [0] * size
    top = -1
    top += 1
    stack[top] = low
    top += 1
    stack[top] = high
    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
        pivot_index = partition(arr, low, high)
        if pivot_index - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = pivot_index - 1
        if pivot_index + 1 < high:
            top += 1
            stack[top] = pivot_index + 1
            top += 1
            stack[top] = high
if __name__ == "__main__":
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array is:")
    for element in arr:
        print(element, end=" ")
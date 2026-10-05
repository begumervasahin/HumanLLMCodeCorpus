def heapify(arr, n, i):
    count = 0
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child
    if largest != i:
        count += 1
        arr[i], arr[largest] = arr[largest], arr[i]
        count += heapify(arr, n, largest)
    return count
def heap_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        count += heapify(arr, i, 0)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        count += heapify(arr, i, 0)
    return "HEAP SORT:\nComparisons: " + str(count)
arr = [12, 11, 13, 5, 6, 7]
print("Unsorted array:", arr)
print(heap_sort(arr.copy()))
print("Sorted array:", arr)
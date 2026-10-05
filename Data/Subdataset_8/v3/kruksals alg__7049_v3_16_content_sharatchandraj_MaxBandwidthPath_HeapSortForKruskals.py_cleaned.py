def heapify(arr, heap_size, root_index):
    largest = root_index
    left_child_index = 2 * root_index + 1
    right_child_index = 2 * root_index + 2
    if left_child_index < heap_size and arr[left_child_index] > arr[largest]:
        largest = left_child_index
    if right_child_index < heap_size and arr[right_child_index] > arr[largest]:
        largest = right_child_index
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)
def heap_sort(arr):
    n = len(arr)
    for i in range(n
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    heap_sort(arr)
    print("Sorted array:", arr)
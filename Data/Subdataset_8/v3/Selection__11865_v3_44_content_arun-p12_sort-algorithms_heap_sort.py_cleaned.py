import common as c
def heap_sort(arr, verbose=0, desc=0):
    def heapify(parent_idx, size):
        largest = parent_idx
        left_child = 2 * parent_idx + 1
        right_child = 2 * parent_idx + 2
        if left_child < size and arr[left_child] > arr[largest]:
            largest = left_child
        if right_child < size and arr[right_child] > arr[largest]:
            largest = right_child
        if verbose == 2:
            print("  Subtree:", parent_idx, size, " :: ", arr)
        if largest != parent_idx:
            arr[parent_idx], arr[largest] = c.swap(arr[parent_idx], arr[largest])
            heapify(largest, size)
    def build_max_heap():
        size = len(arr)
        for i in range(size
            heapify(i, size)
            if verbose:
                print("Iteration")
    def heap_sort_operation():
        size = len(arr)
        build_max_heap()
        for i in range(size - 1, 0, -1):
            arr[0], arr[i] = c.swap(arr[0], arr[i])
            heapify(0, i)
            if verbose:
                print("Iteration")
    heap_sort_operation()
    if desc:
        arr = arr[::-1]
    return arr

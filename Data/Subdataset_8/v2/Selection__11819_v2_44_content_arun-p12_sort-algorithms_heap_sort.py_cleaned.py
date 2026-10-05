import common as c
def heap_sort(arr, verbose=0, desc=0):
    def heapify(i, size):
        parent = i
        left_child = i * 2 + 1
        right_child = left_child + 1
        if left_child < size and arr[left_child] > arr[parent]:
            parent = left_child
        if right_child < size and arr[right_child] > arr[parent]:
            parent = right_child
        if verbose == 2:
            print("  Subtree:", i, size, " :: ", arr)
        if i != parent:
            arr[i], arr[parent] = c.swap(arr[i], arr[parent])
            heapify(parent, size)
    def sort():
        size = len(arr)
        for i in range((size
            heapify(i, size)
            if verbose:
                print("Iteration")
        for i in range(size - 1, 0, -1):
            arr[0], arr[i] = c.swap(arr[0], arr[i])
            heapify(0, i)
            if verbose:
                print("Iteration")
    sort()
    if desc:
        arr = arr[::-1]
    return arr

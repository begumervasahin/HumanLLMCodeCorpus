def max_heapify(heap, index):
    n = len(heap)
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    largest = index
    if left_child < n and heap[left_child] > heap[largest]:
        largest = left_child
    if right_child < n and heap[right_child] > heap[largest]:
        largest = right_child
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        max_heapify(heap, largest)
def build_max_heap(heap):
    n = len(heap)
    for i in range(n
        max_heapify(heap, i)
def heapsort(heap):
    build_max_heap(heap)
    n = len(heap)
    for i in range(n - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap[:i], 0)
def heap_maximum(heap):
    return heap[0]
def heap_insert(heap, key):
    heap.append(key)
    i = len(heap) - 1
    while i > 0 and heap[(i - 1)
        heap[i], heap[(i - 1)
        i = (i - 1)
def heap_delete(heap, index):
    heap[index] = heap[-1]
    heap.pop()
    if index < len(heap):
        max_heapify(heap, index)

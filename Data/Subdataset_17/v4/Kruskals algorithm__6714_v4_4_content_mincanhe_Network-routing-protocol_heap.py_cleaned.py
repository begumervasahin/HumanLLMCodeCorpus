def max_heapify(A, i):
    n = len(A)
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and A[left] > A[i]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
def build_max_heap(A):
    n = len(A)
    for i in range(n
        max_heapify(A, i)
def heapsort(A):
    build_max_heap(A)
    n = len(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A[:i], 0)
def heap_maximum(A):
    return A[0]
def heap_insert(A, key):
    A.append(key)
    i = len(A) - 1
    while i > 0 and A[(i - 1)
        A[i], A[(i - 1)
        i = (i - 1)
def heap_delete(A, i):
    A[i] = A[-1]
    A.pop()
    max_heapify(A, i)

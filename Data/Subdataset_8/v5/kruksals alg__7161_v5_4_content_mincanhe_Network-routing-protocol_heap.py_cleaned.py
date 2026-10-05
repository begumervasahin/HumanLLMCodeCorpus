def max_heapify(A, i):
    n = len(A)
    l = 2 * i
    r = 2 * i + 1
    largest = i
    if l <= n and A[l - 1] > A[i - 1]:
        largest = l
    if r <= n and A[r - 1] > A[largest - 1]:
        largest = r
    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        max_heapify(A, largest)
def build_max_heap(A):
    n = len(A)
    for i in range(n
        max_heapify(A, i)
def heapsort(A):
    build_max_heap(A)
    n = len(A)
    for i in range(n, 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        n -= 1
        max_heapify(A[:n], 1)
def heap_maximum(A):
    return A[0]
def heap_insert(A, a):
    A.append(a)
    n = len(A)
    max_heapify(A, n
def heap_delete(A, h):
    n = len(A)
    A[h - 1] = A[n - 1]
    del A[n - 1]
    max_heapify(A, h)
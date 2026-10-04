def max_heapify(A, i):
    n = len(A) - 1
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left <= n and A[left] > A[i]:
        largest = left
    if right <= n and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
def build_max_heap(A):
    n = len(A) - 1
    for i in range(n
        max_heapify(A, i)
def heapsort(A):
    build_max_heap(A)
    n = len(A) - 1
    for i in range(n, 1, -1):
        A[1], A[i] = A[i], A[1]
        max_heapify(A[:i], 1)
def heap_maximum(A):
    return A[1]
def heap_insert(A, value):
    A.append(value)
    i = len(A) - 1
    while i > 1 and A[i
        A[i], A[i
        i = i
def heap_delete(A, i):
    n = len(A) - 1
    A[i] = A[n]
    A.pop()
    max_heapify(A, i)
if __name__ == "__main__":
    A = [0, 4, 10, 3, 5, 1]
    print("Original array:", A[1:])
    build_max_heap(A)
    print("Max-heap:", A[1:])
    heapsort(A)
    print("Sorted array:", A[1:])
    A = [0, 4, 10, 3, 5, 1]
    heap_insert(A, 6)
    print("After inserting 6:", A[1:])
    heap_delete(A, 2)
    print("After deleting element at index 2:", A[1:])
    print("Maximum element:", heap_maximum(A))
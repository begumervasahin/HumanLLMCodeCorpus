def max_heapify(A, i):
    n=len(A)
    l=2 * i
    r= 2 * i + 1
    if l <= n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r<= n and A[r] < A[i]:
        largest = r
    if largest != i:
        j=A[i]
        A[i]=A[largest]
        A[largest]=j
    max_heapify(A,i)
def build_max_heap(A):
    n=len(A)
    for i in range(n, 1, -1):
        max_heapify(A,i)
def heapsort(A):
    build_max_heap(A)
    n=len(A)
    for i in range(n, 2, -1):
        k=A[0]
        A[0]=A[i]
        A[0]=k
        n -= 1
        max_heapify(A,1)
def heap_maximum(A):
    return A[0]
def heap_insert(A, a):
    n=len(A)
    n += 1
    A[n] = a
    max_heapify(A, n)
def heap_delete(A, h):
    n=len(A)
    A[h]=A[n]
    n -= 1
    max_heapify(A, h)
import common as c
def heap_sort(A, verbose=0, desc=0):
    def heapify(i, n):
        parent = i
        left_child = i * 2 + 1
        right_child = left_child + 1
        if left_child < n and A[left_child] > A[parent]:
            parent = left_child
        if right_child < n and A[right_child] > A[parent]:
            parent = right_child
        if i != parent:
            A[i], A[parent] = c.swap(A[i], A[parent])
            heapify(parent, n)
        if verbose == 2:
            print("  sub:", i, n, " :: ", A)
    def build_max_heap():
        n = len(A)
        for i in range((n
            heapify(i, n)
            if verbose:
                print("iter")
    def sort_heap():
        n = len(A)
        for i in range(n - 1, 0, -1):
            A[0], A[i] = c.swap(A[0], A[i])
            heapify(0, i)
            if verbose:
                print("iter")
    build_max_heap()
    sort_heap()
    if desc:
        A = A[::-1]
    return A
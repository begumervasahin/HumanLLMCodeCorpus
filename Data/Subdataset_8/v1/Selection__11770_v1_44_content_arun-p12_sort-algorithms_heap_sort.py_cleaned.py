def heap_sort(A, verbose=0, desc=0):
    import common as c
    def heapify(i, n):
        parent = i
        ch_1 = i * 2 + 1
        ch_2 = ch_1 + 1
        while (ch_1 < n and A[ch_1] > A[parent]):
            parent = ch_1
        while (ch_2 < n and A[ch_2] > A[parent]):
            parent = ch_2
        if verbose == 2:
            print("  sub:", i, n, " :: ", A)
        if i != parent:
            A[i], A[parent] = c.swap(A[i], A[parent])
            heapify(parent, n - 1)
    def h_sort():
        n = len(A)
        for i in range((n
            heapify(i, n)
            if verbose:
                print("iter")
        for i in range(n - 1, 0, -1):
            A[0], A[i] = c.swap(A[0], A[i])
            heapify(0, i)
            if verbose:
                print("iter")
    h_sort()
    if desc:
        A = A[::-1]
    return A

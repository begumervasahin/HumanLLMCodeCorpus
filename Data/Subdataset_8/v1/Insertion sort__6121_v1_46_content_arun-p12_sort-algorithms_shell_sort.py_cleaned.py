def shell_sort(A, verbose=0, desc=0):
    def insertion_sort(gap, i=0):
        j, n = (gap + i), len(A)
        if i < 0 or j >= len(A):
            return
        if verbose == 2:
            print("Sub:", i, "-", j, "::", A)
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            insertion_sort(gap, i - gap)
        insertion_sort(gap, i + 1)
    gap = len(A)
    while gap:
        if verbose:
            print("Gap:", gap)
        insertion_sort(gap, 0)
        gap
    if desc:
        A = A[::-1]
    return A
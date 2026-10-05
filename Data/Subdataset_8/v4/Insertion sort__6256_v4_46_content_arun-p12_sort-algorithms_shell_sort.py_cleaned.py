def shell_sort(A, verbose=0, desc=0):
    def insertion_sort(gap, start_index=0):
        j = start_index + gap
        n = len(A)
        if start_index < 0 or j >= n:
            return
        if verbose == 2:
            print("Sub:", start_index, "-", j, "::", A)
        if A[start_index] > A[j]:
            A[start_index], A[j] = A[j], A[start_index]
            insertion_sort(gap, start_index - gap)
        insertion_sort(gap, start_index + 1)
    gap = len(A)
    while gap:
        if verbose:
            print("Gap:", gap)
        insertion_sort(gap)
        gap
    if desc:
        A = A[::-1]
    return A
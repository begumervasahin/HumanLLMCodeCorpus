def insertion_sort(A, verbose=0, desc=0):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
            if verbose == 2:
                print("Sub:", j, "::", A)
        A[j + 1] = key
        if verbose:
            print("Iteration", i, ":", A)
    if desc:
        A = A[::-1]
    return A

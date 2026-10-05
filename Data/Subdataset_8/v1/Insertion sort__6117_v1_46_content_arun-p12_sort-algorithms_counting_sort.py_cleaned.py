def counting_sort(A, verbose=0, desc=0):
    largest = max(A)
    smallest = min(A)
    if smallest:
        A = [x - smallest for x in A]
    if verbose:
        print("Normalized list:", A)
    count = [0] * (largest - smallest + 1)
    n = len(A)
    for i in range(n):
        count[A[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        if verbose == 2:
            print("Sub:", i, "::", count[i], count[i - 1])
    B = [0] * n
    for i in range(n - 1, -1, -1):
        count[A[i]] -= 1
        B[count[A[i]]] = A[i]
        if verbose:
            print("Iteration", i, ":", B)
    if smallest:
        B = [x + smallest for x in B]
    if desc:
        B = B[::-1]
    return B

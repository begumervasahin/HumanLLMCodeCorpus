def fonk1(A):
    for i in range(1, len(A)):
        b1 = A[i]
        b2 = i - 1
        while b2 >= 0 and b1 < A[b2]:
            A[b2 + 1] = A[b2]
            b2 -= 1
        A[b2 + 1] = b1
    return A

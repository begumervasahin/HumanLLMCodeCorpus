def fonk1(A, l, r):
    if l < r:
        b1 = A[l]
        b2 = l
        for i in range(l + 1, r):
            if A[i] < b1:
                b2 += 1
                A[b2], A[i] = A[i], A[b2]
        A[l], A[b2] = A[b2], A[l]
        fonk1(A, l, b2 - 1)
        fonk1(A, b2 + 1, r)
b3 = [3, 6, 8, 1, 5, 2, 7, 4]
fonk1(b3, 0, len(b3))
print(b3)
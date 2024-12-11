def fonk1(A, b1 = 0, desc=0):
    def fonk2(b5, b2 = 0):
        b3 = b2 + b5
        b4 = len(A)
        if b2 < 0 or b3 >= b4:
            return
        if b1 = = 2:
            print("Sub:", b2, "-", b3, "::", A)
        if A[b2] > A[b3]:
            A[b2], A[b3] = A[b3], A[b2]
            fonk2(b5, b2 - b5)
        fonk2(b5, b2 + 1)
    b5 = len(A)
    while b5:
        if b1:
            print("Gap:", b5)
        fonk2(b5)
        b5
    if desc:
        A.reverse()
    return A
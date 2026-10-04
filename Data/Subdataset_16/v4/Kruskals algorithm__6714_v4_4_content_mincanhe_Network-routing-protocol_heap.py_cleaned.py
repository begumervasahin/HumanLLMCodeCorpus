def fonk1(A, b5):
    b1 = len(A)
    b2 = 2 * b5 + 1
    b3 = 2 * b5 + 2
    b4 = b5
    if b2 < b1 and A[b2] > A[b5]:
        b4 = b2
    if b3 < b1 and A[b3] > A[b4]:
        b4 = b3
    if b4 != b5:
        A[b5], A[b4] = A[b4], A[b5]
        fonk1(A, b4)
def fonk2(A):
    b1 = len(A)
    for b5 in range(b1
        fonk1(A, b5)
def fonk3(A):
    fonk2(A)
    b1 = len(A)
    for b5 in range(b1 - 1, 0, -1):
        A[0], A[b5] = A[b5], A[0]
        fonk1(A[:b5], 0)
def fonk4(A):
    return A[0]
def fonk5(A, key):
    A.append(key)
    b5 = len(A) - 1
    while b5 > 0 and A[(b5 - 1)
        A[b5], A[(b5 - 1)
        b5 = (b5 - 1)
def fonk6(A, b5):
    A[b5] = A[-1]
    A.pop()
    fonk1(A, b5)

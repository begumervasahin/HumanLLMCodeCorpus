def fonk1(A, i):
    b1 = len(A)
    b2 = 2 * i
    b3 = 2 * i + 1
    b4 = i
    if b2 <= b1 and A[b2] > A[i]:
        b4 = b2
    if b3 <= b1 and A[b3] > A[b4]:
        b4 = b3
    if b4 != i:
        A[i], A[b4] = A[b4], A[i]
        fonk1(A, b4)
def fonk2(A):
    b1 = len(A)
    for i in range(b1
        fonk1(A, i)
def fonk3(A):
    fonk2(A)
    b1 = len(A)
    for i in range(b1, 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        b1 -= 1
        fonk1(A[:b1], 0)
def fonk4(A):
    return A[0]
def fonk5(A, a):
    A.append(a)
    b1 = len(A)
    fonk1(A, b1
def fonk6(A, h):
    b1 = len(A)
    A[h - 1] = A[b1 - 1]
    del A[b1 - 1]
    fonk1(A, h - 1)
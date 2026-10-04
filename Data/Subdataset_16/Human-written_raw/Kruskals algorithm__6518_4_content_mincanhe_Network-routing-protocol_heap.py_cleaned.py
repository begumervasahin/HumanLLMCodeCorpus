def fonk1(A, i):
    b1 = len(A)
    b2 = 2 * i
    b3 = 2 * i + 1
    if b2 <= b1 and A[b2] > A[i]:
        b4 = b2
    else:
        b4 = i
    if b3<= b1 and A[b3] < A[i]:
        b4 = b3
    if b4 != i:
        b5 = A[i]
        A[i]=A[b4]
        A[b4]=b5
    fonk1(A,i)
def fonk2(A):
    b1 = len(A)
    for i in range(b1, 1, -1):
        fonk1(A,i)
def fonk3(A):
    fonk2(A)
    b1 = len(A)
    for i in range(b1, 2, -1):
        b6 = A[0]
        A[0]=A[i]
        A[0]=b6
        b1 -= 1
        fonk1(A,1)
def fonk4(A):
    return A[0]
def fonk5(A, a):
    b1 = len(A)
    b1 += 1
    A[b1] = a
    fonk1(A, b1)
def fonk6(A, h):
    b1 = len(A)
    A[h]=A[b1]
    b1 -= 1
    fonk1(A, h)
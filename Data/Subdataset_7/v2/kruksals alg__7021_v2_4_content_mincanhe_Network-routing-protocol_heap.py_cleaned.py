def fonk1(A, b5):
    b1 = len(A)
    b2 = 2 * b5
    b3 = 2 * b5 + 1
    b4 = b5
    if b2 <= b1 and A[b2 - 1] > A[b5 - 1]:
        b4 = b2
    if b3 <= b1 and A[b3 - 1] > A[b4 - 1]:
        b4 = b3
    if b4 != b5:
        A[b5 - 1], A[b4 - 1] = A[b4 - 1], A[b5 - 1]
        fonk1(A, b4)
def fonk2(A):
    b1 = len(A)
    for b5 in range(b1
        fonk1(A, b5)
def fonk3(A):
    fonk2(A)
    b1 = len(A)
    for b5 in range(b1, 1, -1):
        A[0], A[b5 - 1] = A[b5 - 1], A[0]
        b1 -= 1
        fonk1(A[:b1], 1)
def fonk4(A):
    return A[0]
def fonk5(A, a):
    A.append(a)
    b5 = len(A)
    while b5 > 1 and A[b5
        A[b5
        b5
def fonk6(A, h):
    A[h - 1] = A[-1]
    del A[-1]
    fonk1(A, h)
b6 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print("Original array:", b6)
fonk3(b6)
print("Array after heapsort:", b6)
fonk5(b6, 20)
print("Array after inserting 20:", b6)
fonk6(b6, 2)
print("Array after deleting element at index 2:", b6)
print("Maximum element in the heap:", fonk4(b6))